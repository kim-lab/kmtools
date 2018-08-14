import logging
from pathlib import Path
from typing import List, NamedTuple, Optional, Tuple

from Bio.AlignIO import MultipleSeqAlignment
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from kmbio.PDB import Chain, Model, Residue, Structure

from kmtools import structure_tools

logger = logging.getLogger(__name__)


class DomainTarget(NamedTuple):
    structure_id: str
    model_id: int
    chain_id: str
    #: Sequence of the target protein, with gaps in the alignmend indicated with '-'
    target_sequence: str
    #: Sequence of the template protein, with gaps in the alignment indicated with '-'
    template_sequence: str
    template_start: Optional[int] = None
    template_end: Optional[int] = None


def write_pir_alignment(alignment: MultipleSeqAlignment, file: Path):
    """Write `alignment` into a pir file."""
    assert len(alignment) == 2
    seqrec_1, seqrec_2 = alignment
    with open(file, "wt") as fout:
        # Sequence
        fout.write(f">P1;{seqrec_1.id}\n")
        fout.write(f"sequence:{seqrec_1.id}:.:.:.:.::::\n")
        fout.write(f"{seqrec_1.seq}*\n\n")
        # Structure
        fout.write(f">P1;{seqrec_2.id}\n")
        fout.write(f"structure:{seqrec_2.id}:.:.:.:.::::\n")
        fout.write(f"{seqrec_2.seq}*\n")


def prepare_for_modeling(
    structure: Structure, targets: List[DomainTarget]
) -> Tuple[Structure, MultipleSeqAlignment]:
    """Return a structure and an alignment that can be provided as input to Modeller."""
    template_structure = Structure(structure.id, [Model(0)])
    # Add amino acid chains
    for chain_id, target in zip(structure_tools.CHAIN_IDS, targets):
        residues = list(structure[target.model_id][target.chain_id].residues)
        if target.template_start is not None and target.template_end is not None:
            residues = residues[target.template_start - 1 : target.template_end]
        chain = Chain(chain_id, residues)
        chain_sequence = structure_tools.get_chain_sequence(chain)
        chain_sequence_expected = target.template_sequence.replace("-", "")
        assert chain_sequence == chain_sequence_expected, (chain_sequence, chain_sequence_expected)
        template_structure[0].add(chain)
    # Extract chain sequences
    target_seq = "/".join([target.target_sequence for target in targets])
    template_seq = "/".join([target.template_sequence for target in targets])
    # Add hetatm chain
    hetatm_chain_final = Chain(
        structure_tools.CHAIN_IDS[structure_tools.CHAIN_IDS.index(chain_id) + 1]
    )
    residue_idx = 0
    for chain in structure.chains:
        hetatm_chain = structure_tools.copy_hetatm_chain(template_structure, chain, r_cutoff=5)
        for residue in hetatm_chain.residues:
            new_residue = Residue(
                id=(residue.id[0], residue_idx + 1, residue.id[2]),
                resname=residue.resname,
                segid=residue.segid,
                children=list(residue.atoms),
            )
            residue_idx += 1
            hetatm_chain_final.add(new_residue)
    if list(hetatm_chain_final.residues):
        template_structure[0].add(hetatm_chain_final)
        # Add hetatm chain sequences
        hetatm_chain_sequence = ""
        for residue in hetatm_chain_final.residues:
            if residue.resname not in ["HOH", "W"]:
                hetatm_chain_sequence += "."
        if hetatm_chain_sequence:
            target_seq += "/" + hetatm_chain_sequence
            template_seq += "/" + hetatm_chain_sequence
    # Generate final alignment
    alignment = MultipleSeqAlignment(
        [SeqRecord(Seq(target_seq), "target"), SeqRecord(Seq(template_seq), template_structure.id)]
    )
    return template_structure, alignment

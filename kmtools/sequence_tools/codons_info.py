"""
DNA tables and other stuff
"""
#: Codon usage probability for different species
USAGE_FREQ = {
    "E.coli": {
        "GGG": 0.15,
        "GGA": 0.11,
        "GGT": 0.34,
        "GGC": 0.4,
        "GAG": 0.31,
        "GAA": 0.69,
        "GAT": 0.63,
        "GAC": 0.37,
        "GTG": 0.37,
        "GTA": 0.15,
        "GTT": 0.26,
        "GTC": 0.22,
        "GCG": 0.36,
        "GCA": 0.21,
        "GCT": 0.16,
        "GCC": 0.27,
        "AGG": 0.02,
        "AGA": 0.04,
        "CGG": 0.1,
        "CGA": 0.06,
        "CGT": 0.38,
        "CGC": 0.4,
        "AAG": 0.23,
        "AAA": 0.77,
        "AAT": 0.45,
        "AAC": 0.55,
        "ATG": 1.0,
        "ATA": 0.07,
        "ATT": 0.51,
        "ATC": 0.42,
        "ACG": 0.27,
        "ACA": 0.13,
        "ACT": 0.17,
        "ACC": 0.44,
        "TGG": 1.0,
        "TGT": 0.45,
        "TGC": 0.55,
        "TAG": 0.07,
        "TAA": 0.64,
        "TGA": 0.29,
        "TAT": 0.57,
        "TAC": 0.43,
        "TTT": 0.57,
        "TTC": 0.43,
        "AGT": 0.15,
        "AGC": 0.28,
        "TCG": 0.15,
        "TCA": 0.12,
        "TCT": 0.15,
        "TCC": 0.15,
        "CAG": 0.65,
        "CAA": 0.35,
        "CAT": 0.57,
        "CAC": 0.43,
        "TTG": 0.13,
        "TTA": 0.13,
        "CTG": 0.5,
        "CTA": 0.04,
        "CTT": 0.1,
        "CTC": 0.1,
        "CCG": 0.52,
        "CCA": 0.19,
        "CCT": 0.16,
        "CCC": 0.12,
    },
    "human": {
        "CTT": 0.13,
        "ACC": 0.36,
        "ACA": 0.28,
        "AAA": 0.42,
        "ATC": 0.48,
        "AAC": 0.54,
        "ATA": 0.16,
        "AGG": 0.2,
        "CCT": 0.28,
        "ACT": 0.24,
        "AGC": 0.24,
        "AAG": 0.58,
        "AGA": 0.2,
        "CAT": 0.41,
        "AAT": 0.46,
        "ATT": 0.36,
        "CTG": 0.41,
        "CTA": 0.07,
        "CTC": 0.2,
        "CAC": 0.59,
        "ACG": 0.12,
        "CAA": 0.25,
        "AGT": 0.15,
        "CCA": 0.27,
        "CCG": 0.11,
        "CCC": 0.33,
        "TAT": 0.43,
        "GGT": 0.16,
        "TGT": 0.45,
        "CGA": 0.11,
        "CAG": 0.75,
        "TCT": 0.18,
        "GAT": 0.46,
        "CGG": 0.21,
        "TTT": 0.45,
        "TGC": 0.55,
        "GGG": 0.25,
        "TAG": 0.2,
        "GGA": 0.25,
        "TGG": 1.0,
        "GGC": 0.34,
        "TAC": 0.57,
        "TTC": 0.55,
        "TCG": 0.06,
        "TTA": 0.07,
        "TTG": 0.13,
        "CGT": 0.08,
        "GAA": 0.42,
        "TAA": 0.28,
        "GCA": 0.23,
        "GTA": 0.11,
        "GCC": 0.4,
        "GTC": 0.24,
        "GCG": 0.11,
        "GTG": 0.47,
        "GAG": 0.58,
        "GTT": 0.18,
        "GCT": 0.26,
        "TGA": 0.52,
        "GAC": 0.54,
        "TCC": 0.22,
        "TCA": 0.15,
        "ATG": 1.0,
        "CGC": 0.19,
    },
}


#: Amino acid to codon translation table
A2C_DICT = {
    "I": ["ATT", "ATC", "ATA"],
    "L": ["CTT", "CTC", "CTA", "CTG", "TTA", "TTG"],
    "V": ["GTT", "GTC", "GTA", "GTG"],
    "F": ["TTT", "TTC"],
    "M": ["ATG"],
    "C": ["TGT", "TGC"],
    "A": ["GCT", "GCC", "GCA", "GCG"],
    "G": ["GGT", "GGC", "GGA", "GGG"],
    "P": ["CCT", "CCC", "CCA", "CCG"],
    "T": ["ACT", "ACC", "ACA", "ACG"],
    "S": ["TCT", "TCC", "TCA", "TCG", "AGT", "AGC"],
    "Y": ["TAT", "TAC"],
    "W": ["TGG"],
    "Q": ["CAA", "CAG"],
    "N": ["AAT", "AAC"],
    "H": ["CAT", "CAC"],
    "E": ["GAA", "GAG"],
    "D": ["GAT", "GAC"],
    "K": ["AAA", "AAG"],
    "R": ["CGT", "CGC", "CGA", "CGG", "AGA", "AGG"],
    "*": ["TAA", "TAG", "TGA"],
}

#: Amino acid to codon translation table
A2C_NNS_DICT = {
    "I": ["ATC"],
    "L": ["CTC", "CTG", "TTG"],
    "V": ["GTC", "GTG"],
    "F": ["TTC"],
    "M": ["ATG"],
    "C": ["TGC"],
    "A": ["GCC", "GCG"],
    "G": ["GGC", "GGG"],
    "P": ["CCC", "CCG"],
    "T": ["ACC", "ACG"],
    "S": ["TCC", "TCG", "AGC"],
    "Y": ["TAC"],
    "W": ["TGG"],
    "Q": ["CAG"],
    "N": ["AAC"],
    "H": ["CAC"],
    "E": ["GAG"],
    "D": ["GAC"],
    "K": ["AAG"],
    "R": ["CGC", "CGG", "AGG"],
    "*": ["TAG"],
}


#: codon to Aminoacid translation table
C2A_DICT = {
    "ATT": "I",
    "ATC": "I",
    "ATA": "I",
    "CTT": "L",
    "CTC": "L",
    "CTA": "L",
    "CTG": "L",
    "TTA": "L",
    "TTG": "L",
    "GTT": "V",
    "GTC": "V",
    "GTA": "V",
    "GTG": "V",
    "TTT": "F",
    "TTC": "F",
    "ATG": "M",
    "TGT": "C",
    "TGC": "C",
    "GCT": "A",
    "GCC": "A",
    "GCA": "A",
    "GCG": "A",
    "GGT": "G",
    "GGC": "G",
    "GGA": "G",
    "GGG": "G",
    "CCT": "P",
    "CCC": "P",
    "CCA": "P",
    "CCG": "P",
    "ACT": "T",
    "ACC": "T",
    "ACA": "T",
    "ACG": "T",
    "TCT": "S",
    "TCC": "S",
    "TCA": "S",
    "TCG": "S",
    "AGT": "S",
    "AGC": "S",
    "TAT": "Y",
    "TAC": "Y",
    "TGG": "W",
    "CAA": "Q",
    "CAG": "Q",
    "AAT": "N",
    "AAC": "N",
    "CAT": "H",
    "CAC": "H",
    "GAA": "E",
    "GAG": "E",
    "GAT": "D",
    "GAC": "D",
    "AAA": "K",
    "AAG": "K",
    "CGT": "R",
    "CGC": "R",
    "CGA": "R",
    "CGG": "R",
    "AGA": "R",
    "AGG": "R",
    "TAA": "*",
    "TAG": "*",
    "TGA": "*",
}


#: Stop codons dict
STOP_DICT = {"TAA": "*", "TAG": "*", "TGA": "*"}
STOP_CODONS = ["TAA", "TAG", "TGA"]

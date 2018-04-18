#!/bin/bash

set -ev

PACKAGE_ROOT_DIR="${RECIPE_DIR}/.."

python -m pytest \
    -c setup.cfg \
    --cov="${SP_DIR}/${PKG_NAME}/${SUBPKG_NAME}" \
    --benchmark-disable \
    --color=yes \
    "${PACKAGE_ROOT_DIR}/tests/${SUBPKG_NAME}"

sudo find / -name '.coverage'

echo "${PACKAGE_ROOT_DIR}"
echo "${SRC_DIR}"

mv .coverage "${PACKAGE_ROOT_DIR}/.coverage"

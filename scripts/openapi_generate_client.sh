#!/bin/sh
# Copyright AGNTCY Contributors (https://github.com/agntcy)
# SPDX-License-Identifier: Apache-2.0
set -x

SPEC_FILE=${SPEC_FILE:-acp-spec/openapi.json}
SPEC_VERSION=$(jq -r '.info.version | capture("(?<version>\\d+)\\.\\d+"; "") | .version' ${SPEC_FILE})

CLIENT_DIR=${CLIENT_DIR:-acp-sync-client-generated}
GEN_PACKAGE_NAME=${GEN_PACKAGE_NAME:-acp_client_v${SPEC_VERSION}}
SDK_SUBPACKAGE_NAME=${SDK_SUBPACKAGE_NAME:-acp_v${SPEC_VERSION}}
OPENAPI_GENERATOR_CLI_ARGS=${OPENAPI_GENERATOR_CLI_ARGS:-"--additional-properties=library=urllib3"}

echo "Generating client..."
docker run --rm \
    -v ${PWD}:/local openapitools/openapi-generator-cli generate \
    -i local/${SPEC_FILE} \
    --package-name "${GEN_PACKAGE_NAME}" \
    ${OPENAPI_GENERATOR_CLI_ARGS} \
    -g python \
    -o local/${CLIENT_DIR}

echo "Modifying Python files..."
for genfile in $(find "${CLIENT_DIR}" -name '*.py'); do
    { cat .spdx_header ${genfile} ; } > ${genfile}.bak && mv ${genfile}.bak ${genfile}
done

echo "Generating spec version file..."
CLIENT_PACKAGE_DIR="${CLIENT_DIR}/${GEN_PACKAGE_NAME}"
cp .spdx_header "${CLIENT_PACKAGE_DIR}/spec_version.py" && \
echo VERSION=$(jq '.info.version' "${SPEC_FILE}") >>"${CLIENT_PACKAGE_DIR}/spec_version.py" && \
echo MAJOR_VERSION="\"${SPEC_VERSION}\"" >>"${CLIENT_PACKAGE_DIR}/spec_version.py" && \
echo MINOR_VERSION=$(jq '.info.version | capture("\\d+\\.(?<version>\\d+)"; "") | .version' "${SPEC_FILE}") >>"${CLIENT_PACKAGE_DIR}/spec_version.py"

echo "Modifying documentation files..."
for genfile in $(find "${CLIENT_DIR}/docs" -name '*.md'); do
    sed -i '' -E -e "s/${GEN_PACKAGE_NAME}/${SDK_SUBPACKAGE_NAME}/" ${genfile}
done

echo "Done."
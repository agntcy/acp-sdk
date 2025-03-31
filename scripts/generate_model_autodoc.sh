#!/bin/bash
# Copyright AGNTCY Contributors (https://github.com/agntcy)
# SPDX-License-Identifier: Apache-2.0
#
# Note: This script generates the sphinx rst docs for the 
# package models.

for model in agntcy_acp/acp_v0/models/[a-z]*.py ; do
    awk -f - "${model}" <<'EOF'
/^class/ && /BaseModel/ { 
    match($2, "[^(]+");
    MODEL = substr($2,RSTART,RLENGTH-RSTART+1);
    printf("\n.. autopydantic_model:: agntcy_acp.models.%s\n", MODEL);
    print("   :members:");
}
/^class/ && /Enum/ { 
    match($2, "[^(]+");
    MODEL = substr($2,RSTART,RLENGTH-RSTART+1);
    printf("\n.. autoclass:: agntcy_acp.models.%s\n", MODEL);
    print("   :members:");
}
EOF
done

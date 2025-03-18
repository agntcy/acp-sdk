#!bin/sh
# SPDX-FileCopyrightText: Copyright (c) 2025 Cisco and/or its affiliates.
# SPDX-License-Identifier: Apache-2.0

docker run --rm \
-v ${PWD}:/local openapitools/openapi-generator-cli generate \
-i local/openapi.yaml \
--package-name acp_client \
-g python \
-o local/acp-client
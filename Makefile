# SPDX-FileCopyrightText: Copyright (c) 2025 Cisco and/or its affiliates.
# SPDX-License-Identifier: Apache-2.0
ACP_SPEC_RELEASE?=main
ACP_SPEC_DIR?=acp-sdk/acp_sdk/acp-spec

ACP_CLIENT_DIR=acp-client
ACP_ASYNC_CLIENT_DIR=acp-async-client

.PHONY: default install generate_acp_client \
	generate_acp_server generate install_test test check all \
	generate_async_acp_client

default: test
install: 
	cd acp-sdk && poetry sync --without generate_server

$(ACP_SPEC_DIR)/openapi.yaml: 
	git submodule update $(ACP_SPEC_DIR)

generate_acp_client: $(ACP_SPEC_DIR)/openapi.yaml
	ACP_SPEC_VERSION=$$(yq '.info.version | sub("\.", "_")' $(ACP_SPEC_DIR)/openapi.yaml) ; \
	docker run --rm \
	-v ${PWD}:/local openapitools/openapi-generator-cli generate \
	-i local/$(ACP_SPEC_DIR)/openapi.yaml \
	--package-name acp_client_v$${ACP_SPEC_VERSION} \
	"--additional-properties=library=urllib3" \
	-g python \
	-o local/$(ACP_CLIENT_DIR)

generate_acp_async_client: $(ACP_SPEC_DIR)/openapi.yaml
	ACP_SPEC_VERSION=$$(yq '.info.version | sub("\.", "_")' $(ACP_SPEC_DIR)/openapi.yaml) ; \
	docker run --rm \
	-v ${PWD}:/local openapitools/openapi-generator-cli generate \
	-i local/$(ACP_SPEC_DIR)/openapi.yaml \
	--package-name acp_async_client_v$${ACP_SPEC_VERSION} \
	"--additional-properties=library=asyncio" \
	-g python \
	-o local/$(ACP_ASYNC_CLIENT_DIR)

generate_acp_server: $(ACP_SPEC_DIR)/openapi.yaml
	poetry new acp-server-stub
	cd acp-server-stub && poetry add fastapi
	cd acp-sdk && \
	poetry sync --with generate_server && \
	poetry run fastapi-codegen --input ../$(ACP_SPEC_DIR)/openapi.yaml \
	--output-model-type pydantic_v2.BaseModel \
	--output ../acp-server-stub/acp_server_stub \
	--generate-routers \
	--disable-timestamp


generate: generate_acp_client generate_acp_server

install_test: 
	cd acp-sdk && poetry sync --with test --without generate_server

test: install_test
	make -C acp-sdk test

check: test
	scripts/check-models.sh

all: install generate test

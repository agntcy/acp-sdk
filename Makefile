# SPDX-FileCopyrightText: Copyright (c) 2025 Cisco and/or its affiliates.
# SPDX-License-Identifier: Apache-2.0
ACP_SPEC_RELEASE?=main
ACP_SPEC_DIR?=acp-sdk/acp_sdk/acp-spec

.PHONY: default install generate_sdk_models generate_acp_client \
	generate_acp_server generate install_test test check all

default: test
install: 
	cd acp-sdk && poetry sync --without generate_server

$(ACP_SPEC_DIR)/openapi.yaml: 
	git submodule update $(ACP_SPEC_DIR)

generate_sdk_models: $(ACP_SPEC_DIR)/openapi.yaml
	-@mkdir acp-models
	ACP_SPEC_VERSION=$$(yq '.info.version | sub("\.", "_")' $(ACP_SPEC_DIR)/openapi.yaml) ; \
	cd acp-sdk && poetry run datamodel-codegen \
		--input acp_sdk/acp-spec/openapi.yaml \
		--input-file-type openapi \
		--output-model-type pydantic_v2.BaseModel \
		--output ../acp-models/models_v$${ACP_SPEC_VERSION}.py \
		--disable-timestamp

generate_acp_client: $(ACP_SPEC_DIR)/openapi.yaml
	ACP_SPEC_VERSION=$$(yq '.info.version | sub("\.", "_")' $(ACP_SPEC_DIR)/openapi.yaml) ; \
	docker run --rm \
	-v ${PWD}:/local openapitools/openapi-generator-cli generate \
	-i local/$(ACP_SPEC_DIR)/openapi.yaml \
	--package-name acp_client_v$${ACP_SPEC_VERSION} \
	--additional-properties=generateSourceCodeOnly=true \
	-g python \
	-o local/acp-client && \
	sed -E -i '' -e 's/^import[[:space:]]+acp_client_v'$${ACP_SPEC_VERSION}'.models$$/from . import models as acp_models/' \
	    -e 's/acp_client_v'$${ACP_SPEC_VERSION}'.models/acp_models/' \
		acp-client/acp_client_v$${ACP_SPEC_VERSION}/api_client.py && \
	sed -E -i '' -e 's/acp_client_v'$${ACP_SPEC_VERSION}'\././' \
	    -e 's/acp_client_v'$${ACP_SPEC_VERSION}'[[:space:]]/. /' \
		acp-client/acp_client_v$${ACP_SPEC_VERSION}/*.py && \
	sed -E -i '' -e 's/acp_client_v'$${ACP_SPEC_VERSION}'\.api\././' \
	    -e 's/acp_client_v'$${ACP_SPEC_VERSION}'\.api[[:space:]]/. /' \
	    -e 's/acp_client_v'$${ACP_SPEC_VERSION}'\./../' \
		acp-client/acp_client_v$${ACP_SPEC_VERSION}/api/*.py && \
	sed -E -i '' -e 's/acp_client_v'$${ACP_SPEC_VERSION}'\.models\././' \
	    -e 's/acp_client_v'$${ACP_SPEC_VERSION}'\.models[[:space:]]/. /' \
		acp-client/acp_client_v$${ACP_SPEC_VERSION}/models/*.py

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


generate: generate_sdk_models generate_acp_client generate_acp_server

install_test: 
	cd acp-sdk && poetry sync --with test --without generate_server

test: install_test
	make -C acp-sdk test

check: test
	scripts/check-models.sh

all: install generate test

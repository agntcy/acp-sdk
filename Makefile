# SPDX-FileCopyrightText: Copyright (c) 2025 Cisco and/or its affiliates.
# SPDX-License-Identifier: Apache-2.0
ACP_SPEC_RELEASE?=main
ACP_SPEC_DIR?=acp-sdk/acp_sdk/acp-spec

ACP_CLIENT_DIR=acp-client-generated
ACP_ASYNC_CLIENT_DIR=acp-async-client-generated

.PHONY: default install generate_acp_client \
	generate_acp_server generate install_test test check all \
	generate_async_acp_client update_python_subpackage

default: test
install: 
	cd acp-sdk && poetry sync --without generate_server

$(ACP_SPEC_DIR)/openapi.yaml: 
	git submodule update $(ACP_SPEC_DIR)

# Generate client and correct models for convenience.
generate_acp_client $(ACP_CLIENT_DIR)/README.md : $(ACP_SPEC_DIR)/openapi.yaml
	ACP_SPEC_VERSION=$$(yq '.info.version | sub("\.\d+", "")' $(ACP_SPEC_DIR)/openapi.yaml) ; \
	ACP_PACKAGE_NAME="acp_client_v$${ACP_SPEC_VERSION}" ; \
	ACP_SDK_SUBPACKAGE_NAME="acp_sdk.v$${ACP_SPEC_VERSION}.acp_client" ; \
	ACP_CLIENT_PACKAGE_DIR="$(ACP_CLIENT_DIR)/acp_client_v$${ACP_SPEC_VERSION}" ; \
	docker run --rm \
	-v ${PWD}:/local openapitools/openapi-generator-cli generate \
	-i local/$(ACP_SPEC_DIR)/openapi.yaml \
	--package-name "$${ACP_PACKAGE_NAME}" \
	"--additional-properties=library=urllib3" \
	-g python \
	-o local/$(ACP_CLIENT_DIR) && \
	for pyfile in $$(find "$${ACP_CLIENT_PACKAGE_DIR}" -name '*.py'); do \
	   { cat .spdx_header $${pyfile} ; } > $${pyfile}.bak && \
		sed -i '' -E -e "s/$${ACP_PACKAGE_NAME}.api_client/$${ACP_SDK_SUBPACKAGE_NAME}.api_client/" \
	    	-e "s/^from[[:space:]]+$${ACP_PACKAGE_NAME}[[:space:]]+import[[:space:]]+rest$$/from . import rest/" \
	    	-e "s/$${ACP_PACKAGE_NAME}.rest/$${ACP_SDK_SUBPACKAGE_NAME}.rest/" \
	    	-e "s/$${ACP_PACKAGE_NAME}.api\\./$${ACP_SDK_SUBPACKAGE_NAME}.api./" \
	    	-e "s/$${ACP_PACKAGE_NAME}/acp_sdk.v$${ACP_SPEC_VERSION}/" $${pyfile}.bak && \
		mv $${pyfile}.bak $${pyfile} ; \
	done && \
	cp .spdx_header "$${ACP_CLIENT_PACKAGE_DIR}/spec_version.py" && \
	echo ACP_VERSION="\""$$(yq '.info.version' $(ACP_SPEC_DIR)/openapi.yaml)"\"" >>"$${ACP_CLIENT_PACKAGE_DIR}/spec_version.py" && \
	echo ACP_MAJOR_VERSION="\"$${ACP_SPEC_VERSION}\"" >>"$${ACP_CLIENT_PACKAGE_DIR}/spec_version.py" && \
	echo ACP_MINOR_VERSION="\""$$(yq '.info.version | sub("\d+\.", "")' $(ACP_SPEC_DIR)/openapi.yaml)"\"" >>"$${ACP_CLIENT_PACKAGE_DIR}/spec_version.py"

generate_acp_async_client $(ACP_ASYNC_CLIENT_DIR)/README.md : $(ACP_SPEC_DIR)/openapi.yaml
	ACP_SPEC_VERSION=$$(yq '.info.version | sub("\.\d+", "")' $(ACP_SPEC_DIR)/openapi.yaml) ; \
	ACP_PACKAGE_NAME="acp_async_client_v$${ACP_SPEC_VERSION}" ; \
	ACP_SDK_SUBPACKAGE_NAME="acp_sdk.v$${ACP_SPEC_VERSION}.acp_async_client" ; \
	ACP_ASYNC_CLIENT_PACKAGE_DIR="$(ACP_ASYNC_CLIENT_DIR)/acp_async_client_v$${ACP_SPEC_VERSION}" ; \
	docker run --rm \
	-v ${PWD}:/local openapitools/openapi-generator-cli generate \
	-i local/$(ACP_SPEC_DIR)/openapi.yaml \
	--package-name "$${ACP_PACKAGE_NAME}" \
	"--additional-properties=library=asyncio" \
	-g python \
	-o local/$(ACP_ASYNC_CLIENT_DIR) && \
	for pyfile in $$(find "$${ACP_ASYNC_CLIENT_PACKAGE_DIR}" -name '*.py'); do \
		{ cat .spdx_header $${pyfile} ; } > $${pyfile}.bak && \
		sed -i '' -E -e "s/$${ACP_PACKAGE_NAME}.api_client/$${ACP_SDK_SUBPACKAGE_NAME}.api_client/" \
	    	-e "s/^from[[:space:]]+$${ACP_PACKAGE_NAME}[[:space:]]+import[[:space:]]+rest$$/from . import rest/" \
	    	-e "s/$${ACP_PACKAGE_NAME}.rest/$${ACP_SDK_SUBPACKAGE_NAME}.rest/" \
	    	-e "s/$${ACP_PACKAGE_NAME}.api\\./$${ACP_SDK_SUBPACKAGE_NAME}.api./" \
	    	-e "s/$${ACP_PACKAGE_NAME}/acp_sdk.v$${ACP_SPEC_VERSION}/" $${pyfile}.bak && \
		mv $${pyfile}.bak $${pyfile} ; \
	done

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

update_python_subpackage: $(ACP_CLIENT_DIR)/README.md $(ACP_ASYNC_CLIENT_DIR)/README.md 
	ACP_SPEC_VERSION=$$(yq '.info.version | sub("\.\d+", "")' $(ACP_SPEC_DIR)/openapi.yaml) ; \
	ACP_CLIENT_PACKAGE_DIR="$(ACP_CLIENT_DIR)/acp_client_v$${ACP_SPEC_VERSION}" ; \
	ACP_ASYNC_CLIENT_PACKAGE_DIR="$(ACP_ASYNC_CLIENT_DIR)/acp_async_client_v$${ACP_SPEC_VERSION}" ; \
	cp -pR "$${ACP_CLIENT_PACKAGE_DIR}/__init__.py" \
		"$${ACP_CLIENT_PACKAGE_DIR}/exceptions.py" \
		"$${ACP_CLIENT_PACKAGE_DIR}/configuration.py" \
		"$${ACP_CLIENT_PACKAGE_DIR}/api_response.py" \
		"$${ACP_CLIENT_PACKAGE_DIR}/models" \
		"$${ACP_CLIENT_PACKAGE_DIR}/spec_version.py" \
		"acp-sdk/acp_sdk/v$${ACP_SPEC_VERSION}/" && \
	cp -pR "$${ACP_CLIENT_PACKAGE_DIR}/api" \
		"$${ACP_CLIENT_PACKAGE_DIR}/api_client.py" \
		"$${ACP_CLIENT_PACKAGE_DIR}/rest.py" \
		"acp-sdk/acp_sdk/v$${ACP_SPEC_VERSION}/acp_client/" && \
	cp -pR "$${ACP_ASYNC_CLIENT_PACKAGE_DIR}/api" \
		"$${ACP_ASYNC_CLIENT_PACKAGE_DIR}/api_client.py" \
		"$${ACP_ASYNC_CLIENT_PACKAGE_DIR}/rest.py" \
		"acp-sdk/acp_sdk/v$${ACP_SPEC_VERSION}/acp_async_client/"


generate: generate_acp_client generate_acp_server

install_test: 
	cd acp-sdk && poetry sync --with test --without generate_server

test: install_test
	make -C acp-sdk test

check: test
	scripts/check-models.sh

all: install generate test

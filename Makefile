# SPDX-FileCopyrightText: Copyright (c) 2025 Cisco and/or its affiliates.
# SPDX-License-Identifier: Apache-2.0
.PHONY: default install generate_acp_client \
	generate_acp_server generate install_test test setup_test check all \
	generate_async_acp_client update_python_subpackage

default: test
install: 
	cd acp-sdk && poetry sync --without generate_server

ACP_SPEC_DIR=acp-spec
ACP_CLIENT_DIR:=acp-sync-client-generated
ACP_SUBPACKAGE_PREFIX=acp_v
ACP_SPEC_FILE:=$(ACP_SPEC_DIR)/openapi.yaml
GEN_ACP_SYNC_PACKAGE_PREFIX:=acp_client_v
SDK_ACP_SYNC_PACKAGE_NAME:=sync_client

$(ACP_SPEC_FILE): 
	git submodule update $(ACP_SPEC_DIR)

# Generate client and correct models for convenience.
generate_acp_client $(ACP_CLIENT_DIR)/README.md : $(ACP_SPEC_FILE)
	ACP_SPEC_VERSION=$$(yq '.info.version | sub("\.\d+", "")' $(ACP_SPEC_FILE)) ; \
	PACKAGE_NAME="$(GEN_ACP_SYNC_PACKAGE_PREFIX)$${ACP_SPEC_VERSION}" ; \
	ACP_SDK_SUBPACKAGE_NAME="acp_sdk.$(ACP_SUBPACKAGE_PREFIX)$${ACP_SPEC_VERSION}.$(SDK_ACP_SYNC_PACKAGE_NAME)" ; \
	ACP_CLIENT_PACKAGE_DIR="$(ACP_CLIENT_DIR)/$(GEN_ACP_SYNC_PACKAGE_PREFIX)$${ACP_SPEC_VERSION}" ; \
	docker run --rm \
	-v ${PWD}:/local openapitools/openapi-generator-cli generate \
	-i local/$(ACP_SPEC_FILE) \
	--package-name "$${PACKAGE_NAME}" \
	"--additional-properties=library=urllib3" \
	-g python \
	-o local/$(ACP_CLIENT_DIR) && \
	for pyfile in $$(find "$${ACP_CLIENT_PACKAGE_DIR}" -name '*.py'); do \
	   { cat .spdx_header $${pyfile} ; } > $${pyfile}.bak && \
		sed -i '' -E -e "s/$${PACKAGE_NAME}.api_client/$${ACP_SDK_SUBPACKAGE_NAME}.api_client/" \
	    	-e "s/^from[[:space:]]+$${PACKAGE_NAME}[[:space:]]+import[[:space:]]+rest$$/from . import rest/" \
	    	-e "s/$${PACKAGE_NAME}.rest/$${ACP_SDK_SUBPACKAGE_NAME}.rest/" \
	    	-e "s/$${PACKAGE_NAME}.api\\./$${ACP_SDK_SUBPACKAGE_NAME}.api./" \
	    	-e "s/$${PACKAGE_NAME}/acp_sdk.$(ACP_SUBPACKAGE_PREFIX)$${ACP_SPEC_VERSION}/" $${pyfile}.bak && \
		mv $${pyfile}.bak $${pyfile} ; \
	done && \
	cp .spdx_header "$${ACP_CLIENT_PACKAGE_DIR}/spec_version.py" && \
	echo ACP_VERSION="\""$$(yq '.info.version' $(ACP_SPEC_DIR)/openapi.yaml)"\"" >>"$${ACP_CLIENT_PACKAGE_DIR}/spec_version.py" && \
	echo ACP_MAJOR_VERSION="\"$${ACP_SPEC_VERSION}\"" >>"$${ACP_CLIENT_PACKAGE_DIR}/spec_version.py" && \
	echo ACP_MINOR_VERSION="\""$$(yq '.info.version | sub("\d+\.", "")' $(ACP_SPEC_DIR)/openapi.yaml)"\"" >>"$${ACP_CLIENT_PACKAGE_DIR}/spec_version.py"

ACP_ASYNC_CLIENT_DIR:=acp-async-client-generated
GEN_ACP_ASYNC_PACKAGE_PREFIX:=acp_async_client_v
SDK_ACP_ASYNC_PACKAGE_NAME:=async_client

generate_acp_async_client $(ACP_ASYNC_CLIENT_DIR)/README.md : $(ACP_SPEC_FILE)
	ACP_SPEC_VERSION=$$(yq '.info.version | sub("\.\d+", "")' $(ACP_SPEC_FILE)) ; \
	PACKAGE_NAME="$(GEN_ACP_ASYNC_PACKAGE_PREFIX)$${ACP_SPEC_VERSION}" ; \
	ACP_SDK_SUBPACKAGE_NAME="acp_sdk.$(ACP_SUBPACKAGE_PREFIX)$${ACP_SPEC_VERSION}.$(SDK_ACP_ASYNC_PACKAGE_NAME)" ; \
	ACP_ASYNC_CLIENT_PACKAGE_DIR="$(ACP_ASYNC_CLIENT_DIR)/$(GEN_ACP_ASYNC_PACKAGE_PREFIX)$${ACP_SPEC_VERSION}" ; \
	docker run --rm \
	-v ${PWD}:/local openapitools/openapi-generator-cli generate \
	-i local/$(ACP_SPEC_FILE) \
	--package-name "$${PACKAGE_NAME}" \
	"--additional-properties=library=asyncio" \
	-g python \
	-o local/$(ACP_ASYNC_CLIENT_DIR) && \
	for pyfile in $$(find "$${ACP_ASYNC_CLIENT_PACKAGE_DIR}" -name '*.py'); do \
		{ cat .spdx_header $${pyfile} ; } > $${pyfile}.bak && \
		sed -i '' -E -e "s/$${PACKAGE_NAME}.api_client/$${ACP_SDK_SUBPACKAGE_NAME}.api_client/" \
	    	-e "s/^from[[:space:]]+$${PACKAGE_NAME}[[:space:]]+import[[:space:]]+rest$$/from . import rest/" \
	    	-e "s/$${PACKAGE_NAME}.rest/$${ACP_SDK_SUBPACKAGE_NAME}.rest/" \
	    	-e "s/$${PACKAGE_NAME}.api\\./$${ACP_SDK_SUBPACKAGE_NAME}.api./" \
	    	-e "s/$${PACKAGE_NAME}/acp_sdk.$(ACP_SUBPACKAGE_PREFIX)$${ACP_SPEC_VERSION}/" $${pyfile}.bak && \
		mv $${pyfile}.bak $${pyfile} ; \
	done

generate_acp_server: $(ACP_SPEC_FILE)
	poetry new acp-server-stub
	cd acp-server-stub && poetry add fastapi
	poetry sync --with generate_server && \
	poetry run fastapi-codegen --input $(ACP_SPEC_FILE) \
	--output-model-type pydantic_v2.BaseModel \
	--output acp-server-stub/acp_server_stub \
	--generate-routers \
	--disable-timestamp

AGENT_WORKFLOW_DIR:=agent-workflow-cli
AGENT_WORKFLOW_CLIENT_DIR?=agent-workflow-client
GEN_AGENT_WORKFLOW_PACKAGE_PREFIX:=agent_workflow_v
SDK_AGENT_WORKFLOW_SUBPACKAGE_PREFIX:=agws_v
AGNT_WKFW_SPEC_FILE:=$(AGENT_WORKFLOW_DIR)/acpilot/spec/manifest.yaml
AGNT_WKFW_ACP_SPEC_FILE:=$(AGENT_WORKFLOW_DIR)/acpilot/spec/acp-spec/openapi.yaml

$(AGNT_WKFW_SPEC_FILE):
	git submodule update $(AGENT_WORKFLOW_DIR)

generate_manifest_models: $(AGNT_WKFW_SPEC_FILE)
	ACP_SPEC_VERSION=$$(yq '.info.version' $(ACP_SPEC_FILE)) ; \
	AGNT_WKFW_ACP_SPEC_VERSION=$$(yq '.info.version' $(AGNT_WKFW_ACP_SPEC_FILE)) ; \
	if [ "$${ACP_SPEC_VERSION}" != "$${AGNT_WKFW_ACP_SPEC_VERSION}" ] ; then \
	  { echo "ERROR: ACP spec version $${ACP_SPEC_VERSION} != $${AGNT_WKFW_ACP_SPEC_VERSION} ACP version in manifest" ; exit 1 ; } ; \
	fi ; \
	AGNT_WKFW_SPEC_VERSION=$$(yq '.info.version | sub("\.\d+", "")' $(AGNT_WKFW_SPEC_FILE)) ; \
	PACKAGE_NAME="$(GEN_AGENT_WORKFLOW_PACKAGE_PREFIX)$${AGNT_WKFW_SPEC_VERSION}" ; \
	docker run --rm \
	-v ${PWD}:/local openapitools/openapi-generator-cli generate \
	-i local/$(AGNT_WKFW_SPEC_FILE) \
	--package-name "$${PACKAGE_NAME}" \
	-g python \
	-o local/$(AGENT_WORKFLOW_CLIENT_DIR) && \
	for pyfile in $$(find "$(AGENT_WORKFLOW_CLIENT_DIR)/$${PACKAGE_NAME}" -name '*.py'); do \
		{ cat .spdx_header $${pyfile} ; } > $${pyfile}.bak && \
		sed -i '' -E -e "s/$${PACKAGE_NAME}/acp_sdk.$(SDK_AGENT_WORKFLOW_SUBPACKAGE_PREFIX)$${AGNT_WKFW_SPEC_VERSION}/" $${pyfile}.bak && \
		mv $${pyfile}.bak $${pyfile} ; \
	done

update_python_subpackage: $(ACP_CLIENT_DIR)/README.md $(ACP_ASYNC_CLIENT_DIR)/README.md $(AGENT_WORKFLOW_CLIENT_DIR)/README.md
	ACP_SPEC_VERSION=$$(yq '.info.version | sub("\.\d+", "")' $(ACP_SPEC_FILE)) ; \
	ACP_CLIENT_PACKAGE_DIR="$(ACP_CLIENT_DIR)/$(GEN_ACP_SYNC_PACKAGE_PREFIX)$${ACP_SPEC_VERSION}" ; \
	ACP_ASYNC_CLIENT_PACKAGE_DIR="$(ACP_ASYNC_CLIENT_DIR)/$(GEN_ACP_ASYNC_PACKAGE_PREFIX)$${ACP_SPEC_VERSION}" ; \
	AGNT_WKFW_SPEC_VERSION=$$(yq '.info.version | sub("\.\d+", "")' $(AGNT_WKFW_SPEC_FILE)) ; \
	AGNT_WKFW_CLIENT_PACKAGE_DIR="$(AGENT_WORKFLOW_CLIENT_DIR)/$(GEN_AGENT_WORKFLOW_PACKAGE_PREFIX)$${AGNT_WKFW_SPEC_VERSION}" ; \
	cp -pR "$${ACP_CLIENT_PACKAGE_DIR}/__init__.py" \
		"$${ACP_CLIENT_PACKAGE_DIR}/exceptions.py" \
		"$${ACP_CLIENT_PACKAGE_DIR}/configuration.py" \
		"$${ACP_CLIENT_PACKAGE_DIR}/api_response.py" \
		"$${ACP_CLIENT_PACKAGE_DIR}/models" \
		"$${ACP_CLIENT_PACKAGE_DIR}/spec_version.py" \
		"acp_sdk/$(ACP_SUBPACKAGE_PREFIX)$${ACP_SPEC_VERSION}/" && \
	cp -pR "$${ACP_CLIENT_PACKAGE_DIR}/api" \
		"$${ACP_CLIENT_PACKAGE_DIR}/api_client.py" \
		"$${ACP_CLIENT_PACKAGE_DIR}/rest.py" \
		"acp_sdk/$(ACP_SUBPACKAGE_PREFIX)$${ACP_SPEC_VERSION}/$(SDK_ACP_SYNC_PACKAGE_NAME)/" && \
	cp -pR "$${ACP_ASYNC_CLIENT_PACKAGE_DIR}/api" \
		"$${ACP_ASYNC_CLIENT_PACKAGE_DIR}/api_client.py" \
		"$${ACP_ASYNC_CLIENT_PACKAGE_DIR}/rest.py" \
		"acp_sdk/$(ACP_SUBPACKAGE_PREFIX)$${ACP_SPEC_VERSION}/$(SDK_ACP_ASYNC_PACKAGE_NAME)/" && \
	cp -pR "$${AGNT_WKFW_CLIENT_PACKAGE_DIR}"/models/*.py \
		"acp_sdk/$(SDK_AGENT_WORKFLOW_SUBPACKAGE_PREFIX)$${AGNT_WKFW_SPEC_VERSION}/models/"


generate: generate_acp_client generate_acp_server

setup_test:
	poetry sync --with test --without generate_server

test: setup_test
	@poetry run pytest --exitfirst -q tests/test_descriptor_validator.py::test_descriptor_validator
	@ACP_SPEC_PATH="$(ACP_SPEC_DIR)/openapi.yaml" poetry run pytest --exitfirst -q tests/test_descriptor_validator.py::test_oas_generator
	poetry run pytest -vv tests/test_acp_client.py tests/test_acp_async_client.py

check: test
	scripts/check-models.sh

all: install generate test

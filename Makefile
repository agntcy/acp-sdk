# SPDX-FileCopyrightText: Copyright (c) 2025 Cisco and/or its affiliates.
# SPDX-License-Identifier: Apache-2.0
.PHONY: default install generate_acp_client \
	generate_acp_server generate install_test test setup_test check all \
	generate_async_acp_client update_python_subpackage

default: test
install: 
	poetry sync

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
	export SPEC_FILE="$(ACP_SPEC_FILE)" ; \
	export SPEC_VERSION=$$(yq '.info.version | sub("\.\d+", "")' "$${SPEC_FILE}") ; \
	export CLIENT_DIR="$(ACP_CLIENT_DIR)" ; \
	export GEN_PACKAGE_NAME="$(GEN_ACP_SYNC_PACKAGE_PREFIX)$${SPEC_VERSION}" ; \
	export SDK_SUBPACKAGE_NAME="agntcy_acp.$(ACP_SUBPACKAGE_PREFIX)$${SPEC_VERSION}" ; \
	export OPENAPI_GENERATOR_CLI_ARGS="--additional-properties=library=urllib3" ; \
	./scripts/openapi_generate_client.sh && \
	export SDK_SYNC_SUBPACKAGE_NAME="$${SDK_SUBPACKAGE_NAME}.$(SDK_ACP_SYNC_PACKAGE_NAME)" ; \
	for genfile in $$(find "$${CLIENT_DIR}" -name '*.py'); do \
		sed -i '' -E -e "s/$${GEN_PACKAGE_NAME}.api_client/$${SDK_SYNC_SUBPACKAGE_NAME}.api_client/" \
	    	-e "s/^from[[:space:]]+$${GEN_PACKAGE_NAME}[[:space:]]+import[[:space:]]+rest$$/from . import rest/" \
	    	-e "s/$${GEN_PACKAGE_NAME}.rest/$${SDK_SYNC_SUBPACKAGE_NAME}.rest/" \
	    	-e "s/$${GEN_PACKAGE_NAME}.api\\./$${SDK_SYNC_SUBPACKAGE_NAME}.api./" \
	    	-e "s/$${GEN_PACKAGE_NAME}/$${SDK_SUBPACKAGE_NAME}/" $${genfile} ; \
	done

ACP_ASYNC_CLIENT_DIR:=acp-async-client-generated
GEN_ACP_ASYNC_PACKAGE_PREFIX:=acp_async_client_v
SDK_ACP_ASYNC_PACKAGE_NAME:=async_client

generate_acp_async_client $(ACP_ASYNC_CLIENT_DIR)/README.md : $(ACP_SPEC_FILE)
	export SPEC_FILE="$(ACP_SPEC_FILE)" ; \
	export SPEC_VERSION=$$(yq '.info.version | sub("\.\d+", "")' "$${SPEC_FILE}") ; \
	export CLIENT_DIR="$(ACP_ASYNC_CLIENT_DIR)" ; \
	export GEN_PACKAGE_NAME="$(GEN_ACP_ASYNC_PACKAGE_PREFIX)$${SPEC_VERSION}" ; \
	export SDK_SUBPACKAGE_NAME="agntcy_acp.$(ACP_SUBPACKAGE_PREFIX)$${SPEC_VERSION}" ; \
	export OPENAPI_GENERATOR_CLI_ARGS="--additional-properties=library=asyncio" ; \
	./scripts/openapi_generate_client.sh && \
	export SDK_ASYNC_SUBPACKAGE_NAME="$${SDK_SUBPACKAGE_NAME}.$(SDK_ACP_ASYNC_PACKAGE_NAME)" ; \
	for genfile in $$(find "$${CLIENT_DIR}" -name '*.py'); do \
		sed -i '' -E -e "s/$${GEN_PACKAGE_NAME}.api_client/$${SDK_ASYNC_SUBPACKAGE_NAME}.api_client/" \
	    	-e "s/^from[[:space:]]+$${GEN_PACKAGE_NAME}[[:space:]]+import[[:space:]]+rest$$/from . import rest/" \
	    	-e "s/$${GEN_PACKAGE_NAME}.rest/$${SDK_ASYNC_SUBPACKAGE_NAME}.rest/" \
	    	-e "s/$${GEN_PACKAGE_NAME}.api\\./$${SDK_ASYNC_SUBPACKAGE_NAME}.api./" \
	    	-e "s/$${GEN_PACKAGE_NAME}/$${SDK_SUBPACKAGE_NAME}/" $${genfile} ; \
	done

AGENT_WORKFLOW_DIR:=workflow-srv-mgr
AGENT_WORKFLOW_CLIENT_DIR?=workflow-srv-mgr-client-generated
GEN_AGENT_WORKFLOW_PACKAGE_PREFIX:=workflow_srv_v
SDK_AGENT_WORKFLOW_SUBPACKAGE_PREFIX:=agws_v
AGNT_WKFW_SPEC_FILE:=$(AGENT_WORKFLOW_DIR)/wfsm/spec/manifest.yaml
AGNT_WKFW_ACP_SPEC_FILE:=$(AGENT_WORKFLOW_DIR)/wfsm/spec/acp-spec/openapi.yaml

$(AGNT_WKFW_SPEC_FILE):
	git submodule update $(AGENT_WORKFLOW_DIR)

generate_manifest_models $(AGENT_WORKFLOW_CLIENT_DIR)/README.md : $(AGNT_WKFW_SPEC_FILE)
	ACP_SPEC_VERSION=$$(yq '.info.version' $(ACP_SPEC_FILE)) ; \
	AGNT_WKFW_ACP_SPEC_VERSION=$$(yq '.info.version' $(AGNT_WKFW_ACP_SPEC_FILE)) ; \
	if [ "$${ACP_SPEC_VERSION}" != "$${AGNT_WKFW_ACP_SPEC_VERSION}" ] ; then \
	  { echo "ERROR: ACP spec version $${ACP_SPEC_VERSION} != $${AGNT_WKFW_ACP_SPEC_VERSION} ACP version in manifest" ; exit 1 ; } ; \
	fi ; \
	export SPEC_FILE="$(AGNT_WKFW_SPEC_FILE)" ; \
	export SPEC_VERSION=$$(yq '.info.version | sub("\.\d+", "")' "$${SPEC_FILE}") ; \
	export CLIENT_DIR="$(AGENT_WORKFLOW_CLIENT_DIR)" ; \
	export GEN_PACKAGE_NAME="$(GEN_AGENT_WORKFLOW_PACKAGE_PREFIX)$${SPEC_VERSION}" ; \
	export SDK_SUBPACKAGE_NAME="$(SDK_AGENT_WORKFLOW_SUBPACKAGE_PREFIX)$${SPEC_VERSION}" ; \
	./scripts/openapi_generate_client.sh && \
	for genfile in $$(find "$${CLIENT_DIR}" -name '*.py'); do \
		sed -i '' -E -e "s/$${GEN_PACKAGE_NAME}/agntcy_acp.$${SDK_SUBPACKAGE_NAME}/" "$${genfile}" ; \
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
		"agntcy_acp/$(ACP_SUBPACKAGE_PREFIX)$${ACP_SPEC_VERSION}/" && \
	cp -pR "$${ACP_CLIENT_PACKAGE_DIR}/api" \
		"$${ACP_CLIENT_PACKAGE_DIR}/api_client.py" \
		"$${ACP_CLIENT_PACKAGE_DIR}/rest.py" \
		"agntcy_acp/$(ACP_SUBPACKAGE_PREFIX)$${ACP_SPEC_VERSION}/$(SDK_ACP_SYNC_PACKAGE_NAME)/" && \
	cp -pR "$${ACP_ASYNC_CLIENT_PACKAGE_DIR}/api" \
		"$${ACP_ASYNC_CLIENT_PACKAGE_DIR}/api_client.py" \
		"$${ACP_ASYNC_CLIENT_PACKAGE_DIR}/rest.py" \
		"agntcy_acp/$(ACP_SUBPACKAGE_PREFIX)$${ACP_SPEC_VERSION}/$(SDK_ACP_ASYNC_PACKAGE_NAME)/" && \
	cp -p "$${AGNT_WKFW_CLIENT_PACKAGE_DIR}"/spec_version.py \
		"agntcy_acp/$(SDK_AGENT_WORKFLOW_SUBPACKAGE_PREFIX)$${AGNT_WKFW_SPEC_VERSION}/" && \
	cp -p "$${AGNT_WKFW_CLIENT_PACKAGE_DIR}"/models/*.py \
		"agntcy_acp/$(SDK_AGENT_WORKFLOW_SUBPACKAGE_PREFIX)$${AGNT_WKFW_SPEC_VERSION}/models/"

update_docs: $(ACP_CLIENT_DIR)/README.md $(ACP_ASYNC_CLIENT_DIR)/README.md $(AGENT_WORKFLOW_CLIENT_DIR)/README.md
	cp -p "$(ACP_CLIENT_DIR)"/docs/*.md docs/models/ && \
	cp -p "$(ACP_ASYNC_CLIENT_DIR)"/docs/*.md docs/models/ && \
	cp -p "$(AGENT_WORKFLOW_CLIENT_DIR)"/docs/*.md docs/models/


generate: generate_acp_client generate_acp_server

setup_test:
	poetry sync --with test

test: setup_test
	ACP_SPEC_PATH="$(ACP_SPEC_DIR)/openapi.yaml" poetry run pytest --exitfirst -vv tests/

check: test
	scripts/check-models.sh

all: install generate test

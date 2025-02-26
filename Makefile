# SPDX-FileCopyrightText: Copyright (c) 2025 Cisco and/or its affiliates.
# SPDX-License-Identifier: Apache-2.0

install: 
	cd acp-sdk && poetry install

generate_sdk_models:
	cd acp-sdk && poetry run datamodel-codegen \
		--input acp_sdk/acp-spec/openapi.yaml \
		--input-file-type openapi \
		--output-model-type pydantic_v2.BaseModel \
		--output acp_sdk/models/models.py \
		--disable-timestamp

generate_acp_client:
	docker run --rm \
	-v ${PWD}:/local openapitools/openapi-generator-cli generate \
	-i local/acp-sdk/acp_sdk/acp-spec/openapi.yaml \
	--package-name acp_client \
	-g python \
	-o local/acp-client

generate_acp_server:
	poetry new acp-server-stub
	cd acp-server-stub && poetry add fastapi
	cd acp-sdk && \
	poetry run fastapi-codegen --input ../acp-sdk/acp_sdk/acp-spec/openapi.yaml \
	--output-model-type pydantic_v2.BaseModel \
	--output ../acp-server-stub/acp_server_stub \
	--generate-routers \
	--disable-timestamp


generate: generate_sdk_models generate_acp_client generate_acp_server

test: install generate_sdk_models
	make -C acp-sdk test

check: test
	@if [[ $$( git status --porcelain ) != "" ]]; then\
		echo "ERROR: stale SDK models. Run 'make generate_sdk_models' and commit again";\
		exit 1;\
	else\
		echo "SDK Models are up to date";\
	fi

all: install generate test

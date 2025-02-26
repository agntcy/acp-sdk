#/bin/bash 

# SPDX-FileCopyrightText: Copyright (c) 2025 Cisco and/or its affiliates.
# SPDX-License-Identifier: Apache-2.0

if [[ $( git status --porcelain ) != "" ]]; then
    echo "ERROR: stale SDK models. Run 'make generate_sdk_models' and commit again";
    git status --porcelain
	exit 1;
else
	echo "SDK Models are up to date";
fi
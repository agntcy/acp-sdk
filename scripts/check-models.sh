#!/usr/bin/env bash 

# SPDX-FileCopyrightText: Copyright (c) 2025 Cisco and/or its affiliates.
# SPDX-License-Identifier: Apache-2.0

CHANGED_FILES="$(git status --porcelain)"

if [[ -n "${CHANGED_FILES}" ]]; then
    echo "ERROR: stale SDK models. Run 'make generate_sdk_models' and commit again";
    echo "Changed files:"
    echo "${CHANGED_FILES}"
    exit 1;
else
    echo "SDK Models are up to date";
fi
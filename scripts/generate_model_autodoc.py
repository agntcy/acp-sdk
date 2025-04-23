# Copyright AGNTCY Contributors (https://github.com/agntcy)
# SPDX-License-Identifier: Apache-2.0
from pydantic import BaseModel
from enum import Enum

import inspect
import importlib

mod = importlib.import_module("agntcy_acp.models")
for model, obj in inspect.getmembers(mod):
    if inspect.isclass(obj):
        if issubclass(obj, BaseModel):
            print(f"\n.. autopydantic_model:: agntcy_acp.models.{model}\n");
            print("   :members:");
        elif issubclass(obj, Enum):
            print(f"\n.. autoclass:: agntcy_acp.models.{model}\n");
            print("   :members:");

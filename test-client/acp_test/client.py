# Copyright AGNTCY Contributors (https://github.com/agntcy)
# SPDX-License-Identifier: Apache-2.0
import builtins
import importlib
import json
from typing import Any, Tuple, Union

from agntcy_acp import ACPClient, AsyncApiClient
from deepdiff import diff

from .types import TestOperation


def _get_class(full_name: str) -> Any:
    names = full_name.rsplit(".", maxsplit=1)
    if len(names) > 1:
        mod = importlib.import_module(names[0])
        return vars(mod)[names[1]]
    elif full_name in vars(builtins):
        # builtin classes, e.g., "str"
        return vars(builtins)[full_name]
    else:
        return globals()[names[0]]


def _get_op_args(
    client: Union[ACPClient, AsyncApiClient],
    operation: TestOperation,
) -> Tuple[Any, Any]:
    op = getattr(client, operation.operation_id)
    args = {}

    if operation.test_input is not None:
        for arg_name, arg_info in operation.test_input.items():
            if arg_info.arguments is not None:
                arg_obj = _get_class(arg_info.type)(**arg_info.arguments)
            elif arg_info.value is not None:
                arg_obj = _get_class(arg_info.type)(arg_info.value)
            else:
                arg_obj = _get_class(arg_info.type)()

            args[arg_name] = arg_obj

    return op, args


def _process_result(
    result: Any, operation: TestOperation, op_idx: int
) -> Tuple[bool, Any]:
    result_dump = result.model_dump(exclude_none=True)
    ret_val = True

    # Check for no modified values
    if operation.output_at_least:
        mapdiff = diff.DeepDiff(
            operation.output_at_least,
            result_dump,
            threshold_to_diff_deeper=0,
            use_enum_value=True,
        )
        if "values_changed" in mapdiff:
            print(
                f"{op_idx}: operation {operation.operation_id}:\n{json.dumps(mapdiff['values_changed'], indent=2)}"
            )
            ret_val = False
    if operation.output_exact:
        result_dump = result.model_dump()
        mapdiff = diff.DeepDiff(operation.output_at_least, result_dump)
        if mapdiff:
            print(
                f"{op_idx}: operation {operation.operation_id}:\n{mapdiff.to_json(indent=2)}"
            )
            ret_val = False

    return ret_val, result_dump


def process_operation(
    client: ACPClient, operation: TestOperation, op_idx: int
) -> Tuple[bool, Any]:
    op, args = _get_op_args(client, operation)

    if args:
        result = op(**args)
    else:
        result = op()

    return _process_result(result, operation, op_idx)


async def async_process_operation(
    client: AsyncApiClient, operation: TestOperation, op_idx: int
) -> Tuple[bool, Any]:
    op, args = _get_op_args(client, operation)

    if args:
        result = await op(**args)
    else:
        result = await op()

    return _process_result(result, operation, op_idx)

# Copyright AGNTCY Contributors (https://github.com/agntcy)
# SPDX-License-Identifier: Apache-2.0
import builtins
import importlib
import inspect
import logging
from datetime import datetime
from typing import Any, AsyncIterator, Dict, Iterator, Tuple, Union

from agntcy_acp import ACPClient, AsyncACPClient
from deepdiff import diff
from pydantic import BaseModel

from .types import TestOperation

logger = logging.getLogger(__name__)


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
    client: Union[ACPClient, AsyncACPClient],
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


def _check_output_at_least(
    result_dump: Dict[str, Any],
    output_at_least: Dict[str, Any],
    op_id: str,
    op_idx: int,
) -> bool:
    mapdiff = diff.DeepDiff(
        output_at_least,
        result_dump,
        threshold_to_diff_deeper=0,
        use_enum_value=True,
    )
    if "values_changed" in mapdiff or "dictionary_item_removed" in mapdiff:
        print(f"operation {op_idx}: {op_id}:\n{mapdiff.to_json(indent=2)}")
        return False
    else:
        return True


def _check_output_exact(
    result: Any, output_exact: Dict[str, Any], op_id: str, op_idx: int
) -> bool:
    result_dump = result.model_dump()
    mapdiff = diff.DeepDiff(
        output_exact,
        result_dump,
        threshold_to_diff_deeper=0,
        use_enum_value=True,
        exclude_types=[datetime],
    )
    if mapdiff:
        print(f"operation {op_idx}: {op_id}:\n{mapdiff.to_json(indent=2)}")
        return False
    else:
        return True


def _process_result(
    result: Any, operation: TestOperation, op_idx: int
) -> Tuple[bool, Any]:
    if isinstance(result, BaseModel):
        result_dump = result.model_dump(exclude_none=True)
    else:
        result_dump = {}

    ret_val = True
    op_id = operation.operation_id

    # Check for no modified values
    if operation.output_stream:
        op = operation.output_stream.pop(0)
        if "output_exact" in op:
            ret_val = (
                _check_output_exact(result, op["output_exact"], op_id, op_idx)
                and ret_val
            )
        elif "output_at_least" in op:
            ret_val = (
                _check_output_at_least(
                    result_dump, op["output_at_least"], op_id, op_idx
                )
                and ret_val
            )
    else:
        if operation.output_exact:
            ret_val = (
                _check_output_exact(result, operation.output_exact, op_id, op_idx)
                and ret_val
            )
        elif operation.output_at_least:
            ret_val = (
                _check_output_at_least(
                    result_dump, operation.output_at_least, op_id, op_idx
                )
                and ret_val
            )

    return ret_val, result_dump


def process_operation(
    client: ACPClient, operation: TestOperation, op_idx: int
) -> Iterator[Tuple[bool, Any]]:
    op, args = _get_op_args(client, operation)
    result = op(**args)

    try:
        if inspect.isgenerator(result):
            for res in result:
                yield _process_result(res, operation, op_idx)
        else:
            yield _process_result(result, operation, op_idx)
    except Exception as exc:
        logger.exception(exc)
        yield _process_result(None, operation, op_idx)


async def async_process_operation(
    client: AsyncACPClient, operation: TestOperation, op_idx: int
) -> AsyncIterator[Tuple[bool, Any]]:
    op, args = _get_op_args(client, operation)
    async_obj = op(**args)

    try:
        if inspect.isawaitable(async_obj):
            result = await async_obj
            logger.debug(f"awaitable result: {result}")
            yield _process_result(result, operation, op_idx)
        elif inspect.isasyncgen(async_obj):
            async for res in async_obj:
                logger.debug(f"asyncgen result: {res}")
                yield _process_result(res, operation, op_idx)
        else:
            raise Exception("unknown async object type")
    except Exception as exc:
        logger.exception(exc)
        yield _process_result(None, operation, op_idx)

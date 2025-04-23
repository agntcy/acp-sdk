# Copyright AGNTCY Contributors (https://github.com/agntcy)
# SPDX-License-Identifier: Apache-2.0
#
# Based on https://github.com/ReMi-HSBI/ssec with MIT-License. That code
# requires python-2.13, which we do not want to support.

import codecs
import logging

from typing import Iterator, AsyncIterator, List, Tuple, Optional
from pydantic import BaseModel

__decoder = codecs.getincrementaldecoder("utf-8")()
logger = logging.getLogger(__name__)

class SSEvent(BaseModel):
    event_type: str
    event_data: str
    last_event_id: str

def _prepend_prev_chunks(prev_chunks: List[str], good_line: str) -> str:
    if len(prev_chunks) == 0:
        return good_line
    else:
        # Prepend previous incomplete lines
        prev_chunks.append(good_line)
        return ''.join(prev_chunks)


def _decode_chunk_into_lines(chunk: bytes, prev_chunks: List[str], found_lines: List[str]) -> Tuple[List[str],List[str]]:
    logger.debug(f"chunk:\n{chunk}")
    decoded_chunk = __decoder.decode(chunk)
    logger.debug(f"decoded_chunk:\n{decoded_chunk}")
    chunk_lines = decoded_chunk.splitlines(keepends=True)
    logger.debug(f"decoded chunk lines: {chunk_lines}")

    if len(chunk_lines) > 1:
        # Append found lines
        first_line = _prepend_prev_chunks(prev_chunks, chunk_lines[0])
        prev_chunks = []
        found_lines.append(first_line)
        found_lines += chunk_lines[1:-1]
            
    # Check if last line is complete
    last_line = chunk_lines[-1]
    if last_line.endswith(("\n", "\r", "\r\n")):
        last_line = _prepend_prev_chunks(prev_chunks, last_line)
        prev_chunks = []
        found_lines.append(last_line)
    else:
        prev_chunks.append(last_line)
    
    logger.debug(f"prev chunks: {prev_chunks}\nfound_lines: {found_lines}")
    return prev_chunks, found_lines

def _parse_event_lines(lines: List[str]) -> Iterator[SSEvent]:
    event_type = ""
    event_data = ""
    last_event_id = ""

    for line in lines:
        line = line.rstrip("\r\n")

        if not line:
            yield SSEvent(
                event_type=event_type or "agent_event",
                event_data=event_data.rstrip("\n"),
                last_event_id=last_event_id,
            )

            event_type = ""
            event_data = ""
            last_event_id = ""
        
        if line.startswith(":"):
            continue

        key, _, value = line.partition(":")
        value = value.lstrip()

        if key == "event":
            event_type = value
        elif key == "data":
            event_data = value
        elif key == "id":
            if "\u0000" not in value:
                last_event_id = value            

def sse_stream(stream: Iterator[bytes]) -> Iterator[SSEvent]:
    found_lines = []
    prev_chunks = []
    for chunk in stream:
        prev_chunks, found_lines = _decode_chunk_into_lines(chunk, prev_chunks, found_lines)
        yield from _parse_event_lines(found_lines)

async def sse_astream(stream: AsyncIterator[bytes]) -> AsyncIterator[SSEvent]:
    found_lines = []
    prev_chunks = []
    async for chunk in stream:
        prev_chunks, found_lines = _decode_chunk_into_lines(chunk, prev_chunks, found_lines)
        for event in _parse_event_lines(found_lines):
            yield event
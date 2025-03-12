import state
from langchain_core.messages import BaseMessage, HumanMessage, AIMessage
import mailcomposer
from typing import Any
from pydantic import BaseModel


class IoMapper1:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    def __call__(self, s: Any) -> Any:
        s.acp__ = {}
        s.acp__['mailcomposer']={'input': mailcomposer.Input(messages=[HumanMessage(content=s.description)], is_completed=False)}
        return s

class IoMapper2:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    def __call__(self, s: Any) -> Any:
        s.operation_logs = [s.acp['mc1']['output'].final_email]
        return s

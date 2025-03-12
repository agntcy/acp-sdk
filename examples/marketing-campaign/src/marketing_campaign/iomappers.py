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
        s.acp__['mailcomposer']={'input': mailcomposer.Input(messages=s.messages, is_completed=(s.has_composer_completed==True))}

        return s

class IoMapper2:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    def __call__(self, s: Any) -> Any:
        if s.acp__['mailcomposer']['output'].final_email:
            s.operation_logs = [s.acp__['mailcomposer']['output'].final_email]
        s.messages = s.acp__['mailcomposer']['output'].messages
        return s

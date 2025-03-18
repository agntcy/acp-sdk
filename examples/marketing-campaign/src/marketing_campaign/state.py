import acp_sdk.langgraph.acp_node
from pydantic import BaseModel, Field
from typing import List, Dict, Optional
from langchain_core.messages import  AIMessage, HumanMessage
import mailcomposer
import sendgrid

class InputState(BaseModel):
    messages: List[mailcomposer.Message]  = Field([], description="Chat messages")

class OutputState(InputState):
    operation_logs:List[str] = Field([], description="An array containing all the operations performed and their result. Each operation is appended to this array with a timestamp.", examples=[["Mar 15 18:10:39 Operation performed: email sent Result: OK","Mar 19 18:13:39 Operation X failed"]])

class ConfigModel(BaseModel):
    recipient_email_address: Optional[str] = Field(None, description="Email address of the email recipient")
    sender_email_address: Optional[str] = Field(None, description="Email address of the email sender")

class MailComposerState(BaseModel):
    input: Optional[mailcomposer.InputSchema] = None
    output: Optional[mailcomposer.OutputSchema] = None

class SendGridState(BaseModel):
    input: Optional[sendgrid.InputSchema] = None
    output: Optional[sendgrid.OutputSchema]= None

class OverallState(OutputState):
    has_composer_completed: Optional[bool] = Field(None, description="Flag indicating if the mail composer has succesfully completed its task")
    has_reviewer_completed: Optional[bool] = None
    has_sender_completed: Optional[bool] = None
    recipient_email_address: Optional[str] = Field(None, description="Email address of the email recipient")
    sender_email_address: Optional[str] = Field(None, description="Email address of the email sender")
    mailcomposer_state: Optional[MailComposerState] = None
    sendgrid_state: Optional[SendGridState] = None




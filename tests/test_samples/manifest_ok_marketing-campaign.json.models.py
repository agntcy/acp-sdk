# Generated from ACP Descriptor org.agntcy.marketing-campaign using datamodel_code_generator.

from __future__ import annotations

from enum import Enum
from typing import List, Optional

from pydantic import BaseModel, Field


class APIBridgeInput(BaseModel):
    query: str = Field(
        ...,
        description="Query for the API bridge agent in natural language",
        title="Query",
    )


class APIBridgeOutput(BaseModel):
    result: str = Field(
        ..., description="API response from API bridge agent", title="Result"
    )


class ConfigSchema(BaseModel):
    recipient_email_address: str = Field(
        ...,
        description="Email address of the email recipient",
        title="Recipient Email Address",
    )
    sender_email_address: str = Field(
        ...,
        description="Email address of the email sender",
        title="Sender Email Address",
    )
    target_audience: TargetAudience = Field(
        ..., description="Target audience for the marketing campaign"
    )


class InputSchema(BaseModel):
    messages: Optional[List[Message]] = Field(
        [], description="Chat messages", title="Messages"
    )
    operation_logs: Optional[List[str]] = Field(
        [],
        description="An array containing all the operations performed and their result. Each operation is appended to this array with a timestamp.",
        examples=[
            [
                "Mar 15 18:10:39 Operation performed: email sent Result: OK",
                "Mar 19 18:13:39 Operation X failed",
            ]
        ],
        title="Operation Logs",
    )
    has_composer_completed: Optional[bool] = Field(
        None,
        description="Flag indicating if the mail composer has succesfully completed its task",
        title="Has Composer Completed",
    )
    has_reviewer_completed: Optional[bool] = Field(None, title="Has Reviewer Completed")
    has_sender_completed: Optional[bool] = Field(None, title="Has Sender Completed")
    mailcomposer_state: Optional[MailComposerState] = None
    email_reviewer_state: Optional[MailReviewerState] = None
    target_audience: Optional[TargetAudience] = None
    sendgrid_state: Optional[SendGridState] = None
    recipient_email_address: Optional[str] = Field(
        None,
        description="Email address of the email recipient",
        title="Recipient Email Address",
    )
    sender_email_address: Optional[str] = Field(
        None,
        description="Email address of the email sender",
        title="Sender Email Address",
    )


class MailComposerState(BaseModel):
    input: Optional[MarketingCampaignMailcomposerInputSchema] = None
    output: Optional[MarketingCampaignMailcomposerOutputSchema] = None


class MailReviewerState(BaseModel):
    input: Optional[MarketingCampaignEmailReviewerInputSchema] = None
    output: Optional[MarketingCampaignEmailReviewerOutputSchema] = None


class MarketingCampaignEmailReviewerInputSchema(BaseModel):
    email: str = Field(
        ..., description="The email content to be reviewed and corrected", title="Email"
    )
    target_audience: TargetAudience = Field(
        ...,
        description="The target audience for the email, affecting the style of review",
    )


class MarketingCampaignEmailReviewerOutputSchema(BaseModel):
    correct: bool = Field(
        ...,
        description="Indicates whether the email is correct and requires no changes",
        title="Correct",
    )
    corrected_email: Optional[str] = Field(
        None,
        description="The corrected version of the email, if changes were necessary",
        title="Corrected Email",
    )


class MarketingCampaignMailcomposerInputSchema(BaseModel):
    messages: Optional[List[Message]] = Field(None, title="Messages")
    is_completed: Optional[bool] = Field(None, title="Is Completed")


class MarketingCampaignMailcomposerOutputSchema(BaseModel):
    messages: Optional[List[Message]] = Field(None, title="Messages")
    is_completed: Optional[bool] = Field(None, title="Is Completed")
    final_email: Optional[str] = Field(
        None,
        description="Final email produced by the mail composer",
        title="Final Email",
    )


class Message(BaseModel):
    type: Type = Field(
        ...,
        description="indicates the originator of the message, a human or an assistant",
    )
    content: str = Field(..., description="the content of the message", title="Content")


class OutputSchema(BaseModel):
    messages: Optional[List[Message]] = Field(
        [], description="Chat messages", title="Messages"
    )
    operation_logs: Optional[List[str]] = Field(
        [],
        description="An array containing all the operations performed and their result. Each operation is appended to this array with a timestamp.",
        examples=[
            [
                "Mar 15 18:10:39 Operation performed: email sent Result: OK",
                "Mar 19 18:13:39 Operation X failed",
            ]
        ],
        title="Operation Logs",
    )
    has_composer_completed: Optional[bool] = Field(
        None,
        description="Flag indicating if the mail composer has succesfully completed its task",
        title="Has Composer Completed",
    )
    has_reviewer_completed: Optional[bool] = Field(None, title="Has Reviewer Completed")
    has_sender_completed: Optional[bool] = Field(None, title="Has Sender Completed")
    mailcomposer_state: Optional[MailComposerState] = None
    email_reviewer_state: Optional[MailReviewerState] = None
    target_audience: Optional[TargetAudience] = None
    sendgrid_state: Optional[SendGridState] = None
    recipient_email_address: Optional[str] = Field(
        None,
        description="Email address of the email recipient",
        title="Recipient Email Address",
    )
    sender_email_address: Optional[str] = Field(
        None,
        description="Email address of the email sender",
        title="Sender Email Address",
    )


class SendGridState(BaseModel):
    input: Optional[APIBridgeInput] = None
    output: Optional[APIBridgeOutput] = None


class TargetAudience(Enum):
    general = "general"
    technical = "technical"
    business = "business"
    academic = "academic"


class Type(Enum):
    human = "human"
    assistant = "assistant"
    ai = "ai"

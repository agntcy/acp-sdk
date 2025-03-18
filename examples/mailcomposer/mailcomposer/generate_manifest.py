from state import AgentState, OutputState
from acp_sdk.models import *
from pydantic import TypeAdapter

descriptor = AgentACPDescriptor(
    metadata=AgentMetadata(
        ref=AgentRef(name="org.agntcy.mailcomposer", version="0.0.1"),
        description="Offer a chat interface to compose an email for a marketing campaign. Final output is the email that could be used for the campaign"),
    specs=AgentACPSpec(
        input=TypeAdapter(AgentState).json_schema(),
        output=TypeAdapter(OutputState).json_schema(),
        config=TypeAdapter(OutputState).json_schema(),
        capabilities=AgentCapabilities(
            threads=False,
            callbacks=False,
            interrupts=False
        )
    )
)

with open("___manifest.json", "w") as f:
    f.write(descriptor.model_dump_json(
        exclude_unset=True,
        exclude_none=True,
        indent=2
    ))
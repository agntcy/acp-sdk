from src.marketing_campaign.state import OverallState, ConfigModel
from acp_sdk.models import *

descriptor = AgentACPDescriptor(
    metadata=AgentMetadata(
        ref=AgentRef(name="org.agntcy.marketing-campaign", version="0.0.1"),
        description="Offer a chat interface to compose an email for a marketing campaign. Final output is the email that could be used for the campaign"),
    specs=AgentACPSpec(
        input=OverallState.model_json_schema(),
        output=OverallState.model_json_schema(),
        config=ConfigModel.model_json_schema(),
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
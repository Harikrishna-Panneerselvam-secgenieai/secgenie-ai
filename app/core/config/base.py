from pydantic import BaseModel, ConfigDict


class BaseConfigModel(BaseModel):
    """Base class for all configuration models."""

    model_config = ConfigDict(
        frozen=True,
        validate_assignment=True,
        extra="ignore",
    )
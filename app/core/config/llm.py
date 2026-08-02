from .base import BaseConfigModel


class LLMSettings(BaseConfigModel):
    """LLM provider configuration."""

    provider: str = "openai"

    model: str = "gpt-5.5"

    api_key: str = ""

    base_url: str = ""

    temperature: float = 0.0

    max_tokens: int = 4096

    timeout: int = 60

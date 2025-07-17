from pydantic import BaseModel


class SummarizationConfig(BaseModel):
    model: str = "openai/gpt-4o"
    temperature: float = 0.0
    max_tokens: int = 1024

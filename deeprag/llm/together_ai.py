from typing import Dict, List
from deeprag.llm.base import BaseLLM, ChatResponse


class TogetherAI(BaseLLM):
    def __init__(self, model: str = "deepseek-ai/DeepSeek-V3"):
        from together import Together
        self.model = model
        self.client = Together()

    def chat(self, messages: List[Dict]) -> ChatResponse:
        response = self.client.chat.completions.create(
            model=self.model,
            messages=messages,
        )
        return ChatResponse(content=response.choices[0].message.content, total_tokens=response.usage.total_tokens)


if __name__ == "__main__":
    llm = TogetherAI()
    print(llm.chat(messages=[{"role": "user", "content": "Hello, how are you?"}]))
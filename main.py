import os
from typing import List, Dict
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()


class HelloAgentsLLM:
    def __init__(
        self,
        model=None,
        api_key=None,
        base_url=None,
    ):
        self.model = model or os.getenv("LLM_MODEL_ID")
        self.api_key = api_key or os.getenv("LLM_API_KEY")
        self.base_url = base_url or os.getenv("LLM_API_URL")

        if not all([self.model, self.api_key, self.base_url]):
            raise ValueError("模型名称、URL 和 Key 必须填写")

        # 只在创建实例时初始化客户端
        self.client = OpenAI(
            api_key=self.api_key,
            base_url=self.base_url,
        )

    def think(self, messages: List[Dict[str, str]], temperature: float = 0) -> str:
        """调用大语言模型进行思考"""
        print(f"🧠 正在调用 {self.model} 模型...")

        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                temperature=temperature,
                stream=True,
            )

            collected_content = []
            for chunk in response:
                if not chunk.choices:
                    continue
                content = chunk.choices[0].delta.content or ""
                print(content, end="", flush=True)
                collected_content.append(content)
            print()

            return "".join(collected_content)

        except Exception as e:
            print(f"❌ 调用 LLM API 时发生错误: {e}")
            return ""


if __name__ == "__main__":
    try:
        llm_client = HelloAgentsLLM()

        example_messages = [
            {"role": "system", "content": "你是一个有帮助的助手"},
            {"role": "user", "content": "写一个冒泡排序算法"},
        ]

        print("--- 调用 LLM ---")
        response_text = llm_client.think(example_messages)

        if response_text:
            print("\n\n--- 完整模型响应 ---")
            print(response_text)

    except ValueError as e:
        print(e)

from openai import OpenAI
from dotenv import load_dotenv
from pathlib import Path
import os

# .env から環境変数を読む
load_dotenv()

class OpenAIAdapter:
    def __init__(self):
        api_key = os.environ.get("OPENAI_API_KEY")
        if not api_key:
            raise RuntimeError("OPENAI_API_KEY が未設定です")
        self.client = OpenAI(api_key=api_key)

        # system_promptはsystem_prompt.txtから読み込む
        prompt_path = Path(__file__).parent / "system_prompt.txt"
        self.system_prompt = prompt_path.read_text(encoding="utf-8")

    def _create_message(self, role: str, message: str) -> dict:
        return {"role": role, "content": message}

    def create_chat(self, question: str) -> str:
        messages = [
            self._create_message("system", self.system_prompt),
            self._create_message("user", question),
        ]
        model = os.environ.get("OPENAI_MODEL", "gpt-4o-mini")
        res = self.client.chat.completions.create(
            model=model,
            messages=messages,
        )
        return res.choices[0].message.content

if __name__ == "__main__":
    adapter = OpenAIAdapter()
    print(adapter.create_chat("こんにちは"))

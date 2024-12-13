from .base import BaseProvider
from openai import OpenAI

class ChatGPTProvider(BaseProvider):
    def get_response(self, question):
        client = OpenAI(api_key=self.api_key)
        
        response = client.chat.completions.create(
            messages=[{"role": "user", "content": question}],
            model=self.config.get('model', 'gpt-4-0125-preview'),
            max_tokens=self.config.get('max_tokens', 1024)
        )
        
        return response.choices[0].message.content
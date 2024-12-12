from .base import BaseProvider
import requests

class ChatGPTProvider(BaseProvider):
    def get_response(self, question):
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f"Bearer {self.api_key}"
        }
        
        data = {
            "messages": [{"role": "user", "content": question}],
            "model": self.config.get('model', 'gpt-4-turbo-preview'),
            "max_tokens": self.config.get('max_tokens', 1024)
        }
        
        response = requests.post(
            self.config.get('api_url', 'https://api.openai.com/v1/chat/completions'),
            headers=headers,
            json=data
        )
        response.raise_for_status()
        return response.json()['choices'][0]['message']['content']
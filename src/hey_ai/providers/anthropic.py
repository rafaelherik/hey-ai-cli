from .base import BaseProvider
import requests

class ClaudeProvider(BaseProvider):
    def get_response(self, question):
        headers = {
            'Content-Type': 'application/json',
            'x-api-key': self.api_key,
            'anthropic-version': '2023-06-01'
        }
        
        data = {
            "messages": [{"role": "user", "content": question}],
            "model": self.config.get('model', 'claude-3-opus-20240229'),
            "max_tokens": self.config.get('max_tokens', 1024)
        }
        
        response = requests.post(
            self.config.get('api_url', 'https://api.anthropic.com/v1/messages'),
            headers=headers,
            json=data
        )
        response.raise_for_status()
        return response.json()['content'][0]['text']
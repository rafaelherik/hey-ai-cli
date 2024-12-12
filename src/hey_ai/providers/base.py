class BaseProvider:
    def __init__(self, config):
        self.config = config
        self.api_key = config.get('api_key')
        if not self.api_key:
            raise ValueError(f"API key not found for {self.__class__.__name__}")

    def get_response(self, question):
        raise NotImplementedError("Providers must implement get_response method")
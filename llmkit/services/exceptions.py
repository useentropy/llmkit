class LLMResponseException(Exception):
    """
    Exception for LLM Requests
    """

    def __init__(self, code, message):
        self.code = code
        self.message = message
        super().__init__(f"LLM Response Exception (Code {code}): {message}")

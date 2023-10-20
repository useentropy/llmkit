import os

from dotenv import load_dotenv

load_dotenv()


class Config:
    def __init__(self) -> None:
        self._assert_env()

    def _assert_env(self) -> None:
        llm_api_keys = ["OPENAI_API_KEY", "CF_API_KEY"]
        # Check if any of the API key is added to the .env
        assert any(
            api_key in os.environ for api_key in llm_api_keys
        ), "Missing API key(s) in environment variables."

    @property
    def openai_api_key(self) -> str:
        return os.getenv("OPENAI_API_KEY", "")

    @property
    def cloudflare_api_key(self) -> str:
        return os.getenv("CF_API_KEY", "")

    @property
    def cloudflare_api_base_url(self) -> str:
        account_id = os.getenv("CF_ACCOUNT_ID", "")
        return f"https://api.cloudflare.com/client/v4/accounts/{account_id}/ai/run/"

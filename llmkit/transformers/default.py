from llmkit.models import Message, RoleEnum
from llmkit.transformers.base import GeneratedTextTransformer, PromptTransformer


from typing import List


class DefaultPromptTransformer(PromptTransformer[str]):
    """
    Default Prompt Transformer returns prompt as it were
    """

    def format(self, input_data: str) -> List[Message]:
        return [{"role": RoleEnum.user, "content": input_data}]


class DefaultGeneratedTextTransformer(GeneratedTextTransformer[str]):
    """
    Default Response Transformer returns generated text as it comes from the LLM
    """

    def transform(self, generated_text: str) -> str:
        """
        Default Response returns the generated text as it comes from the LLM
        """
        return generated_text
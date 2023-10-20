import re
from typing import List

from llmkit.models import Message, RoleEnum
from llmkit.transformers.base import GeneratedTextTransformer, PromptTransformer


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


class EnumeratedListTransformer(GeneratedTextTransformer[List[str]]):
    """
    Class Transform generated text to list of industry string
    """

    def transform(self, generated_text: str) -> List[str]:
        """This method transform the generated text on each line to an array of string"""
        industries = generated_text.splitlines()

        # Remove empty lines and numbering
        industries = [
            self._extract_text_from_numbered_list(line)
            for line in industries
            if line.strip() != ""
        ]
        return industries

    def _extract_text_from_numbered_list(self, input_string: str):
        """
        This method remove numbering from LLM list output
        which may contain a number e.g "1. Computer Science"
        and return "Computer Science instead
        """
        # Define a regular expression pattern to match a number (optional) and text.
        pattern = r"^\s*(\d+\.)?\s*(.*)$"

        # Use the re.match() function to search for the pattern in the input string.
        match = re.match(pattern, input_string)

        return match.group(2) if match else input_string

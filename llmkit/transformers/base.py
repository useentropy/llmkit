from abc import ABC, abstractmethod
from typing import Generic, List

from llmkit.models import Message, TModelOutput, TPromptInput


class PromptTransformer(Generic[TPromptInput], ABC):
    """
    Base Class for every prompt formatter to transform your data into a prompt string
    """

    @abstractmethod
    def format(self, input_data: TPromptInput) -> List[Message]:
        """Format is implemented in concrete class"""


class GeneratedTextTransformer(Generic[TModelOutput], ABC):
    """
    Base class for for transforming generated text to data format
    """

    @abstractmethod
    def transform(self, generated_text: str) -> TModelOutput:
        """Transform is implemented in concrete class"""



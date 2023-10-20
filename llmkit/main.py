from llmkit.models import TModelOutput, TPromptInput
from llmkit.services import InferenceService, PickModelProvider
from llmkit.transformers import (
    DefaultGeneratedTextTransformer,
    DefaultPromptTransformer,
    GeneratedTextTransformer,
    PromptTransformer,
)


class LLMKit:
    """
    LLMKit class for generating data from LLM using custom transformer
    to transform your output to desired data structure
    """

    def generate_data(
        self,
        input_data: TPromptInput,
        prompt_transformer: PromptTransformer[
            TPromptInput
        ] = DefaultPromptTransformer(),
        response_transformer: GeneratedTextTransformer[
            TModelOutput
        ] = DefaultGeneratedTextTransformer(),
        llm_model_provider_name: str = "cloudflare",
    ):
        """
        Generate Data From LLM.

        Parameters:
        - input_data (TPromptInput): Input data to be transformed into an LLM text prompt.
        - prompt_transformer (PromptTransformer[TPromptInput], optional): A transformer for formatting the input data into a prompt. Default is DefaultPromptTransformer.
        - response_transformer (GeneratedTextTransformer[TModelOutput], optional): A transformer for processing the LLM-generated text into the expected data format. Default is DefaultGeneratedTextTransformer.
        - llm_model_provider_name (str, optional): Name of the LLM model provider. Default is "cloudflare".

        Returns:
        TModelOutput: The generated data.

        Raises:
        AttributeError: If the specified model provider doesn't exist.
        """
        # Picks a model using the right model keyword
        model = PickModelProvider(llm_model_provider_name).get_model_provider()

        # If the wrong model is used, an exception is raised
        if model is None:
            raise AttributeError("Model Id doesn't exist")

        # Create an instance of our inference service
        inference = InferenceService[TPromptInput, TModelOutput](
            model=model,
            prompt_formatter=prompt_transformer,
            response_transformer=response_transformer,
        )

        # Generate the text and transform it into the expected data format
        output = inference.generate_data(input_data=input_data)
        return output

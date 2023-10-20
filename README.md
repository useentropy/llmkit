# LLMKit - Language Model Kit

LLMKit is a Python package that simplifies the interaction with Language Models (LLMs) and allows you to generate text data with ease.

## Features

- **Simple Interface**: LLMKit provides a straightforward interface to interact with various language models.

- **Custom Transformers**: You can create custom transformers to format input data into prompts and transform LLM-generated text into the desired data format.

- **Model Abstraction**: LLMKit abstracts the details of model selection and provider handling.

## Installation

You can install LLMKit using pip:

```bash
pip install llm-stack-kit
```

## Usage

```python
from llmkit import LLMKit

llm_kit = LLMKit()

input_data = "Translate the following English text to French: 'Hello, World!'"

# Generate text using the default transformers
generated_text = llm_kit.generate_data(input_data)

print("Generated Text:", generated_text)
```

## Configuration

For more advanced usage and customization, you can create your own transformers and specify model providers. Only two model providers are supported for now: "openai" and "cloudflare". You need to provide a .env file with either `OPENAI_API_KEY` for OpenAI or `CF_API_KEY` and `CF_ACCOUNT_ID` for Cloudflare.

See [sample custom transformer](llmkit/tree/main/examples/transformers.py) for how to write a custom transformer.

## Documentation

Comprehensive documentation will be made available soon.

## Contributing

We welcome contributions! Our contributions guideline will be added soon.

## License

LLMKit is distributed under the MIT License. See [LICENCE](llmkit/tree/main/Licence.md) for details.

## Contact

If you have any questions or suggestions, feel free to reach out to us at <a href="mailto:useentropyai@gmail.com" target="_new">useentropy@gmail.com</a>.

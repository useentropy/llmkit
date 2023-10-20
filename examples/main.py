from examples.models import CareerAdvisor
from examples.transfomers import (
    GeneratedIndustryTransformer,
    IndustryPromptTransformer,
)
from llmkit import LLMKit

if __name__ == "__main__":
    career = CareerAdvisor(
        career_interest="Fashion", course_of_study="Computer Science", limit=3
    )

    app = LLMKit()

    generated_data = app.generate_data(
        input_data=career,
        prompt_transformer=IndustryPromptTransformer(),
        response_transformer=GeneratedIndustryTransformer(),
    )
    print(generated_data)

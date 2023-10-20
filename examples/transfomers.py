from typing import List

from examples.models import CareerAdvisor
from llmkit.models import Message, RoleEnum
from llmkit.transformers import PromptTransformer

class IndustryPromptTransformer(PromptTransformer[CareerAdvisor]):
    """
    Class to transform Careeer Interest and Course of Study to Prompt
    """

    def format(self, input_data: CareerAdvisor) -> List[Message]:
        """
        Format Industry Prompt
        """
        system_prompt = (
            "You are Nigerian based Student Career Advisor that student ask"
            " advice on their career interest and roadmap"
        )

        # Use a different prompt if career interest is specified
        if input_data.career_interest:
            user_prompt = f"""I am a {input_data.course_of_study} major and I have career interest in {input_data.career_interest}.
            List {input_data.limit} industries in Nigeria that can offer me potential job opportunities, mention only industry name, don't add description and don't number your list
            Format: Return your answer in a list separated over multi-line
            Example:
            Banking
            Telecom
            Fashion
            """
            assistant_prompt = (
                f"Sure, here are {input_data.limit} industries in Nigeria that"
                " can offer potential job opportunities for a"
                f" {input_data.course_of_study} major interested in"
                f" {input_data.career_interest}:"
            )

        # Use a different prompt if career interest is not specified
        else:
            user_prompt = f"""I am a {input_data.course_of_study} major and I have no career interest yet.
            Task: List {input_data.limit} industries in Nigeria that can offer me potential job opportunities, mention only industry name, don't add description and don't number your list
            Format: Return your answer in a list separated over multi-line
            Example:
            Banking
            Telecom
            Fashion
            """
            assistant_prompt = (
                f"Sure, here are {input_data.limit} industries in Nigeria that"
                " can offer potential job opportunities for a"
                f" {input_data.course_of_study} major:"
            )

        # organize prompt into a List serially, - system, user and assistant
        messages = [
            Message(role=RoleEnum.system, content=system_prompt).model_dump(),
            Message(role=RoleEnum.user, content=user_prompt).model_dump(),
            Message(
                role=RoleEnum.assistant, content=assistant_prompt
            ).model_dump(),
        ]

        return messages


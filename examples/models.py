from typing import Optional

from pydantic import BaseModel


class CareerAdvisor(BaseModel):
    course_of_study: str
    career_interest: Optional[str] = ""
    limit: int = 3

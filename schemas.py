from pydantic import BaseModel
from typing import List

class SewingStep(BaseModel):
    step_number: int
    instruction: str
    diagram_prompt: str

class SewingProject(BaseModel):
    title: str
    overview: str
    materials: List[str]
    fabric: str
    needle: str
    tension: str
    pattern_pieces: List[str]
    steps: List[SewingStep]

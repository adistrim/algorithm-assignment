from pydantic import BaseModel
from typing import List

class User(BaseModel):
    id: str
    name: str
    age: int
    gender: str
    interested_in: str
    location: str
    hobbies: List[str]
    interests: List[str]
    occupation: str
    education_level: str
    personality_traits: List[str]

class MatchResult(BaseModel):
    user_id: str
    name: str
    compatibility_score: float
    common_interests: List[str]
    common_hobbies: List[str]
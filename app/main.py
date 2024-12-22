from fastapi import FastAPI, HTTPException
from typing import List, Dict
import json
from .models import User, MatchResult
from .matching.algorithm import calculate_matches, get_compatibility_score

app = FastAPI(title="Dating App Matchmaking API")

with open("mock_data/users.json", "r") as f:
    USER_DATA = json.load(f)["users"]

@app.get("/")
async def read_root():
    return {"message": "Welcome to the Dating App Matchmaking API"}

@app.post("/api/v1/match/{user_id}")
async def generate_matches(user_id: str) -> List[MatchResult]:
    """
    Generate matches for a given user.
    Returns a list of potential matches sorted by compatibility score.
    """

    user = next((u for u in USER_DATA if u["id"] == user_id), None)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    matches = calculate_matches(user, USER_DATA)
    return matches

@app.get("/api/v1/compatibility/{user_id1}/{user_id2}")
async def get_compatibility(user_id1: str, user_id2: str) -> Dict:
    """
    Calculate compatibility score between two specific users
    """
    user1 = next((u for u in USER_DATA if u["id"] == user_id1), None)
    user2 = next((u for u in USER_DATA if u["id"] == user_id2), None)
    
    if not user1 or not user2:
        raise HTTPException(status_code=404, detail="One or both users not found")
    
    score = get_compatibility_score(user1, user2)
    
    return {
        "user1_id": user_id1,
        "user2_id": user_id2,
        "compatibility_score": score
    }
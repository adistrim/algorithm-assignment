# Dating App Matchmaking Algorithm Assignment

## Overview
In this assignment, you will implement a matchmaking algorithm for a dating application. Your task is to create a scoring system that determines compatibility between users based on their profiles, including hobbies, interests, and other relevant data.

## Requirements

### Technical Stack
- Python 3.8+
- FastAPI
- Additional libraries of your choice (please document them)

### Project Structure
```
matchmaking/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── models.py
│   └── matching/
│       ├── __init__.py
│       └── algorithm.py
│
├── mock_data/
│   └── users.json
│
├── requirements.txt
└── README.md
```

### Data Model
Each user profile contains the following information:
```python
{
    "id": str,
    "name": str,
    "age": int,
    "gender": str,
    "interested_in": str,
    "location": str,
    "hobbies": List[str],
    "interests": List[str],
    "occupation": str,
    "education_level": str,
    "personality_traits": List[str]
}
```

### Task Description
1. Implement the matching algorithm in `app/matching/algorithm.py`
2. The algorithm should:
   - Calculate compatibility scores between users
   - Consider factors like common interests, hobbies, education level, etc.
   - Return ranked pairs of users with their compatibility scores
3. Expose the functionality through FastAPI endpoints

### API Endpoints
Implement the following endpoints:
- `POST /api/v1/match`: Generate matches for a given user
- `GET /api/v1/compatibility/{user_id1}/{user_id2}`: Get compatibility score for two users

## Submission Requirements

### Format
Submit your solution as a ZIP file containing:
1. All source code
2. Requirements file
3. Documentation (PDF format) explaining:
   - Your algorithm's approach
   - Scoring methodology
   - Trade-offs and decisions made
   - Potential improvements
   - Setup and running instructions
4. Virtual Environment should not be included in the ZIP file

### Documentation Structure
Your documentation should include:
1. **Algorithm Overview**
   - Explanation of your matching logic
   - Factors considered and their weights
   - Mathematical formulas (if any)

2. **Technical Implementation**
   - Code structure
   - Libraries used and why
   - Performance considerations

3. **Future Improvements**
   - What would you do differently with more time?
   - Scalability considerations
   - Additional features

### Evaluation Criteria
Your submission will be evaluated based on:
1. Code quality and organization
2. Algorithm effectiveness and creativity
3. Documentation clarity
4. Performance and scalability considerations
5. Error handling and edge cases

## Getting Started
1. Clone this template
2. Install dependencies: `pip install -r requirements.txt`
3. Start server: `uvicorn app.main:app --reload`

## Mock Data
Sample user data is provided in `mock_data/users.json`. Use this data to test your implementation.

## API Testing Guide in Postman

### Base URL
```
http://localhost:8000
```

### Test Cases

#### 1. Health Check
- **Request**:
  - Method: GET
  - URL: `/`
  - No headers required
- **Expected Response**:
```json
{
    "message": "Welcome to the Dating App Matchmaking API"
}
```

#### 2. Generate Matches for a User
- **Request**:
  - Method: POST
  - URL: `/api/v1/match/user1`
  - No body required
- **Expected Response**:
```json
[
    {
        "user_id": "user4",
        "name": "Emily Parker",
        "compatibility_score": 0.85,
        "common_interests": ["travel", "technology"],
        "common_hobbies": ["hiking", "photography"]
    },
    {
        "user_id": "user2",
        "name": "Sarah Chen",
        "compatibility_score": 0.72,
        "common_interests": ["travel"],
        "common_hobbies": ["cooking"]
    }
]
```

#### 3. Check Compatibility Between Two Users
- **Request**:
  - Method: GET
  - URL: `/api/v1/compatibility/user1/user2`
  - No body required
- **Expected Response**:
```json
{
    "user1_id": "user1",
    "user2_id": "user2",
    "compatibility_score": 0.72
}
```

### Test Scenarios

1. **Valid Match Generation**
   - Use existing user IDs (user1, user2, user3, user4, user5)
   - Verify that matches are sorted by compatibility score
   - Check that gender preferences are respected
   - Verify common interests and hobbies are correct

2. **Invalid User IDs**
   - Test with non-existent user ID: `/api/v1/match/user999`
   - Expected: 404 Not Found response
   ```json
   {
       "detail": "User not found"
   }
   ```

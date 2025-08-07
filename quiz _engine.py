def generate_quiz(user_id,topic):
    return {
        "user_id": user_id,
        "topic": topic,
        "questions": [
            {"q": "what is AI?","options":["math","Science","AI","Biology"], "answer": "AI"},
            {"q":"python is a?","options":["language","animal","App"], "answer":"language"}
        ]
    }
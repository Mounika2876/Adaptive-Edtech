from transformers import pipeline

sentiment_pipeline = pipeline("sentiment-analysis")

def analyze_feedback(text):
    analysis = sentiment_pipeline(text)
    return {"feedback":text, "analysis": analysis}

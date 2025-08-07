import streamlit as st
import requests

st.tittle("AI-Powered adaptive Learning")

page = st.sidebar.selection("Go to", ["dashboard", "Content", "Quiz", "Feedback"])

if page == "Dashboard":
    st.subheader("Dashboard")
    user_id = st.text_input("Enter User ID")
    if st.button("Fetch Profile"):
        res = requests.get(f"http://localhost:8000/learner/profile/{user_id}")
        st.json(res.json())

elif page == "Content":
    st.subheader("Content Recommendation")
    user_id = st.text_input("User ID for content")
    if st.button("Recommend"):
        res  = requests.get(f"http://localhost:8000/content/profile/{user_id}")
        st.json(res.json())

elif page == "Quiz":
    st.subheader("Adaptive Quiz")
    user_id = st.text_input("User ID for quiz")
    topic = st.text_input("Topic")
    if st.button("Generate Quiz"):
        res  = requests.post(f"http://localhost:8000/quiz/generate", json={"user_id": user_id, "topic": topic})
        st.json(res.json())

elif page == "Feedback":
    st.subheader("Feedback Analysis")
    user_id = st.text_input("User ID for feedback")
    text = st.text_area("Enter feedback")
    if st.button("Analyze"):
        res  = requests.post(f"http://localhost:8000/feedback/analyze", json={"user_id": user_id, "text": text})
        st.json(res.json())         

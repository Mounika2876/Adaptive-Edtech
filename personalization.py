from utils.prompt_templates import content_prompt
def recommmend_content(user_id):
    profile = {"level": "beginner", "interests": ["AI","Python"]}
    prompt = content_prompt.format(profile=profile)
    return {"user_id" : user_id,"recommended" : ["Intro to AI", "Python Basics"]}
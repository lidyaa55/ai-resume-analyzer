import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()  # Load from .env

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not OPENAI_API_KEY:
    raise ValueError("Please set your OPENAI_API_KEY environment variable")

client = OpenAI(api_key=OPENAI_API_KEY)

def get_resume_feedback(resume_text, job_description):
    prompt = f"""
    You are a career coach AI. Given this job description:
    {job_description}

    And this resume text:
    {resume_text}

    Suggest:
    1. Missing keywords or skills the resume should include.
    2. How to improve bullet points to better match the job.
    3. Any general feedback to improve resume relevance.
    """
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
        max_tokens=500,
    )
    return response.choices[0].message.content



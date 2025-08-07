from src.ai_feedback import get_resume_feedback

resume = """
Experienced software engineer with expertise in Python, data analysis, and cloud computing.
Strong team player with good communication skills.
"""

job_desc = """
Looking for a software engineer skilled in Python, machine learning, and data analysis.
Experience with cloud platforms and teamwork is a plus.
"""

feedback = get_resume_feedback(resume, job_desc)
print(feedback)

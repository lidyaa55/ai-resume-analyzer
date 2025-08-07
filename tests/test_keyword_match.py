from src.keyword_match import extract_keywords, match_score

job_desc = """
Looking for a software engineer skilled in Python, machine learning, and data analysis.
Experience with cloud platforms and teamwork is a plus.
"""

resume_text = """
Experienced software engineer with expertise in Python, data analysis, and cloud computing.
Strong team player with good communication skills.
"""

job_keywords = extract_keywords(job_desc)
score, matched_keywords = match_score(resume_text, job_keywords)

print(f"Match Score: {score:.2f}%")
print(f"Matched Keywords: {matched_keywords}")

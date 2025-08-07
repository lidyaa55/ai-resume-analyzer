from src.text_extraction import read_resume

# Change the file name below if yours is different
file_path = "data/Resume.pdf"  

resume_text = read_resume(file_path)

# Print only the first 500 characters so the output isn't too long
print(resume_text[:500])

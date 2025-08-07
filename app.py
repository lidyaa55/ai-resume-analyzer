import streamlit as st
import os
import matplotlib.pyplot as plt
from src.text_extraction import read_resume
from src.keyword_match import extract_keywords, match_score
from src.ai_feedback import get_resume_feedback

# Page settings
st.set_page_config(page_title="AI Resume Analyzer", layout="wide")

# ===== HEADER =====
st.markdown(
    """
    <div style="background-color:#2E86C1;padding:20px;border-radius:10px">
        <h1 style="color:white;text-align:center;">📄 AI Resume Analyzer</h1>
        <p style="color:white;text-align:center;">
            Upload your resume, paste a job description, and get an instant match score with AI-powered improvement tips.
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

# ===== FILE & TEXT INPUT =====
resume_file = st.file_uploader("**Upload Resume (PDF/DOCX)**", type=["pdf", "docx"])
job_desc_text = st.text_area("**Paste Job Description Here**", height=200)

# ===== RUN ANALYSIS =====
if st.button("🚀 Run Analysis"):
    if not resume_file:
        st.error("Please upload a resume.")
    elif not job_desc_text.strip():
        st.error("Please paste the job description.")
    else:
        os.makedirs("data/sample_resumes", exist_ok=True)

        ext = os.path.splitext(resume_file.name)[1]
        resume_path = f"data/sample_resumes/Resume{ext}"
        with open(resume_path, "wb") as f:
            f.write(resume_file.getbuffer())

        resume_text = read_resume(resume_path)
        job_keywords = extract_keywords(job_desc_text)
        score, matched_keywords = match_score(resume_text, job_keywords)
        missing_keywords = job_keywords - matched_keywords

        # ===== LAYOUT =====
        col1, col2 = st.columns([2, 3])

        with col1:
            # Match score badge
            st.markdown(
                f"""
                <div style="background-color:#27AE60;padding:15px;border-radius:10px;text-align:center;">
                    <h2 style="color:white;">Match Score</h2>
                    <h1 style="color:white;font-size:48px;">{score:.2f}%</h1>
                </div>
                """,
                unsafe_allow_html=True
            )

            with st.expander("✅ Matched Keywords"):
                st.write(", ".join(sorted(matched_keywords)) if matched_keywords else "None")

            with st.expander("⚠️ Missing Keywords"):
                st.write(", ".join(sorted(missing_keywords)) if missing_keywords else "None")

        with col2:
            st.subheader("📊 Match Visualization")
            sizes = [len(matched_keywords), len(missing_keywords)]
            labels = ['Matched', 'Missing']
            colors = ['#27AE60', '#E74C3C']

            fig, ax = plt.subplots()
            ax.pie(sizes, labels=labels, autopct='%1.1f%%', colors=colors, startangle=140)
            ax.axis('equal')
            st.pyplot(fig)

        # ===== AI FEEDBACK =====
        with st.expander("💡 AI Suggestions for Improvement", expanded=True):
            with st.spinner("Analyzing resume with AI..."):
                feedback = get_resume_feedback(resume_text, job_desc_text)
                st.markdown(feedback)

# ===== FOOTER =====
st.markdown(
    """
    <hr>
    <div style="text-align:center; padding-top:10px;">
        <p style="color:grey;">
            Developed by <b>Lidya-Langana</b> | © 2025 All Rights Reserved
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

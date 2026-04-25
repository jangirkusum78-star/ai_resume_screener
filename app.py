import streamlit as st
import pandas as pd
import pdfplumber
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Skill list
skills_list = [
    "python", "sql", "pandas", "machine learning",
    "data visualization", "power bi", "excel"
]

# Extract text from PDF
def extract_text_from_pdf(pdf_file):
    text = ""
    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages:
            text += page.extract_text() or ""
    return text

# Extract skills
def extract_skills(text, skills_list):
    text = text.lower()
    found_skills = []
    for skill in skills_list:
        if skill in text:
            found_skills.append(skill)
    return found_skills

# UI Title
st.title(" AI Resume Screener")

# Upload resumes
uploaded_files = st.file_uploader("Upload Resumes (PDF)", type="pdf", accept_multiple_files=True)

# Job description input
job_desc = st.text_area("Paste Job Description")

if st.button("Analyze Resumes"):

    if uploaded_files and job_desc:

        resumes = []
        resume_names = []

        for file in uploaded_files:
            text = extract_text_from_pdf(file)
            resumes.append(text)
            resume_names.append(file.name)

        # TF-IDF
        documents = [job_desc] + resumes
        vectorizer = TfidfVectorizer(stop_words='english')
        tfidf_matrix = vectorizer.fit_transform(documents)

        # Similarity
        similarity_scores = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:])
        scores = similarity_scores[0]

        # Ranking
        results = list(zip(resume_names, scores))
        results = sorted(results, key=lambda x: x[1], reverse=True)

        # Job skills
        job_skills = extract_skills(job_desc, skills_list)

        st.subheader(" Results")

        result_data = []

        for name, score in results:
            resume_index = resume_names.index(name)
            resume_text = resumes[resume_index]

            resume_skills = extract_skills(resume_text, skills_list)

            matched = list(set(job_skills) & set(resume_skills))
            missing = list(set(job_skills) - set(resume_skills))
            result_data.append({
                "Resume": name,
                "Match Score (%)": round(score * 100, 2),
                "Matched Skills": ", ".join(matched),
                "Missing Skills": ", ".join(missing)
            })

            st.write(f"### {name}")
            st.write(f"Match Score: {round(score * 100, 2)}%")
            st.write(f" Matched Skills: {matched}")
            st.write(f" Missing Skills: {missing}")
            st.write("---")

        df = pd.DataFrame(result_data)
        csv = df.to_csv(index=False).encode('utf-8')

        st.download_button(
            label=" Download Results as CSV",
            data=csv,
            file_name="resume_screening_results.csv",
            mime="text/csv",
        )
    else:
        st.warning("Please upload resumes and enter job description.")

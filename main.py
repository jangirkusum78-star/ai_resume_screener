import os
from utils import extract_text_from_pdf

resume_folder = "resumes"
resumes = []
resume_names = []

for file in os.listdir(resume_folder):
    if file.endswith(".pdf"):
        path = os.path.join(resume_folder, file)
        text = extract_text_from_pdf(path)
        resumes.append(text)
        resume_names.append(file)


# loading job description
with open("job_description.txt", "r") as f:
    job_desc = f.read()

# converting text into numbers using tfidf vectorizer
from sklearn.feature_extraction.text import TfidfVectorizer

documents = [job_desc] + resumes

vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = vectorizer.fit_transform(documents)

# calculating cosine similarity
from sklearn.metrics.pairwise import cosine_similarity
similarity_scores = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:])
scores    =similarity_scores[0]


# ranking resumes based on similarity scores
ranked_resumes = sorted(zip(resume_names, scores), key=lambda x: x[1], reverse=True)
for name, score in ranked_resumes:
    print(f"{name}: {round(score * 100, 2)}  %  match")

# creating skills list
skills_list = [
    "python", "sql", "pandas", "machine learning",
    "data visualization", "power bi", "excel"
]
# extracting skills from text
def extract_skills(text, skills_list):
    text = text.lower()
    found_skills = []

    for skill in skills_list:
        if skill in text:
            found_skills.append(skill)

    return found_skills
# extracting skills from job description
job_skills = extract_skills(job_desc, skills_list)

# extracting skills from resumes
resume_skills_list = []

for resume in resumes:
    skills = extract_skills(resume, skills_list)
    resume_skills_list.append(skills)

# calculating skill match percentage
print("\n📊 Resume Ranking with Skill Match:\n")

for i, (name, score) in enumerate(ranked_resumes):
    resume_skills = resume_skills_list[resume_names.index(name)]

    matched = list(set(job_skills) & set(resume_skills))
    missing = list(set(job_skills) - set(resume_skills))

    print(f"{name}: {round(score * 100, 2)}% match")
    print(f"    Matched Skills: {matched}")
    print(f"    Missing Skills: {missing}\n")

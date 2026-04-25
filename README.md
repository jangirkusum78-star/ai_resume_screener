# AI Resume Screener

An AI-powered Resume Screening application that analyzes and ranks resumes based on their relevance to a given job description using Natural Language Processing (NLP).

---

##  Project Overview

Recruiters often receive hundreds of resumes for a single job role. Manually screening them is time-consuming and inefficient.

This project automates the process by:

* Extracting text from resumes (PDF)
* Comparing resumes with job description
* Ranking candidates based on similarity score
* Highlighting matched and missing skills

---

##  Features

*  Upload multiple resumes (PDF)
*  Input job description
*  Rank resumes based on match score
*  Identify matched skills
*  Identify missing skills
*  Download results as CSV
*  Interactive UI using Streamlit

---

##  Tech Stack

* Python
* Scikit-learn (TF-IDF, Cosine Similarity)
* pdfplumber (PDF text extraction)
* Streamlit (UI)
* Pandas (Data handling)

---

##  How It Works

1. Extract text from resumes using pdfplumber
2. Convert text into numerical vectors using TF-IDF
3. Compute similarity using cosine similarity
4. Rank resumes based on similarity score
5. Extract and compare skills
6. Display results and allow CSV download

---

##  Output Example

* Resume Ranking with Match %
* Matched Skills
* Missing Skills
* Downloadable CSV report

---

##  How to Run

```bash
pip install -r requirements.txt
streamlit run app.py
```

---

##  Project Structure

```
resume_screener/

├── app.py
├── main.py
├── requirements.txt
└── README.md
└── utils.py
└── .gitignore

```

---
# resumes
Sample resumes are not included in this repository. 
You can use your own PDF resumes to test the application.

##  Future Improvements

* Improve skill extraction using NLP libraries
* Add keyword highlighting in resumes
* Add visual analytics (graphs)
* Support DOCX resumes


---

##  Key Learnings

* Natural Language Processing (NLP)
* Feature Engineering (TF-IDF)
* Similarity Algorithms
* Building end-to-end ML applications
* UI development with Streamlit

---
## Deployment
https://airesumescreener-kmqmywdrpydozpxxzyuvqp.streamlit.app/
##  Author

Kusum Jangir

---

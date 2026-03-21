# AI-Powered Resume Screening System 🚀

An automated candidate evaluation pipeline that ranks resumes against Job Descriptions (JD) using **LLaMA 3.3** and provides actionable insights directly to a Google Sheets dashboard.

## 📌 Overview
This project is an AI-powered Resume Screening System designed to automate candidate evaluation and shortlisting based on a given Job Description (JD).

It processes multiple resumes, evaluates them using AI, and generates structured outputs including scores, strengths, gaps, and recommendations. The final results are displayed in a recruiter-friendly Google Sheets dashboard


## 🛠️ Tech Stack
* **LLM:** Groq API (LLaMA 3.3-70b)
* **Language:** Python 3.x
* **Data:** Pandas, PyPDF2
* **Integration:** Google Sheets API (gspread)

##⚙️ How the System Works
📥 Inputs
Job Description (jd.txt)
Multiple resumes (PDF format)

⚙️ Processing
1.Extract text from resumes
2.Evaluate resumes using Groq LLaMA 3.3
3.Perform keyword matching with JD
4.Calculate:
-AI Score (0–100)
-Keyword Match %
-Final Score (weighted)
5.Rank candidates

📤 Outputs
Match Score (0–100)
Strengths (2–3 points)
Gaps (2–3 points)
Recommendation (Strong Fit / Moderate Fit / Not Fit)
Candidate Ranking

## ⚙️ Project Structure
```text
ai-resume/
├── resumes/              # Drop candidate PDF files here
├── jd.txt                # Paste the Job Description here
├── main.py               # Orchestration script
├── utils.py              # Logic for PDF parsing & AI scoring
├── requirements.txt      # List of dependencies
├── .gitignore            # Keeps your API keys safe
└── README.md

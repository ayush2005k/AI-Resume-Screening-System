# AI-Powered Resume Screening System 🚀(fixing it)

An automated candidate evaluation pipeline that ranks resumes against a Job Description (JD) using **Groq LLaMA 3.3** and provides structured insights in a **Google Sheets dashboard**.

---

## 📌 Overview

Recruiters often receive a large number of resumes and need to quickly identify the best candidates. This system automates the process by:

* Parsing multiple PDF resumes
* Evaluating candidates using AI
* Matching resumes with job requirements
* Ranking candidates based on relevance
* Displaying results in a recruiter-friendly dashboard

---

## 🎯 Key Features

* 📄 Extracts text from PDF resumes
* 🧠 AI-based evaluation (Score, Strengths, Gaps, Recommendation)
* 🔍 Keyword matching with Job Description
* 🏆 Candidate ranking using weighted scoring
* 📊 Google Sheets dashboard output
* 📈 Recruiter insights (Top candidate, Average score)

---

## ⚙️ How It Works

### 📥 Inputs

* Job Description (`jd.txt`)
* Multiple resumes (PDF format)

### ⚙️ Processing Pipeline

1. Extract text from resumes
2. Evaluate using Groq LLaMA 3.3
3. Perform keyword matching
4. Compute:

   * AI Score (0–100)
   * Keyword Match %
   * Final Score = (70% AI + 30% Keywords)
5. Rank candidates

### 📤 Outputs

* Match Score (0–100)
* Strengths (2–3 points)
* Gaps (2–3 points)
* Recommendation (Strong Fit / Moderate Fit / Not Fit)
* Final Ranking

---

## 📊 Live Dashboard (Google Sheets)

👉 https://docs.google.com/spreadsheets/d/1YVnklsSAxhKkCE6CR4Nj9UgTz1EdjfzH-JJdWsIbjtY/edit?gid=0#gid=0



---

## 🛠️ Tech Stack

* **Language:** Python
* **LLM:** Groq API (LLaMA 3.3)
* **Libraries:** pandas, PyPDF2 / pypdf
* **Integration:** Google Sheets API (gspread)

---

## 📂 Project Structure

```text
ai-resume/
├── resumes/              # Input resumes (PDF)
├── jd.txt                # Job Description
├── main.py               # Main execution script
├── utils.py              # Core logic (AI + parsing)
├── results.csv           # Local output backup
├── requirements.txt      # Dependencies
├── .gitignore            # Protects secrets
└── README.md
```

---

## ⚙️ Setup Instructions

### 🔐 1. Set Groq API Key (IMPORTANT)

To run this project, you need to set your Groq API key as an environment variable.

```
client = Groq(api_key=os.getenv("GROQ_API_KEY"))
```
replace the above code 
present in utils.py, to below code to make it working

```
client = Groq(api_key="gsk_your_actual_key_here")
```

---

### 📦 2. Install Dependencies

```
pip install -r requirements.txt
```

---

### 📄 3. Add Input Files

* Place resumes inside `resumes/`
* Add job description in `jd.txt`

---

### ▶️ 4. Run the System

```
python main.py
```

---

## 📈 Output

* 📊 Google Sheets dashboard:

  * Ranked candidates
  * Scores
  * Strengths & gaps
  * Recommendations

* 💾 Local backup:

  * `results.csv`

---

## 🧠 Approach

The system is designed as a practical AI pipeline for resume screening.

Resumes are first converted into text and evaluated using a large language model. The AI generates structured insights such as scores, strengths, gaps, and recommendations.

To improve reliability, keyword matching is performed between the job description and resume content. A weighted scoring system combines AI evaluation (70%) and keyword relevance (30%) to rank candidates.

The final output is presented in a Google Sheets dashboard to make it easy for recruiters to compare and shortlist candidates efficiently.

---

## 🔐 Security

* API keys are stored using environment variables
* Sensitive files are excluded using `.gitignore`
* No credentials are exposed in the repository

---

## 🚀 Future Improvements

* Web interface (Streamlit / React)
* Resume upload portal
* Candidate filtering system
* Email automation

---

## 👨‍💻 Author

Ayush Singh

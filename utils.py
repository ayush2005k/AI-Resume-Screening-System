from pypdf import PdfReader   # safer than PyPDF2
import json
import re
import os
from groq import Groq

# 🔐 Use environment variable (recommended)
client = Groq(api_key=os.getenv("GROQ_API_KEY"))


# 📄 Extract text from PDF
def extract_text(pdf_path):
    reader = PdfReader(pdf_path)
    text = ""

    for page in reader.pages:
        if page.extract_text():
            text += page.extract_text()

    return text


# 🧠 AI Resume Evaluation (ROBUST VERSION)
def evaluate_resume(resume_text, jd_text):
    prompt = f"""
You are an ATS system.

Return ONLY JSON. No explanation. No markdown.

{{
  "score": 0-100,
  "strengths": ["", "", ""],
  "gaps": ["", "", ""],
  "recommendation": ""
}}

Resume:
{resume_text}

Job Description:
{jd_text}
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}]
    )

    content = response.choices[0].message.content

    print("\n--- RAW AI RESPONSE ---")
    print(content)
    print("-----------------------\n")

    try:
        # 🔥 Remove ```json formatting
        content = content.strip()
        content = re.sub(r"```json|```", "", content)

        return json.loads(content)

    except Exception as e:
        print("⚠️ JSON parsing failed:", e)

        return {
            "score": 50,
            "strengths": ["Parsing issue"],
            "gaps": ["AI response format error"],
            "recommendation": "Moderate Fit"
        }


# 🔍 Keyword Matching
def keyword_score(resume_text, jd_text):
    keywords = jd_text.lower().split()
    match_count = sum(1 for word in keywords if word in resume_text.lower())

    return round((match_count / len(keywords)) * 100, 2)


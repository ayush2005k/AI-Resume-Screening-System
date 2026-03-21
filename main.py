import os
import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from utils import extract_text, evaluate_resume, keyword_score
from gspread_formatting import format_cell_range, CellFormat, TextFormat, set_column_width

# 📄 Load Job Description
with open("jd.txt", "r", encoding="utf-8") as f:
    jd_text = f.read()

results = []

# 📂 Process resumes
for file in os.listdir("resumes"):
    if file.endswith(".pdf"):
        path = f"resumes/{file}"

        print(f"Processing {file}...")

        resume_text = extract_text(path)
        ai = evaluate_resume(resume_text, jd_text)
        kw = keyword_score(resume_text, jd_text)

        results.append({
            "Name": file,
            "Score": ai["score"],
            "Keyword %": kw,
            "Strengths": "• " + "\n• ".join(ai["strengths"]),
            "Gaps": "• " + "\n• ".join(ai["gaps"]),
            "Recommendation": ai["recommendation"]
        })

# 📊 DataFrame
df = pd.DataFrame(results)

# 🏆 Ranking
df["Final Score"] = (df["Score"] * 0.7) + (df["Keyword %"] * 0.3)
df = df.sort_values(by="Final Score", ascending=False)
df["Rank"] = range(1, len(df) + 1)

# 📋 Column order
df = df[[
    "Rank",
    "Name",
    "Final Score",
    "Score",
    "Keyword %",
    "Strengths",
    "Gaps",
    "Recommendation"
]]

print("\n=== FINAL RESULTS ===\n")
print(df)

# 💾 Save CSV
df.to_csv("results.csv", index=False)

# 🔐 Google Sheets
scope = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/drive"
]

creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
client = gspread.authorize(creds)

sheet = client.open("AI Resume Screening").sheet1

# 🧹 Clear old data
sheet.clear()

# 📊 Upload
sheet.update([df.columns.values.tolist()] + df.values.tolist())

# 📏 Auto resize columns
sheet.columns_auto_resize(0, 8)

# 📦 Wrap text (important for long text)
format_cell_range(
    sheet,
    "F2:G100",
    CellFormat(wrapStrategy='WRAP')
)

# 📐 Increase column width (Strengths & Gaps)
set_column_width(sheet, 'F', 300)
set_column_width(sheet, 'G', 300)

# 🎨 Header bold
header_format = CellFormat(
    textFormat=TextFormat(bold=True)
)
format_cell_range(sheet, "A1:H1", header_format)

# ❄ Freeze header
sheet.freeze(rows=1)

# 📈 Recruiter Insights
summary = [
    ["Total Candidates", len(df)],
    ["Average Score", round(df["Score"].mean(), 2)],
    ["Top Candidate", df.iloc[0]["Name"]],
    ["Highest Score", df["Score"].max()]
]

sheet.update("J1", summary)

print("\n✅ Google Sheet updated successfully!")
from flask import Flask, render_template, request, send_file
import os
from datetime import datetime
import pdfkit

app = Flask(__name__)

GENERATED_FOLDER = "generated"
os.makedirs(GENERATED_FOLDER, exist_ok=True)

WKHTMLTOPDF_PATH = r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe"
pdf_config = pdfkit.configuration(wkhtmltopdf=WKHTMLTOPDF_PATH)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/generate_resume', methods=['POST'])
def generate_resume():
    f = request.form

    data = {
        "name": f.get("name"),
        "location": f.get("location"),
        "phone": f.get("phone"),
        "email": f.get("email"),
        "linkedin": f.get("linkedin"),
        "summary": f.get("summary"),

        "skills": [s.strip() for s in f.get("skills","").split(",") if s.strip()],
        "languages": [l.strip() for l in f.get("languages","").split(",") if l.strip()],

        "education": [e.strip() for e in f.get("education","").split(";") if e.strip()],
        "experience": [e.strip() for e in f.get("experience","").split(";") if e.strip()],
        "projects": [p.strip() for p in f.get("projects","").split(";") if p.strip()],
    }

    filename = "resume_" + datetime.now().strftime("%Y%m%d%H%M%S")
    html_path = os.path.join(GENERATED_FOLDER, filename+".html")
    pdf_path = os.path.join(GENERATED_FOLDER, filename+".pdf")

    rendered = render_template("resume_template.html", **data)

    with open(html_path,"w",encoding="utf-8") as f:
        f.write(rendered)

    pdfkit.from_file(html_path, pdf_path, configuration=pdf_config)

    return render_template("resume_generated.html",
                           resume_file_pdf=filename+".pdf")

@app.route('/generated/<path:filename>')
def generated_file(filename):
    return send_file(os.path.join(GENERATED_FOLDER, filename))

if __name__ == "__main__":
    app.run(debug=True)

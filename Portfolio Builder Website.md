 **Portfolio Builder Website**



A simple \*\*Portfolio / Resume Builder\*\* web app built with \*\*Flask (Python)\*\* and \*\*Bootstrap (Frontend)\*\* that allows users to fill out their personal details, education, skills, and projects — and automatically generate a \*\*professional HTML/CSS resume\*\* that can be \*\*viewed online\*\* or \*\*downloaded as a PDF\*\*.



---

&nbsp;**Features**



✅ Responsive \*\*Bootstrap Frontend\*\*  

✅ Simple \*\*Flask Backend\*\* (No Database Required)  

✅ Dynamic \*\*HTML Resume Generation\*\*  

✅ \*\*PDF Download\*\* support using `pdfkit` + `wkhtmltopdf`  

✅ Includes support for \*\*Projects\*\*, \*\*Education\*\*, \*\*Skills\*\*, and \*\*Experience\*\*  

✅ Lightweight, fast, and runs fully on your local machine



---



**Tech Stack**



| Component | Technology |

|------------|-------------|

| Frontend | HTML, CSS, Bootstrap |

| Backend | Python (Flask) |

| PDF Conversion | pdfkit + wkhtmltopdf |

| Templates | Jinja2 (Flask built-in) |



---

&nbsp;Project Structure



portfolio-builder/

│

├── static/

│ └── style.css # Custom styles (optional)

│

├── templates/

│ ├── index.html # Form page for user input

│ ├── resume\_template.html # Resume layout

│

├── app.py # Flask backend

│

├── README.md # Documentation (this file)

│

└── requirements.txt # Dependencies list



yaml





---



**Installation Guide**



**Step 1**: Clone or Download the Project

Download or clone this project folder to your local machine:



```bash

git clone https://github.com/yourusername/portfolio-builder.git

cd portfolio-builder

Or simply extract the .zip file you downloaded.



 **Step 2**: Create a Virtual Environment





python -m venv venv

venv\\Scripts\\activate    # On Windows



 **Step 3:** Install Required Packages



pip install flask pdfkit



 **Step 4:** Install wkhtmltopdf



This tool converts the HTML resume to a PDF file.



🔗 Download:

https://wkhtmltopdf.org/downloads.html



📦 Installation Path:



It should be installed at:



C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe



🧭 Add to System PATH:



Press Windows + R, type sysdm.cpl, press Enter



Go to Advanced → Environment Variables



Under System variables, find and edit Path



Add new path:



C:\\Program Files\\wkhtmltopdf\\bin



Click OK, then



&nbsp;**open a new terminal and verify:**



wkhtmltopdf --version



✅ It should display a version number.



▶️ **Run the Application**



After setup,

 

**run the Flask server:**



python app.py



then you will see like this



&nbsp;\* Running on http://127.0.0.1:5000



Now open http://127.0.0.1:5000 in your browser.



 **How It Works**



Fill out the form with your personal, educational, project, and skill details.



Click Generate Resume to view it in browser.



Click Download PDF to export your resume as a PDF file.



🧾 **Example Form Fields**



Full Name



Email



Phone



Summary



Education



Experience



Projects (Title, Description)



Skills



📤 **Output Example**



When you click Download Resume, a file like this will be saved:



resume.pdf



containing your details in a formatted professional style.






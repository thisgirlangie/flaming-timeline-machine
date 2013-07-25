from flask import Flask, render_template, redirect, request, session
from model import Student, session
import model

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello World!"

@app.route("/add-student")
def display_add_student_form():
    html = render_template("add_student.html")
    return html

@app.route("/add-student-create")
def add_student_create():
    name = request.args.get("name")
    title_company = request.args.get("title_company")
    hb_class = request.args.get("hb_class")
    headshot_img_url = request.args.get("headshot_img_url")
    s = Student(name=name, title_company=title_company, hb_class=hb_class, headshot_img_url=headshot_img_url)
    session.add(s)
    session.commit()
    return "Succesfully added student!!"

if __name__ == "__main__":
    app.run(debug = True)
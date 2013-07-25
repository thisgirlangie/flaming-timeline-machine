from flask import Flask, render_template, redirect, request, session
from model import Student, Event, session

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello World!"

@app.route("/students")
def display_students():
    student_list = session.query(Student).limit(15).all()
    return render_template ("students.html", students=student_list)

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

@app.route("/add-event")
def display_add_event_form():
    html = render_template("add_event.html")
    return html


@app.route("/add-event-create")
def add_event_create():
    title = request.args.get("title")
    date = request.args.get("date")
    description = request.args.get("description")
    user_id = request.args.get("user_id")
    e = Event(title=title, date=date, description=description, user_id=user_id)
    session.add(e)
    session.commit()
    return "Succesfully added event for student!!"    

if __name__ == "__main__":
    app.run(debug = True)
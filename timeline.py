from flask import Flask, render_template, redirect, request, session
from model import Student, Event, session
from sqlalchemy import update

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello World!"

@app.route("/student-life")
def display_student_events():
    user_id = request.args.get("id")
    student_id = session.query(Student).get(user_id)
    return render_template("student_life.html", student=student_id)

@app.route("/students")
def display_students():
    student_list = session.query(Student).limit(15).all()
    return render_template("students.html", students=student_list)

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

@app.route("/events")
def display_events():
    events_list = session.query(Event).limit(15).all()
    return render_template("events.html", events=events_list)
    
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

@app.route("/edit-event")
def display_edit_event_form():
    id = request.args.get("id")
    title = request.args.get("title")
    date = request.args.get("date")
    description = request.args.get("description")
    user_id = request.args.get("user_id")
    event_id = session.query(Event).get(id)
    html = render_template("edit_event.html", event=event_id)
    return html

@app.route("/edit-event-now")
def edit_event():
    id = request.args.get("id") # event ID
    new_event = session.query(Event).get(id)
    new_event.title = request.args.get("title")
    new_event.date = request.args.get("date")
    new_event.description = request.args.get("description")
    user_id = request.args.get("user_id")
    new_event.user_id = user_id[0:1] # removing the pesky tuple that appeared in the ForeignKey
    session.commit()
    return render_template("student_life.html", student=new_event.user_id)

if __name__ == "__main__":
    app.run(debug = True)
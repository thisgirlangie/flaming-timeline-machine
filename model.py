from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, update
from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.orm import backref, relationship
from sqlalchemy import Table, MetaData, join
from sqlalchemy.orm import mapper

engine = create_engine("sqlite:///timelines.db", echo=False)
session = scoped_session(sessionmaker(bind=engine, autocommit = False, autoflush = False))

metadata = MetaData()

Base = declarative_base()
Base.query = session.query_property()

def connect():
    global ENGINE
    global Session

    ENGINE = create_engine("sqlite:///timelines.db", echo=True)
    Session = sessionmaker(bind=ENGINE)

    return Session()

def main():
    global session

class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True)
    name = Column(String(64), nullable=True)
    email = Column(String(64), nullable=True)
    password = Column(String(64), nullable=True)
    headshot_img_url = Column(String(250), nullable=True)
    title_company = Column(String(250), nullable=True)
    hb_class = Column(String(140), nullable=True)

    events = relationship("Event", backref=backref("students", order_by=id))

class Event(Base):
    __tablename__ = "events"

    id = Column(Integer, primary_key=True)
    title = Column(String(140), nullable=True) # ie. Graduated HB
    date = Column(String(140), nullable=True) # ie. Spring 2012
    description = Column(String(1000), nullable=True) # ie. Best day of my life
    user_id = Column(Integer, ForeignKey('students.id')) # Forgot to rename this item to student_id

    # for each event, there is a title and description
        # events: college grad, first/second/third job(s), 
        # started learning to code, applied to HB, started HB,
        # final project achieved, graduated HB, started job post-HB

if __name__ == "__main__":
    main()
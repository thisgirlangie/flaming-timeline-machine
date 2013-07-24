from flask import Flask, render_template, redirect, request
from model import User, session
import model # why do we call things model?!

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello World!"

if __name__ == "__main__":
    app.run(debug = True)
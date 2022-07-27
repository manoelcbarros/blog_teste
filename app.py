from flask import Flask, render_template
from datetime import datetime

app = Flask("hello")

posts = [
    {
        "title" : "O meu segundo Post",
        "body" : "Aqui é o texto do Post",
        "author" : "Manolo",
        "created" : datetime(2022,7,25)
    },
    {
        "title" : "O meu primeiro Post",
        "body" : "Aqui é o texto do Post",
        "author" : "Manolo",
        "created" : datetime(2022,7,26)
    },   
]

@app.route("/")
def index():
    return render_template("index.html", posts=posts)


import os
from flask import Flask, render_template
app = Flask(__name__)

os.environ["FLASK_DEBUG"] = "True"
app.debug = os.environ.get("FLASK_DEBUG") == "True"

@app.route("/")
def inicio():
    return render_template("index.html")

@app.route("/sobre")
def sobre():
    return render_template("sobre.html")

@app.route("/jogos")
def jogos():
    return render_template("jogos.html")

@app.route("/ittakestwo")
def jogo1():
    return render_template("jogo1.html")

@app.route("/splitfiction")
def jogo2():
    return render_template("jogo2.html")

@app.route("/awayout")
def jogo3():
    return render_template("jogo3.html")

@app.route("/gemini")
def gemini():
    return render_template("gemini.html")

app.run()
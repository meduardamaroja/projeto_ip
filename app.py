from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
def inicio():
    return render_template("index.html")

@app.route("/sobre")
def sobre():
    return render_template("sobre.html")

@app.route("/ittakestwo")
def ittakestwo():
    return render_template("jogo1.html")

@app.route("/jogo2")
def jogo2():
    return render_template("jogo2.html")

@app.route("/jogo3")
def jogo3():
    return render_template("jogo3.html")

@app.route("/gemini")
def gemini():
    return render_template("gemini.html")

app.run()
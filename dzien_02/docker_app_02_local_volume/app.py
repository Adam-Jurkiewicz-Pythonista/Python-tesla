from flask import Flask, request, render_template
from markupsafe import escape

app = Flask("APP_Template")

@app.route("/")
def hello_world():
    return render_template("index_start.html")

@app.route("/rejestruj")
def rejestruj():
    return "NIC"


@app.route("/user/<name>")
def hello_user(name):
    plec = "Dziewczynę" if name.endswith("a") else "Chłopaka"
    return render_template("zmienna.html", name=name, plec=plec)


# dla dockera nie jest to ważne
# app.run(host="0.0.0.0", port=5000, debug=True)
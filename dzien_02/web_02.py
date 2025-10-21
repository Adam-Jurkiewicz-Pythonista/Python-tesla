from flask import Flask, request

app = Flask("Moja nazwa aplikacji")

@app.route("/")
def hello_world():
    return "<h1>Hello, World!</h1>"

@app.route("/user/<name>")
def hello_user(name):
    plec = "Dziewczynę" if name.endswith("a") else "Chłopaka"
    return f"<h2>Hej {name} - wyglądasz na {plec}.</h2>"

@app.route("/user/")
def hello_user_request():
    name = request.args.get("imie", "NIC")
    return f"<h1>Halo -- {name}!</h1>"

app.run(host="0.0.0.0", port=5000)
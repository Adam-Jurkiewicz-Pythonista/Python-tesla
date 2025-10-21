from flask import Flask, request

app = Flask("Moja nazwa aplikacji")

@app.route("/")
def hello_world():
    return "<h1>Hello, World!</h1>"

@app.route("/user/<name>")
def hello_user(name):
    plec = "Dziewczynę" if name.endswith("a") else "Chłopaka"
    return f"<h2>Hej {name} - wyglądasz na {plec}.</h2>"

# http://localhost:5000/user2?imie=Adasiek&rok=1974
@app.route("/user2")
def hello_user_request():
    name = request.args.get("imie", "NIC")
    rok = request.args.get("rok", 0)
    if rok.isdigit():
        wiek = 2025 - int(rok)
        return f"<h1>Halo -- {name} / {rok=} / {wiek=} </h1>"
    else:
        return "<h3>Zła wartość roku</h3>"

app.run(host="0.0.0.0", port=5000, debug=True)
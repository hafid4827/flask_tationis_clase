from flask import Flask, render_template, redirect, url_for, request, session
from flask_session import Session
from os import urandom

from login import login_change

app = Flask("main_exampel_flask")

app.register_blueprint(login_change)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"

app.secret_key = urandom(24)

Session(app)


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html", name="joshua", holamundo="holamundo")


@app.route("/admin")
def admin():
    if session.get("user_name") and session.get("user_password"):
        return render_template("admin.html")
    
    return redirect(url_for("user.login"))


@app.route("/nombre/<nombre_param>", methods=["GET"])
def name_list(nombre_param):
    saludando = str(nombre_param) + "como te encuentras hoy"
    print(saludando)
    return render_template('saludo.html', name=saludando)

@app.route("/redireccionmiento/home")
def redirect_home():
    return redirect(url_for("login"))


@app.route("/probando", methods=["GET"])
def probando():
    lista_items = {
        "joshua": {
            "id": "123123",
            "anos": "123123123123123123",
            "ciudad": "laksjdalkjlkasjd"
        },
        "guillermos": {
            "id": "123123",
            "anos": "123123123123123123",
            "ciudad": "laksjdalkjlkasjd"
        },
        "sebastian": {
            "id": "123123",
            "anos": "",
            "ciudad": "laksjdalkjlkasjd"
        },
        "lennin": {
            "id": "123123",
            "anos": "123123123123123123",
            "ciudad": "laksjdalkjlkasjd"
        },
        "jeison": {
            "id": "123123",
            "anos": "123123123123123123",
            "ciudad": "laksjdalkjlkasjd"
        }
    }
    return render_template("for.html", items=lista_items)


if __name__ == "__main__":
    app.run(debug=True)

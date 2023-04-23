from flask import Flask, render_template, redirect, url_for, request

app = Flask("main_exampel_flask")


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html", name="joshua", holamundo="holamundo")


@app.route("/login", methods=["GET", "POST"])
def login():
    try:
        user_name = request.form['user_name']
        user_password = request.form['user_password']
        if user_name == "joshua" and user_password == "123456":
            return redirect(url_for("admin", user_name=user_name, user_password=user_password))
    except:
        pass

    return render_template('login.html')


@app.route("/admin/<user_name>/<user_password>")
def admin(user_name, user_password):
    return render_template("admin.html", user_name=user_name, user_password=user_password)


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

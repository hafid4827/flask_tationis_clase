from os import urandom
from flask import Flask, render_template, redirect, url_for, request, session
from flask_session import Session
from flaskext.mysql import MySQL
from hashlib import sha3_512

from login import login_change

app = Flask("main_exampel_flask")

app.register_blueprint(login_change)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"

# config mysql
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'flask_practice'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'

app.secret_key = urandom(24)

Session(app)

mysql = MySQL()
mysql.init_app(app)
cursor = mysql.connect().cursor()


@app.route("/create_count", methods=["POST", "GET"])
def create_count():
    if request.method == "POST":
        first_name = request.form["first_name"]
        age = request.form["age"]
        email = request.form["email"]
        password = request.form["password"]
        password_encrypt = sha3_512(password.encode("utf-8")).hexdigest()
        query = f"""
        INSERT INTO users 
        (first_name, age, email, password) 
        VALUES ("{first_name}", "{age}", "{email}", "{password_encrypt}"); 
        """
        cursor.execute(query)
        cursor.connection.commit()
        return redirect(url_for("login"))

    return render_template("register.html")


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html", name="joshua", holamundo="holamundo")


@app.route("/admin")
def admin():
    if session.get("user_name") and session.get("user_password"):
        return render_template("admin.html")
    return redirect(url_for("login"))


@app.route("/nombre/<nombre_param>", methods=["GET"])
def name_list(nombre_param):
    saludando = str(nombre_param) + "como te encuentras hoy"
    print(saludando)
    return render_template('saludo.html', name=saludando)

@app.route("/redireccionmiento/home")
def redirect_home():
    return redirect(url_for("login"))


@app.route("/create", methods=["POST"])
def create():
    msg = request.form["msg"]
    img = request.form["img"]
    date = request.form["fecha"]
    
    query = f"""
    INSERT INTO messages 
    (message_day, message_img, date_day_publish ) 
    VALUES ('{msg}', '{img}', '{date}');"""

    cursor.execute(query)
    cursor.connection.commit()
    
    return redirect(url_for("probando"))

@app.route('/delete/<id>')
def delete_by_id(id):
    if session.get("user_name") and session.get("user_password"):
        query = f"""DELETE FROM messages WHERE id = '{id}';"""
        cursor.execute(query)
        cursor.connection.commit()
        return redirect(url_for("probando"))
    return redirect(url_for("admin"))

@app.route("/update", methods=["POST"])
def update():
    if session.get("user_name") and session.get("user_password"):
        if request.method == "POST":
            _id = request.form["id"]
            msg = request.form["msg"]
            img = request.form["img"]
            date = request.form["fecha"]
            query = f"""
            UPDATE messages 
            SET message_day = '{msg}', message_img = '{img}', date_day_publish = '{date}'
            WHERE id = '{_id}';
            """
            cursor.execute(query)
            cursor.connection.commit()
        return redirect(url_for("probando"))
    return redirect(url_for("admin"))


@app.route("/probando", methods=["GET"])
def probando():
    if session.get("user_name") and session.get("user_password"):
        query = """SELECT * FROM messages"""
        cursor.execute(query)
        account = cursor.fetchall()
        return render_template("for.html", items=account)
    return redirect(url_for("admin"))


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        
        user_name = request.form['user_name']
        user_password = request.form['user_password']
        password_encrypt = sha3_512(user_password.encode("utf-8")).hexdigest()

        query = f"""SELECT first_name, password FROM users WHERE first_name = '{user_name}' AND password = '{password_encrypt}';"""
        try:
            cursor.execute(query)
            account = cursor.fetchone()
            session["user_name"] = user_name
            session["user_password"] = password_encrypt
            if account[0] ==session["user_name"] and account[1] == session["user_password"]:
                return redirect(url_for("admin"))
        except:
            return redirect(url_for("login"))
        
    return render_template('login.html')


@app.route("/logout")
def logout():
    if session.get("user_name") and session.get("user_password"):
        session["user_name"] = None
        session["user_password"] = None
    return redirect(url_for('login'))


if __name__ == "__main__":
    app.run(debug=True)

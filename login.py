from flask import render_template, redirect, url_for, request, session, Blueprint


login_change = Blueprint("user", __name__, template_folder="templates")

@login_change.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user_name = request.form['user_name']
        user_password = request.form['user_password']
        session["user_name"] = user_name
        session["user_password"] = user_password
        return redirect(url_for("admin"))
        
    return render_template('login.html')


@login_change.route("/logout")
def logout():
    if session.get("user_name") and session.get("user_password"):
        session["user_name"] = None
        session["user_password"] = None
    return redirect(url_for('login'))

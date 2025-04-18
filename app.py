import sqlite3
from flask import Flask
from flask import redirect, render_template, request, session
from werkzeug.security import generate_password_hash, check_password_hash
import db
import config, location


app = Flask(__name__)
app.secret_key = config.secret_key


@app.route("/")
def index():
    return render_template("index.html")

# Uusi tietokohde, ja sen tulos
@app.route("/new_location")
def order():
    return render_template("order.html")


@app.route("/result", methods=["POST"])
def result(): 
    try:
        if "user_id" not in session:
            return redirect("/login")

        bar_name = request.form.get("bar_name")
        bar_address= request.form.get("bar_address")
        extras = request.form.getlist("extra")
        extra_info = request.form.get("extra_info", "")

        drinks = {
            'beer': {
                'selected': request.form.get("beer") == "on",
                'sizes': request.form.getlist("bsize"),
                'prices': request.form.getlist("bprice")
            },
            'lonkero': {
                'selected': request.form.get("lonkero") == "on",
                'sizes': request.form.getlist("lsize"),
                'prices': request.form.getlist("lprice")
            },
            'ananas': {
                'selected': request.form.get("ananas") == "on",
                'sizes': request.form.getlist("asize"),
                'prices': request.form.getlist("aprice")
            },
            'cider': {
                'selected': request.form.get("cider") == "on",
                'sizes': request.form.getlist("csize"),
                'prices': request.form.getlist("cprice")
            }
        }

        new_location_id = location.add_location(bar_name=bar_name, bar_address=bar_address,
        user_id=session["user_id"],
        happy_hour=1 if 'happy_hour' in extras else 0,
        student_discount=1 if 'student_discount' in extras else 0,
        gluten_free=1 if 'gluten_free' in extras else 0,
        student_patch=1 if 'student_patch' in extras else 0,
        extra_info=extra_info )

        for drink_type, data in drinks.items():
            data["pairs"] = list(zip(data["sizes"], data["prices"]))

        return render_template(
            "result.html",
            bar_name=bar_name,
            bar_address=bar_address,
            drinks=drinks,
            extras=extras,
            extra_info=extra_info)

    except Exception as e:
        print(f"Error: {str(e)}")
        return "An error occurred", 500
    

# kirjautimen rekisteröinti

@app.route("/register")
def register():
    return render_template("register.html")


@app.route("/create", methods=["POST"])
def create():
    username = request.form["username"]
    password1 = request.form["password1"]
    password2 = request.form["password2"]
    if password1 != password2:
        return "VIRHE: salasanat eivät ole samat"
    password_hash = generate_password_hash(password1)

    try:
        sql = "INSERT INTO users (username, password_hash) VALUES (?, ?)"
        db.execute(sql, [username, password_hash])
    except sqlite3.IntegrityError:
        return "VIRHE: tunnus on jo varattu"

    return render_template("account_created.html")


@app.route("/login", methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]
    
    sql = "SELECT id, password_hash FROM users WHERE username = ?"  
    result = db.query(sql, [username])
    
    if not result:
        return "VIRHE: väärä tunnus tai salasana"
        
    user_id, password_hash = result[0]
    
    if check_password_hash(password_hash, password):
        session["username"] = username
        session["user_id"] = user_id  
        return redirect("/")
    else:
        return "VIRHE: väärä tunnus tai salasana"

@app.route("/logout")
def logout():
    session.clear()  
    return redirect("/")
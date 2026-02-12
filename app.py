from flask import Flask, render_template, request, redirect, url_for, flash
from models import db, Doctor
from flask_login import LoginManager
from werkzeug.security import generate_password_hash, check_password_hash
import os

app = Flask(__name__)

app.config['SECRET_KEY'] = 'your-secret-key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    db.creat_all()

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

@login_manager.user_loader
def load_user(user_id):
    return Doctor.query.get(int(user_id))

@app.route("/")
def home():
    return "Homeopathy Repertory Platform - Login Required"

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        password = request.form.get("password")

        existing_user = Doctor.query.filter_by(email=email).first()
        if existing_user:
            flash("Email already registered.")
            return redirect(url_for("register"))

        hashed_password = generate_password_hash(password)

        new_doctor = Doctor(
            name=name,
            email=email,
            password=hashed_password
        )

        db.session.add(new_doctor)
        db.session.commit()

        flash("Registration successful! Please login.")
        return redirect(url_for("home"))

    return render_template("register.html")
        
if __name__ == "__main__":
    with app.app_context():
        db.create_all()
app = Flask(__name__)
app.config["SECRET_KEY"] = "supersecret"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

with app.app_context():
    db.create_all()

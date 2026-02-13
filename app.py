from flask import Flask, render_template, request, redirect, url_for, flash
from yourapp import app, db
from yourapp.models import Doctor

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("password")

        if not username or not email or not password:
            flash("All fields are required.")
            return render_template("register.html")

        existing_user = Doctor.query.filter_by(email=email).first()
        
        if existing_user:
            flash("Email already registered.")
            return render_template("register.html")

        if username and email and password:
            new_user = Doctor(username=username, email=email, password=password)
            db.session.add(new_user)
            db.session.commit()
            flash("Registration successfull! Please login.")
            return redirect(url_for("login"))

return render_template("register.html")

       

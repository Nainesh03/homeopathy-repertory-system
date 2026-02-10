from flask import Flask, render_template
from data.demo_data import rubrics

app = Flask(_name_)

@app.route("/")
def index():
    return render_template("index.html", rubrics=rubrics)

if _name_ == "_main_":
    app.run(host="0.0.0.0", port=5000)

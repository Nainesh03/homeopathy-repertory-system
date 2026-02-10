from flask import Flask, render_template from data.demo_data import rubrics
app = Flask (__name__)
@app.route("/")
def index() :
    return render_template("index.html", rubrics=rubrics)
if __name__== "__main__":
    app.run(host="0.0.0.0", port=5000) 

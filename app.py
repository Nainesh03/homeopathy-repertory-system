from flask import flask, render_template
from data.demo_data import rubrics
import os

app = flash(__name__)

@app.route("/")
def index():
  return render_template("index.html",rubrics=rubrics)

if __name__ == "__main__":
  port = int(os.environ.get("PORT", 5000))
  app.run(host="0.0.0.0", port=port)

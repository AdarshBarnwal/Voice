from flask import Flask, render_template, request
from app_backend import ask_llama

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    response = ""
    if request.method == "POST":
        question = request.form["question"]
        response = ask_llama(question)
    return render_template("index.html", response=response)

if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for, session
from app_backend import ask_llama  # Modular logic import
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)  # Secure random key for session

# Bot response handler
def get_bot_response(question):
    return ask_llama(question)  # Modular backend call

@app.route("/", methods=["GET", "POST"])
def index():
    if "chat_history" not in session:
        session["chat_history"] = []

    if request.method == "POST":
        question = request.form["question"]
        response = get_bot_response(question)
        session["chat_history"].append({"user": question, "bot": response})
        session.modified = True

    return render_template("index.html", chat_history=session["chat_history"])

@app.route("/reset", methods=["POST"])
def reset():
    session["chat_history"] = []
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)

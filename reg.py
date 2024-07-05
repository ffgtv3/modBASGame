from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Простая "база данных" (в реальном проекте используйте настоящую БД)
users = {}

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        users[username] = password  # "Регистрация" пользователя
        return redirect(url_for("forum"))
    return render_template("reg.html")

@app.route("/forum")
def forum():
    return "Добро пожаловать на форум!"

if __name__ == "__main__":
    app.run(debug=True)

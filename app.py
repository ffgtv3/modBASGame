from flask import Flask, render_template, request, redirect, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Замените на случайный секретный ключ!

# Простая "база данных" (в реальном проекте используйте настоящую БД)
users = {}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        # Проверка, существует ли уже пользователь
        if username in users:
            flash('Имя пользователя уже занято', 'error')
            return redirect(url_for('register'))

        # Хеширование пароля перед сохранением
        hashed_password = generate_password_hash(password)

        # Сохранение пользователя (в реальном проекте - в базу данных)
        users[username] = {'email': email, 'password': hashed_password}

        flash('Регистрация прошла успешно!', 'success')
        return redirect(url_for('index'))

    return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True)
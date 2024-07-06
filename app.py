# Импортируем необходимые библиотеки
from flask import Flask, render_template

# Создаем экземпляр приложения Flask
app = Flask(__name__)

# Определяем маршрут для главной страницы
@app.route('/')
def index():
    return render_template('index.html')

# Определяем маршрут для страницы "О нас"
@app.route('/about')
def about():
    return render_template('about.html')

# Определяем маршрут для страницы "Форум"
@app.route('/forum')
def forum():
    return render_template('forum.html')

# Запускаем приложение
if __name__ == '__main__':
    app.run(debug=True)
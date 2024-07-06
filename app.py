from flask import Flask, send_file

app = Flask(__name__)

@app.route('/')
def index():
    # Путь к HTML-файлу
    html_file = 'index.html'

    # Отправить HTML-файл в браузер
    return send_file(html_file, mimetype='text/html')

if __name__ == '__main__':
    app.run()
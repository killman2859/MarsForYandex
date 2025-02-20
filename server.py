from flask import Flask

app = Flask(__name__)


@app.route('/')
def start():
    return "Миссия Колонизация Марса"


@app.route('/index')
def index():
    return "И на Марсе будут яблони цвести!"


@app.route('/promotion')
def promotion():
    return "Человечество вырастает из детства.<br>Человечеству мала одна планета.<br>Мы сделаем обитаемыми безжизненные пока планеты.<br>И начнем с Марса!<br>Присоединяйся!"


@app.route('/image_mars')
def image_mars():
    return '''<html><title>Привет, Марс!</title><h1>Жди нас, Марс!</h1><img src="static/Images/mars.png" alt="Mars surface" width=500 height=500><br><br>Вот она красная планета!</html>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')

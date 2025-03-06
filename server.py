from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def start():
    return render_template('index.html', username="killman2859", title="Заготовка")


@app.route('/training/<prof>')
def training(prof):
    if "инженер" in prof or "строитель" in prof:
        return render_template('training.html', username="killman2859", title2="Инженерные тренажеры",
                               title="Миссия марс")
    return render_template('training.html', username="killman2859",
                           title2="Научные симуляторы", title="Миссия марс")


@app.route('/index')
def index():
    return "И на Марсе будут яблони цвести!"


@app.route('/promotion')
def promotion():
    return "Человечество вырастает из детства.<br>Человечеству мала одна планета.<br>Мы сделаем обитаемыми безжизненные пока планеты.<br>И начнем с Марса!<br>Присоединяйся!"


@app.route('/list_prof/<lst>')
def list_prof(lst):
    return render_template('list_prof.html', username="killman2859", title="Список профессий",
                           profs=['Инженер', 'Физик-Ядерщик', 'Что-то ещё'], list=lst)


@app.route('/image_mars')
def image_mars():
    return '''<html><title>Привет, Марс!</title><h1>Жди нас, Марс!</h1><img src="static/Images/mars.png" alt="Mars surface" width=500 height=500><br><br>Вот она красная планета!</html>'''


@app.route('/promotion_image')
def promotion_image():
    return '''<!DOCTYPE html>
<html lang="ru">
<head>
    <title>Колонизация</title>
    <link rel="stylesheet" href="static/css/style.css">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
</head>

<body>
<h1 class="welcome_text">Жди нас марс!</h1>
<img src="static/Images/mars.png" alt="Mars surface" width=500 height=500>
<div class="p-3 mb-2 bg-primary text-white">Человечество вырастает из детства.</div>
<div class="p-3 mb-2 bg-secondary text-white">Человечеству мала одна планета.</div>
<div class="p-3 mb-2 bg-danger text-white">Мы сделаем безжизнеными пока планеты.</div>
<div class="p-3 mb-2 bg-warning text-white">И начнём с Марса!</div>
<div class="p-3 mb-2 bg-info text-white">Присоединяйся!</divЮ
</body>

</html>'''


@app.route('/registration', methods=['POST', 'GET'])
def registration():
    if request.method == 'GET':
        return render_template('reg.html')
    else:
        email = request.form.get('email')
        school_class = request.form.get('class')
        about = request.form.get('about')
        return render_template('auto_answer.html', email=email, school_class=school_class, about=about)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')

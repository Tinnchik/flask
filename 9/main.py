from os import makedirs
from os.path import exists, join

from flask import Flask, request, url_for, redirect, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Миссия Колонизация Марса</h1>'


@app.route('/index')
def name():
    return '<h1>И на Марсе будут яблони цвести!</h1>'


@app.route('/promotion')
def promotion():
    return ('<h1>Человечество вырастает из детства.</h1>'
            '<h1>Человечеству мала одна планета.</h1>'
            '<h1>Мы сделаем обитаемыми безжизненные пока планеты.</h1>'
            '<h1>И начнем с Марса!</h1>' + '<h1>Присоединяйся!</h1>')


@app.route('/image_mars')
def image_mars():
    return '''<!doctype html>
                <html lang="en">
                  <head>
                    <title>Привет, Марс!</title>
                  </head>
                  <body>
                    <h1>Жди нас Марс</h1>
                    <img src="https://i.pinimg.com/736x/d6/c4/94/d6c494ee44bd9d7ec69653ced9bf92dd.jpg">
                    <h3> Вот она какая, красная планета </h3>
                  </body>
                </html>'''


@app.route('/promotion_image')
def promotion_image():
    return '''<!doctype html>
                    <html lang="en">
                      <head>
                        <title>Привет, Марс!</title>
                      </head>
                      <body>
                        <h1 style="color: red">Жди нас Марс</h1>
                        <img src="https://i.pinimg.com/736x/d6/c4/94/d6c494ee44bd9d7ec69653ced9bf92dd.jpg">
                        <h1 style = "background: lightgray" class="m-5 alert">Человечество вырастает из детства.</h1>
                        <h1 style = "background: lightgreen" class="m-5 alert">Человечеству мала одна планета.</h1>
                        <h1 style = "background: lightgray" class="m-5 alert">Мы сделаем обитаемыми безжизненные пока планеты.</h1>
                        <h1 style = "background: lightyellow" class="m-5 alert">И начнем с Марса!</h1>
                        <h1 style = "background: pink" class="m-5 alert">Присоединяйся!</h1>
                      </body>
                    </html>'''


@app.route('/astrounaut_selection')
def astrounaut_selection():
    return '''<!doctype html>
                    <html lang="en">
                      <head>
                      <meta charset="utf-8">
                      <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                      <link rel="stylesheet"
                            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                            crossorigin="anonymous">
                        <link rel="stylesheet" type="text/css" href="/static/style.css"/>
                        <title>Отбор астронавтов</title>
                      </head>
                      <body>
                      <h1 style="text-align: center;">Анкета претендента</h1>
                        <h2 style="text-align: center;">на участие в миссии</h2>
                      <div>
                        <div>
                                <form class="login_form" method="post">
                                    <input type="email" class="form-control" id="surname" placeholder="Введите фамилия" name="surname">
                                    <input type="password" class="form-control" id="name" placeholder="Введите имя" name="name">
                                    <br></br>
                                    <input type="password" class="form-control" id="email" placeholder="Введите адрес почты" name="email">
                                    <div class="form-group">
                                        <label for="classSelect">Какое у вас образование</label>
                                        <select class="form-control" id="classSelect" name="class">
                                          <option>Начальное</option>
                                          <option>Среднее</option>
                                          <option>Высшее</option>
                                        </select>
                                        <div class="form-group">
                                        <label for="form-check">Какие у вас профессии?</label>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="type" id="male" value="male" checked>
                                          <label class="form-check-label" for="male">
                                            Мужской
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                                          <label class="form-check-label" for="female">
                                            Женский
                                          </label>
                                        </div>
                                    </div>
                                     </div>
                                    <div class="form-group">
                                        <label for="about">Немного о себе</label>
                                        <textarea class="form-control" id="about" rows="3" name="about"></textarea>
                                    </div>
                                    <div class="form-group">
                                        <label for="photo">Приложите фотографию</label>
                                        <input type="file" class="form-control-file" id="photo" name="file">
                                    </div>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label" for="acceptRules">Готов быть добровольцем</label>
                                    </div>
                                    <button type="submit" class="btn btn-primary">Записаться</button>
                                </form>
                            </div>
                        </div>
                      </body>
                    </html>'''


@app.route('/results/<name>/<level>/<rating>')
def choice(name, level, rating):
    return f'''<html lang="en"><head>
    <meta charset="UTF-8">
    <title>Результаты</title>
    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
    </head>
  <body>
    <div class="p-5">
      <h1>Результаты отбора</h1>
      <h2>Претендент на участие в миссии {name}</h2>
      <div class="alert alert-success">"Поздравляем! Ваш рейтинт после {level} этапа отбора"</div>
      <div>составляет {rating}</div>
      <div class="alert alert-secondary">Желаем удачи</div>
    </div>

  <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
  </body></html>
'''


@app.route('/load_photo', methods=['POST', 'GET'])
def load_photo():
    if request.method == 'GET':
        return f'''<!doctype html>
                            <html lang="en">
                              <head>
                                <meta charset="utf-8">
                                <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                                 <link rel="stylesheet"
                                 href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                                 integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                                 crossorigin="anonymous">
                                <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                                <title>Пример загрузки файла</title>
                              </head>
                              <body>
                                <h1>Загрузим файл</h1>
                                <form method="post" enctype="multipart/form-data">
                                   <div class="form-group">
                                        <label for="photo">Выберите файл</label>
                                        <input type="file" class="form-control-file" id="photo" name="file">
                                    </div>
                                    <button type="submit" class="btn btn-primary">Отправить</button>
                                </form>
                              </body>
                            </html>'''
    elif request.method == 'POST':
        f1 = request.files['file']
        with open('static/img/img.jpg', 'wb') as f:
            f.write(f1.read())
        return '''<img src="{url_for('static', filename='img/img.jpg')}" 
                   alt="здесь должна была быть картинка, но не нашлась">'''


@app.route('/carousel', methods=['POST', 'GET'])
def galery():
    return '''<html lang="en"><head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <body>
  <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
    </head>
    <div class="p-5">
      <h1 class="text-center">Пейзажи Марса</h1>

      <div id="carouselExample" class="carousel slide" data-bs-ride="carousel">
        <div class="carousel-inner">
          <div class="carousel-item active" data-bs-interval="500">
            <img src="https://i.pinimg.com/736x/b7/e6/c7/b7e6c71b5ce0c2e509bad526915961fd.jpg" class="d-block w-100">
          </div>
          <div class="carousel-item" data-bs-interval="500">
            <img src="https://cdna.artstation.com/p/assets/images/images/028/598/264/large/knife-entertainment-frame-0309.jpg?1594922978" class="d-block w-100">
          </div>
          <div class="carousel-item" data-bs-interval="500">
            <img src="https://i.ytimg.com/vi/w3vRyGLnqfs/maxresdefault.jpg" class="d-block w-100">
          </div>
          <div class="carousel-item" data-bs-interval="500">
            <img src="https://thumbs.dreamstime.com/b/desert-mars-landscapes-sand-rocks-generative-ai-268284761.jpg" class="d-block w-100">
          </div>
        </div>
        <button class="carousel-control-prev" type="button" data-bs-target="#carouselExample" data-bs-slide="prev">
          <span class="carousel-control-prev-icon" aria-hidden="true"></span>
          <span class="visually-hidden">Previous</span>
        </button>
        <button class="carousel-control-next" type="button" data-bs-target="#carouselExample" data-bs-slide="next">
          <span class="carousel-control-next-icon" aria-hidden="true"></span>
          <span class="visually-hidden">Next</span>
        </button>
      </div>
      <h1>Загрузим файл</h1>
                                <form method="post" enctype="multipart/form-data">
                                   <div class="form-group">
                                        <label for="photo">Выберите файл</label>
                                        <input type="file" class="form-control-file" id="photo" name="file">
                                    </div>
                                    <button type="submit" class="btn btn-primary">Отправить</button>
                                </form>
    </div>

  </body></html>'''


@app.route('/member')
def member():
    with open('members.json', 'r', encoding='utf-8') as f:
        mem = choice(f.read())
    return f'''<html lang="en"><head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <body>
  <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
    </head>
    <div class="p-5">
        {mem['name']}, {mem['lastname']}
      </div>
      <h1>Загрузим файл</h1>
                                <form method="post" enctype="multipart/form-data">
                                   <div class="form-group">
                                        <label for="photo">Выберите файл</label>
                                        <input type="file" class="form-control-file" id="photo" name="file">
                                    </div>
                                    <button type="submit" class="btn btn-primary">Отправить</button>
                                </form>
    </div>
    {mem['prof']}, {mem['spet']}

  </body></html>'''


if __name__ == '__main__':
    app.run(debug=True, port=8080)

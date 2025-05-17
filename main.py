from flask import Flask, render_template

app = Flask(__name__)


@app.route('/<title>')
@app.route('/index/<title>')
def index(title):
    params = {'title': title}
    return render_template('base.html', **params)


if __name__ == '__main__':
    app.run(debug=True, port=8080)

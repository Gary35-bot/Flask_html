from flask import Flask, render_template

app = Flask(__name__)


@app.route('/<name>/')
def home(name):
    return render_template('homepage.html', name=name)


@app.route("/<name>", methods=['GET', 'POST'])
def picture(name):
    return render_template('homepage.html', name=name)


if __name__ == '__main__':
    app.debug = True
    app.run()

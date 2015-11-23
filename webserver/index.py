from flask import Flask

__author__ = 'Burgy Benjamin'
__version__ = 0.1

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()

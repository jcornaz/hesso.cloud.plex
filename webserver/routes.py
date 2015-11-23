from flask import Flask, send_from_directory, url_for
from about import about_controller

app = Flask(__name__)


@app.route('/')
def main():
    return send_from_directory('static', 'index.html')


@app.route('/about')
def about(): return about_controller()

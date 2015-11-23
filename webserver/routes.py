from flask import Flask, render_template, send_from_directory
from about import about_controller

app = Flask(__name__)


@app.route('/')
def main():
    return render_template('index.html', title = 'Plex Media File Manager')


@app.route('/about')
def about(): return about_controller()


@app.route('/bower/<path:path>')
def bower_components(path):
    return send_from_directory('bower_components', path)

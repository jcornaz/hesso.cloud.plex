from flask import Flask, render_template

from about import about_controller

app = Flask(__name__)


@app.route('/')
def main():
    return render_template('index.html', title = 'Plex Media File Manager')


@app.route('/about')
def about(): return about_controller()

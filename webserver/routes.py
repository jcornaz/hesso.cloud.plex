from flask import Flask, send_from_directory, url_for, render_template
from about import about_controller

app = Flask(__name__)


@app.route('/')
def main():
    return render_template('index.html', title = 'Plex Media File Manager')


@app.route('/about')
def about(): return about_controller()

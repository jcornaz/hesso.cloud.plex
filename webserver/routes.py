from flask import Flask
from about import about_controller

# Start the webserver
from home import home_controller

app = Flask(__name__)


@app.route('/')
def main(): return home_controller()


@app.route('/about')
def about(): return about_controller()

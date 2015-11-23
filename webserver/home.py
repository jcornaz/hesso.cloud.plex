from flask import render_template


def home_controller():
    return render_template('main.html', title='Home Plex Media File Manager')

from flask import render_template


def about_controller():
    return render_template('main.html', title='Plex Media File Manager')

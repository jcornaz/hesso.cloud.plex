from flask import Flask, render_template, send_from_directory
from flask_json import as_json, FlaskJSON

from controllers.about_controller import about_controller
from controllers.directory_create_controller import directory_create_controller
from controllers.file_controller import file_controller
from controllers.file_delete_controller import file_delete_controller
from controllers.file_upload_controller import file_upload_controller
from controllers.files_controller import files_controller

app = Flask(__name__)
json = FlaskJSON()


@app.route('/')
def main():
    return render_template('index.html', title = 'Plex Media File Manager')


@app.route('/about')
@as_json
def about():
    return about_controller()


@app.route('/bower/<path:path>')
def bower_components(path):
    return send_from_directory('bower_components', path)


@app.route('/files')
@as_json
def files():
    return files_controller()


@app.route('/file/', defaults = {'path': '<root>'}, methods = ['GET'])
@app.route('/file/<path:path>', methods = ['GET'])
@as_json
def file(path):
    return file_controller(path)


@app.route('/file/<path:path>', methods = ['DELETE'])
@as_json
def file_delete(path):
    return file_delete_controller(path)


@app.route('/file/<path:path>', methods = ['POST'])
@as_json
def file_upload(path):
    return file_upload_controller(path)


@app.route('/file/<path:path>', methods = ['PUT'])
@as_json
def directory_create(path):
    return directory_create_controller(path)

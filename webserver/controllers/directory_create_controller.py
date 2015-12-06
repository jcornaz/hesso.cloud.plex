from os import makedirs
from os.path import exists

from flask import jsonify

from Services.PathService import get_absolute_storage_path


def directory_create_controller(path):
    absolute_path = get_absolute_storage_path(path)
    json = {'directory_path': path, 'error': True}

    try:
        if exists(path):
            json['message'] = 'The folder %s already exists.' % path

        else:
            makedirs(absolute_path)
            json['error'] = False

    except Exception as e:
        json['message'] = '%s' % e

    return jsonify(json)

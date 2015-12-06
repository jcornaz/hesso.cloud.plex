from os import rmdir
from os.path import isdir

from flask import jsonify

from Services.PathService import get_absolute_storage_path


def directory_delete_controller(path):
    absolute_path = get_absolute_storage_path(path)
    storage_path = get_absolute_storage_path()

    if not isdir(absolute_path):
        json = {'error': True, 'message': "%s not found." % path}

    elif absolute_path == storage_path:
        json = {'error': True, 'message': 'You cannot delete the root storage.'}

    else:
        rmdir(absolute_path)
        json = {'error': False, 'message': "Directory %s successfully deleted." % path}

    return jsonify(json)

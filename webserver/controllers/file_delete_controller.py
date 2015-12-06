from os import remove

from os.path import isfile
from shutil import rmtree
from flask import jsonify

from services.PathService import get_absolute_storage_path


def file_delete_controller(path):
    absolute_path = get_absolute_storage_path(path)

    try:
        if isfile(absolute_path):
            remove(absolute_path)
            json = {'error': False, 'message': "File %s successfully deleted." % path}
        else:
            rmtree(absolute_path)
            json = {'error': False, 'message': "Directory %s successfully deleted." % path}

    except Exception as e:
        json = {'error': True, 'message': e}

    return jsonify(json)

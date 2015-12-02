from os import remove
from os.path import isfile, abspath
from shutil import rmtree

import flask

from index import settings


def file_delete_controller(path):
    storage_path = settings['application']['storage']
    absolute_path = abspath('{0}/{1}'.format(storage_path, path))

    try:
        if isfile(absolute_path):
            remove(absolute_path)
            return flask.jsonify({'error': False, 'message': "File {0} successfully deleted.".format(path)})
        else:
            rmtree(absolute_path)
            return flask.jsonify({'error': False, 'message': "Directory {0} successfully deleted.".format(path)})

    except Exception as e:
        return flask.jsonify({'error': True, 'message': e})

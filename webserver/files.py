from os import walk
from os.path import normpath, normcase, sep

import flask

from index import settings


def files_controller():
    storage_path = normcase(normpath(settings['application']['storage']))
    json = []

    for root, dirs, files in walk(storage_path, topdown = True):

        if files.__len__() > 0:
            json.append((remove_base_folder(root, storage_path), files))

    return flask.jsonify(json)


def remove_base_folder(path, base):
    return normcase(normpath(path.replace(base, '').lstrip(sep))).replace('\\', '/')

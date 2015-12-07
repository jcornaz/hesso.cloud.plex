from datetime import datetime
from os.path import exists, basename, getmtime, getsize, isdir, isfile, getctime

import flask

from services.PathService import get_absolute_storage_path, get_relative_storage_path, format_path


def file_controller(path):
    absolute_path = get_absolute_storage_path(path)
    storage_path = get_absolute_storage_path()
    display_path = get_relative_storage_path(absolute_path)

    json = {'display_path': display_path,
            'canDelete'   : False,
            'path'        : format_path(display_path)}

    if not exists(absolute_path):
        json['error'] = True
        json['message'] = 'The given path is not found.'

        return flask.jsonify(json)

    json['exists'] = True
    json['name'] = basename(absolute_path)
    json['lastModification'] = getmtime(absolute_path)

    if isdir(absolute_path):
        json['isFile'] = False

    if isfile(absolute_path):
        size = getsize(absolute_path)
        creation_time = datetime.fromtimestamp(getctime(absolute_path)).strftime('%Y-%m-%d %H:%M:%S')

        json['isFile'] = True
        json['size'] = size
        json['size_mb'] = "%.1f" % (size / 1024 / 1024)
        json['creation_time'] = creation_time

    if not absolute_path == storage_path:
        json['canDelete'] = True

    return flask.jsonify(json)

from datetime import datetime
from os.path import normpath, normcase, sep, exists, basename, getmtime, abspath, getsize, isdir, isfile, getctime

import flask

from index import settings


# url: https://docs.python.org/2/library/os.path.html

def file_controller(path):
    storage_path = settings['application']['storage']
    absolute_path = abspath('{0}/{1}'.format(storage_path, path))
    json = {('path', remove_base_folder(absolute_path, storage_path))}

    if not exists(absolute_path):
        json.add(('error', True))
        json.add(('message', 'The given path is not found.'))

        return flask.jsonify(json)

    json.add(('exists', True))
    json.add(('name', basename(absolute_path)))
    json.add(('lastModification', getmtime(absolute_path)))

    if isdir(absolute_path):
        json.add(('isFile', False))

    if isfile(absolute_path):
        size = getsize(absolute_path)
        creation_time = datetime.fromtimestamp(getctime(absolute_path)).strftime('%Y-%m-%d %H:%M:%S')

        json.add(('isFile', True))
        json.add(('size', size))
        json.add(('size_mb', "%.1f" % (size / 1024 / 1024)))
        json.add(('creation_time', creation_time))

    return flask.jsonify(json)


def remove_base_folder(path, base):
    return normcase(normpath(path.replace(base, '').lstrip(sep))).replace('\\', '/')

import os

import flask

from index import settings


def file_controller(path):
    absolute_path = os.path.abspath('{0}/{1}'.format(settings['application']['storage'], path))
    json = {('path', absolute_path)}

    if not os.path.exists(absolute_path):
        json.add(('error', True))
        json.add(('message', 'The given path is not found.'))

    json.add(('exists', True))
    json.add(('name', os.path.basename(absolute_path)))
    json.add(('lastModification', os.path.getmtime(absolute_path)))

    if os.path.isdir(absolute_path):
        json.add(('isDirectory', True))

    if os.path.isfile(absolute_path):
        json.add(('isFile', True))
        json.add(('size', os.path.getsize(absolute_path)))

    return flask.jsonify(json)

from os import listdir
from os.path import normpath, normcase, sep, join, isdir

import flask

from index import settings


def files_controller():
    storage_path = normcase(normpath(settings['application']['storage']))

    json = {'label': 'storage', 'id': '.', 'children': browse_folder(storage_path, storage_path)}

    return flask.jsonify(json)


# noinspection PyBroadException
def browse_folder(source_path, base):
    json = []

    try:
        for entry in listdir(source_path):
            path = join(source_path, entry)
            display_path = remove_base_folder(path, base)

            json_entry = {'label': entry, 'id': display_path}

            if isdir(path):
                json_entry['children'] = browse_folder(path, base)

            json.append(json_entry)
    except:
        pass

    return json


def remove_base_folder(path, base):
    return normcase(normpath(path.replace(base, '').lstrip(sep))).replace('\\', '/')

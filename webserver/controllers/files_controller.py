from os import listdir
from os.path import isdir

import flask

from services.PathService import get_absolute_storage_path, join, get_relative_storage_path, format_path


def files_controller():
    storage_path = get_absolute_storage_path()

    json = {'label': 'storage', 'id': '<root>', 'children': browse_folder(storage_path, storage_path)}

    return flask.jsonify(json)


# noinspection PyBroadException
def browse_folder(source_path, base):
    json = []

    try:
        for entry in listdir(source_path):
            path = join(source_path, entry)
            relative_path = get_relative_storage_path(path)
            entry_id = format_path(relative_path)

            json_entry = {'label': entry, 'id': entry_id}

            if isdir(path):
                json_entry['children'] = browse_folder(path, base)

            json.append(json_entry)
    except:
        pass

    return json

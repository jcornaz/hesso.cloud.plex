from datetime import datetime
from os.path import normpath, normcase, sep, isdir, getctime, abspath, basename, getsize

from flask import render_template

from index import settings


# url: https://docs.python.org/2/library/os.path.html

# def file_controller(path):
#     absolute_path = os.path.abspath('{0}/{1}'.format(settings['application']['storage'], path))
#     json = {('path', absolute_path)}
#
#     if not os.path.exists(absolute_path):
#         json.add(('error', True))
#         json.add(('message', 'The given path is not found.'))
#
#         return flask.jsonify(json)
#
#     json.add(('exists', True))
#     json.add(('name', os.path.basename(absolute_path)))
#     json.add(('lastModification', os.path.getmtime(absolute_path)))
#
#     if os.path.isdir(absolute_path):
#         json.add(('isFile', False))
#
#     if os.path.isfile(absolute_path):
#         json.add(('isFile', True))
#         json.add(('size', os.path.getsize(absolute_path)))
#
#     return flask.jsonify(json)

def file_controller(path):
    storage_path = normcase(normpath(settings['application']['storage']))

    if path != '<root>':
        absolute_path = abspath('{0}/{1}'.format(storage_path, path))
    else:
        absolute_path = storage_path

    size = getsize(absolute_path);

    if isdir(absolute_path):
        return render_template('directory_detail.html',
                               name=basename(absolute_path),
                               path=remove_base_folder(absolute_path, storage_path))
    else:
        creation_time = datetime.fromtimestamp(getctime(absolute_path)).strftime('%Y-%m-%d %H:%M:%S')

        return render_template('file_detail.html',
                               name=basename(absolute_path),
                               size=size,
                               size_mb="%.1f" % (size / 1024 / 1024),
                               path=remove_base_folder(absolute_path, storage_path),
                               creation_time=creation_time)


def remove_base_folder(path, base):
    return normcase(normpath(path.replace(base, '').lstrip(sep))).replace('\\', '/')

from os.path import normcase, normpath, sep

from flask import request, jsonify

from index import settings


def file_upload_controller(path):
    storage_path = settings['application']['storage']
    json = {'upload_path': path}

    try:

        if not path:
            json['error'] = True
            json['message'] = 'No path specified for uploading files.'

        else:
            for file_index in request.files:
                file = request.files[file_index]

                if file:
                    absolute_path = format_path("%s\%s\%s" % (storage_path, path, file.filename))
                    file.save(absolute_path)

    except Exception as e:
        json['error'] = True
        json['message'] = '%s' % e

    return jsonify(json)


def format_path(path):
    return normcase(normpath(path.lstrip(sep))).replace('\\', '/')

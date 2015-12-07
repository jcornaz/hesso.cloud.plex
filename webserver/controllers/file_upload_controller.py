from os.path import join

from flask import request, jsonify

from services.PathService import get_absolute_storage_path


def file_upload_controller(path):
    json = {'upload_path': path}

    try:
        if not path:
            json['error'] = True
            json['message'] = 'No path specified for uploading files.'

        else:
            for file_index in request.files:
                file = request.files[file_index]

                if file:
                    absolute_path = get_absolute_storage_path(join(path, file.filename))
                    file.save(absolute_path)

    except Exception as e:
        json['error'] = True
        json['message'] = '%s' % e

    return jsonify(json)

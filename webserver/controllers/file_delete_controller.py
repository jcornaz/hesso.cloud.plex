from os.path import normpath, normcase, isfile
from index import settings

from os import remove


def file_delete_controller(path):
    storage_path = normcase(normpath(settings['application']['storage']))
    absolute_path = "{0}/{1}".format(storage_path, path)

    if not isfile(absolute_path):
        return {'error': True, 'message': "{0} not found.".format(path)}

    remove(absolute_path)

    return {'error': False, 'message': "File {0} successfully deleted.".format(path)}

from os.path import normpath, normcase, isdir
from index import settings

from os import rmdir


def directory_delete_controller(path):
    storage_path = normcase(normpath(settings['application']['storage']))
    absolute_path = "{0}/{1}".format(storage_path, path)

    if not isdir(absolute_path):
        return {'error': True, 'message': "{0} not found.".format(path)}

    rmdir(absolute_path)

    return {'error': False, 'message': "Directory {0} successfully deleted.".format(path)}

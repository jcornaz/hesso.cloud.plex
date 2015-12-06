from index import settings


# Python documentation
# url: https://docs.python.org/2/library/os.path.html

# Join two (or more) paths using unix like path even for Windows.
def join(path, *paths):
    result = format_path(path)

    for p in paths:
        if p:
            result += '/' + format_path(p)

    return result


# Format path for the application use only.
def format_path(path):
    return path.strip('\\').strip('/').replace('\\', '/')


# Get the storage path where medias are.
def get_absolute_storage_path(path = ''):
    storage_path = format_path(settings['application']['storage'])

    if path:
        return join(storage_path, format_path(path.replace('<root>', '')))

    return format_path(storage_path)


def get_relative_storage_path(path):
    storage_path = format_path(settings['application']['storage'])

    result = path.replace(storage_path, '')

    return '/' if not result else result

import yaml
from livereload import Server

import routes

with open('settings.yaml', 'r') as stream:
    settings = yaml.load(stream)

if settings is None:
    raise Exception('Cannot read the settings file.')

if __name__ == '__main__':
    # Production way
    # routes.app.run(settings['application']['host'], debug = settings['application']['debug'])

    # Development way using livereload
    server = Server(routes.app.wsgi_app)
    server.serve(host = 'localhost')

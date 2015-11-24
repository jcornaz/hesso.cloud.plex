import yaml
from livereload import Server

import routes

with open('settings.yaml', 'r') as stream:
    settings = yaml.load(stream)

if settings is None:
    raise Exception('Cannot read the settings file.')

if __name__ == '__main__':
    # routes.app.run(settings['application']['host'], debug = settings['application']['debug'])

    server = Server(routes.app.wsgi_app)
    server.serve(open_url = True, host = 'localhost')

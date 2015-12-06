import yaml

import routes

with open('settings.yaml', 'r') as stream:
    settings = yaml.load(stream)

if settings is None:
    raise Exception('Cannot read the settings file.')

if __name__ == '__main__':
    host = settings['application']['host']
    debug = settings['application']['debug']
    port = settings['application']['port']

    # Production way
    routes.app.run(host, debug = debug, port = port)

    # Development way using livereload
    # server = Server(routes.app.wsgi_app)
    # server.serve(host = 'localhost')

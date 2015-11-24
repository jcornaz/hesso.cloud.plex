import yaml

from routes import app

with open('settings.yaml', 'r') as stream:
    settings = yaml.load(stream)

if settings is None:
    raise Exception('Cannot read the settings file.')

if __name__ == '__main__':
    app.run(settings['application']['host'], debug = settings['application']['debug'])


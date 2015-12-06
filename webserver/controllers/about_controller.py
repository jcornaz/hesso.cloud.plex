import flask

import constants


def about_controller():
    return flask.jsonify({'version': constants.__version__})

import flask

import constants
from json_models import get_main_model


def about_controller():
    array = get_main_model("About")

    array.append(('version', constants.__version__))

    return flask.jsonify(array)

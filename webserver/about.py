import flask
from json_models import get_main_model


def about_controller():
    array = get_main_model(about)

    return flask.jsonify(array)

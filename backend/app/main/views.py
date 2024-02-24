from flask import jsonify, request, make_response
from . import main

@main.route('/')
def index():
    """
        This is the main blueprint
        It contains the routes for the application
        @Author: Hezekiah Elisha
        @Date: 25-01-2024

            @main.route('/')
            def index():
                return 'Hello World!'
        :return: JSON
    """
    return make_response(
        jsonify(
            message = 'Hello World!'
        ),200
    )
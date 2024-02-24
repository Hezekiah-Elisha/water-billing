#!/bin/bash
source venv/bin/activate
export FLASK_APP=billing.py
export FLASK_CONFIG=development
export FLASK_DEBUG=1
flask run --host='0.0.0.0' --port=7000
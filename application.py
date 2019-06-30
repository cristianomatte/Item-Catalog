#!/usr/bin/env python3

import json
from flask import Flask
from views.api import api
from views.web import web
from views.auth import auth


app = Flask(__name__)
app.register_blueprint(api)
app.register_blueprint(web)
app.register_blueprint(auth)

if __name__ == "__main__":
    with open('client_secrets.json', 'r') as file:
        # Read secret key from configuration file
        data = file.read()
        dictionary = json.loads(data)
        app.secret_key = dictionary['app']['secret_key']

    app.run(host="0.0.0.0", port=8000, debug=True)

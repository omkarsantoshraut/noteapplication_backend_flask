from flask import Flask
import requests
import json
from datetime import datetime

from server_auth import auth
from note_operations import note_operation_main

app = Flask(__name__)
auth.Auth()
app.register_blueprint(note_operation_main.noteOperations)

if __name__ == '__main__':
    app.run(debug=True)
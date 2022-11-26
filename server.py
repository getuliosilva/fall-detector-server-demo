"""
This program simulates a REST API that receives fall alerts from a fall sensor used by a person and sends the sensor status to a client that requests it.
For this demonstration, phone.py sends HTTP GET requests to server.py every second. server.py responds with the status object. If sensor.py detects a fall, it sends a HTTP PUT request to server.py, changing fall to True.
"""

"""
Python Flask is a microframework for developing web apps. It serves as our web server.
Python Flask-RESTful is an extension for Flask that adds support for quickly building REST APIs.
"""
from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

"""
The status variable stores the object that indicate if the sensor sent a fall alert.
status = {"fall": False} means a fall alert was NOT received by the server.
status = {"fall": True} means a fall alert WAS received by the server.
"""
status = {"fall": False}

class TodoSimple(Resource):

    """
    The Python get method (server) defines how the server should respond to the HTTP GET method (client). In this case the server just sends the status object to the client.
    """
    def get(self):
        return status

    """
    The Python put method (server) defines how the server should respond to the HTTP PUT method (client). In this case the server gets the request payload and overwrites the status variable to reflect the new sensor state. 'data' is the information sent from the client.
    """
    def put(self):
        status["fall"] = request.form['data']
        return status

api.add_resource(TodoSimple, '/')

if __name__ == '__main__':
    app.run(debug=True)
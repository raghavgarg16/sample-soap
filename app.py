""" Main file to serve the application """

# Python packages
from flask import Flask
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from werkzeug.serving import run_simple

# Main functionality
from services.get_user_service import get_user_wsgi_app
from services.insert_user_service import insert_user_wsgi_app

# Flask app Instance
app = Flask(__name__)

# Combine Flask with the SOAP apps
application = DispatcherMiddleware(app.wsgi_app, {
    '/soap/get_user': get_user_wsgi_app,
    '/soap/insert_user': insert_user_wsgi_app,
})

# Define a simple route for the Flask app
if __name__ == "__main__":
    run_simple('127.0.0.1', 5000, application)

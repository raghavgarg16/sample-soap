""" This file contain the MySQL Connection... """

# Python Packages
import mysql.connector

# App Constants
from base import constants





class Database:
    """ Main Class of Database to connect with your Database... """

    def __init__(self):
        """ Constructor Function - Call Automatically... """

        self.connection = mysql.connector.connect(
            host = constants.DB_HOST,
            database = constants.DB_NAME,
            user = constants.DB_USERNAME,
            password = constants.DB_PASSWORD
        )


    def get_connection(self):
        """ Get Connection with DB..."""

        return self.connection


    def close_connection(self):
        """ Close Connection with DB... """

        if self.connection.is_connected():
            self.connection.close()

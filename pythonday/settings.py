from flask import Flask
import sqlite3


app = Flask(__name__)
app.config['DEBUG'] = False

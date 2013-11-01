from flask import Flask
import sqlite3


app = Flask(__name__)
app.config['DEBUG'] = True

conn = sqlite3.connect('database.db')
# cursor = conn.cursor()
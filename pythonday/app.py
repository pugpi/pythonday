from flask import render_template
from settings import app
import sqlite3
from werkzeug.contrib.fixers import ProxyFix


@app.route('/')
def index():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * from palestrantes')
    palestrantes = cursor.fetchall()
    return render_template('index.html', palestrantes=palestrantes)

app.wsgi_app = ProxyFix(app.wsgi_app)

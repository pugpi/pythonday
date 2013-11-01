from flask import render_template
from settings import app
import sqlite3


@app.route('/')
def index():
    conn = sqlite3.connect('database2.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * from palestrantes')
    palestrantes = cursor.fetchall()
    return render_template('index.html', palestrantes=palestrantes)


if __name__ == '__main__':
    app.run(port=8001)
import sqlite3
from flask import Flask
from flask import render_template, g


#Konstanten werden groß geschrieben!
PATH="db/jobs.sqlite"

#Einfache Definition einer Variable
app = Flask(__name__)


def open_connection():
    connection = getattr(g, '_connection', None)
    if connection == None:
        connection = sqlite3.connect(PATH)
        g._connection = sqlite3.connect(PATH)
    connection.row_factory = sqlite3.Row
    return connection


def execute_sql(sql, values=(), commit=False, single=False):
    connection = open_connection()
    cursor = connection.execute(sql, values)
    if commit is True:
        results = connection.commit()
    else:
        if single:
            results = cursor.fetchone()
        else:
            results = cursor.fetchall()
    cursor.close()
    return results



@app.teardown_appcontext
def close_connection(exception):
    connection = getattr(g, '_connection', None)
    if connection is not None:
        connection.close()

    


@app.route('/')
@app.route('/jobs')
def jobs ():
    return render_template('index.html')


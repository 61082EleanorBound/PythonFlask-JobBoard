import sqlite3
from flask import Flask, render_template, g #g is to help provide access to the database
#  a constant that contains the path to the already created database
PATH = 'db/jobs.sqlite'

#created instance of flask
app = Flask(__name__)

def open_connection(): # new function
    connection = getattr(g,'_connection', None)
    if connection == None:
        connection = g._connection = sqlite3.connect(PATH)
    connection.row_factory = sqlite3.Row #all rows returned from the database will be named tuples
    return connection

def execute_sql(sql, values=(), commit=False, single=False):   # 4 parameters
    connection = open_connection() 
    cursor = connection.exectue(sql, values) # curser = the return value
    if commit == True:
        results = connection.commit()
    else:
        results = cursor.fetchone() if single else curser.fetchall()
    
    cursor.close()
    return results

@app.teardown_appcontext
def close_connection(exception):
    connection = getattr(g, '_connection', None)
    if connection is not None:
        connection.close()
        

@app.route('/')
@app.route('/jobs')
def jobs():
    return render_template('index.html')
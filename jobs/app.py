from flask import Flask, render_template

#created instance of flask by Ellie
app = Flask(__name__)

@app.route('/')
@app.route('/jobs')
def jobs():
    return render_template('index.html')
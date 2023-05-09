from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "<a href='/greet'>Hello Universe!</a>"

@app.route('/greet')
def greet():
    return "<a href='/morning'>How Are You</a>"

@app.route('/morning')
def morning():
    return "<a href='/afternoon'>Good Morning</a>"

@app.route('/afternoon')
def afternoon():
    return "<a href='/evening'>Good Afternoon</a>"

@app.route('/evening')
def evening():
    return "<a href='goodnight'>Good Evening</a>"

@app.route('/goodnight')
def goodnight():
    return "<a href='rip'>Good Night</a>"

@app.route('/rip')
def rip():
    return "<p>rest in peace</p>"


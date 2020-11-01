from flask import Flask, make_response
app = Flask("api")

@app.route('/hello')
def hello():
    return 'Hello, World'
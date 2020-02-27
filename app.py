from flask import render_template, session, redirect, url_for, request
from settings import app, db


@app.route('/index')
@app.route('/')
def index():
    return "Hello world"

if __name__ == '__main__':
    db.create_all()
    app.debug = True 
    app.run(threaded=True, port=5000, debug=True)


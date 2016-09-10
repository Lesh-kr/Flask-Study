from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash
from flask.ext.sqlalchemy import SQLAlchemy
from contextlib import closing

app = Flask(__name__)
app.config.from_pyfile('config.py')
db = SQLAlchemy(app)

@app.route('/')
def main():
    return render_template('main.html')

@app.route('/notepad/')
def notepad():
    return render_template('render_note.html')

@app.route('/notepadHandler', methods=['POST'])
def notepadHandler():
    return redirect(url_for('notepad'))

if __name__ == '__main__':
    app.run()

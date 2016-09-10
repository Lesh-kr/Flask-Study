from flask import Flask, render_template, redirect, url_for
from flaskr import app
from flaskr.models import Note

@app.route('/')
def main():
    return render_template('main.html')

@app.route('/notepad/')
def notepad():
    return render_template('render_note.html')

@app.route('/notepadHandler', methods=['POST'])
def notepadHandler():
    return redirect(url_for('notepad'))


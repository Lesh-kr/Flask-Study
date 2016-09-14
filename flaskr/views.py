from flask import Flask, render_template, redirect, url_for, jsonify
from flaskr import app
from flaskr.models import Note

def serialize(note):
    return {'id': note.id, 'title': note.title, 'body': note.body}

@app.route('/')
def main():
    return render_template('main.html')

@app.route('/notepad/')
def notepad():
    return render_template('render_note.html')

@app.route('/notepadHandler', methods=['POST'])
def notepadHandler():
    return redirect(url_for('notepad'))

@app.route('/api/notes')
def all_notes():
    count = Note.query.count()
    notes = Note.query.all()
    result = []
    for note in notes:
        serialized_note = serialize(note)
        result.append(serialized_note)
    return jsonify(total_count=count, notes=result)

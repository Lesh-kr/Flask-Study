from flaskr import db

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(20))
    body = db.Column(db.String(255))

    def __init__(self, title, body):
        self.title = title
        self.body = body

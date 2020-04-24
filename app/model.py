from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(127))
    password = db.Column(db.String(127))

    def __init__(self, username, password):
        self.username = username
        self.password = password




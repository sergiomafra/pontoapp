from ..pontoapp import db


class User:
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), nullable=False)
    password = db.Column(db.String(128), nullalble=False)

    def __repr__(self):
        return f'<User {self.username}>'

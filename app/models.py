from app import db


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), unique=True, nullable=False)
    password = db.Column(db.String(64), nullable=False)

    def __init__(self, username, password):
        self.username = username

    def __repr__(self):
        return f'<User {self.username}>'

class Ponto(db.Model):
    ''' ponto model '''

    __tablename__ = 'ponto'

    id = db.Column(db.Integer, primary_key=True)
    uid = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    date = db.Column(db.Date, nullable=False)
    hour1 = db.Column(db.Time)
    hour2 = db.Column(db.Time)
    hour3 = db.Column(db.Time)
    hour4 = db.Column(db.Time)
    picture = db.Column(db.Time, nullable=False)
    absence_reason = db.Column(db.String(64))
    notes = db.Column(db.String(300))

    def __init__(self, id, uid, date, hour1, hour2, hour3, hour4, picture, \
        absence_reason, notes):

        self.id = id
        self.uid = uid
        self.date = date
        self.hour1 = hour1
        self.hour2 = hour2
        self.hour3 = hour3
        self.hour4 = hour4
        self.picture = picture
        self.absence_reason = absence_reason
        self.notes = notes

    def __repr__(self):
        print(f'<Ponto info for user {self.username} on {self.date}>')

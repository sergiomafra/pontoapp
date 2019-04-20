from app import db


class Ponto(db.Model):

    __tablename__ = 'ponto'

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column()
    hour1 = db.Column
    hour2 = db.Column
    hour3 = db.Column
    hour4 = db.Column
    picture = db.Column
    absence_reason = db.Column
    notes = db.Column

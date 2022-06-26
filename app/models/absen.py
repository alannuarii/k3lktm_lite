from app import db

class Absen(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nama = db.Column(db.String(80), nullable=False)
    instansi = db.Column(db.String(100), nullable=False)
    telepon = db.Column(db.String(20), nullable=False)
    foto = db.Column(db.String(255), nullable=True)

    def __repr__(self):
        return '<{}. {} ({})>'.format(self.id, self.nama)
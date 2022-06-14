import datetime
from app import db
import datetime

class Guestbook(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    tanggal = db.Column(db.String(30), default=datetime.datetime.now().strftime('%d %B %Y, %H:%M:%S'))
    nama = db.Column(db.String(80), nullable=False)
    instansi = db.Column(db.String(100), nullable=False)
    alamat = db.Column(db.String(150), nullable=False)
    telepon = db.Column(db.String(20), nullable=False)
    tujuan = db.Column(db.String(250), nullable=False)
    foto = db.Column(db.String(255), nullable=True)

    def __repr__(self):
        return '<{}. {} ({})>'.format(self.id, self.nama, self.tanggal)
from app import db

class PHProses(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    ph = db.Column(db.Float, nullable=False)
    tanggal = db.Column(db.String(30), nullable=False)
    bulan = db.Column(db.String(10), nullable=False)

    def __repr__(self):
        return '<{}. {} = {}>'.format(self.id, self.tanggal, self.ph)
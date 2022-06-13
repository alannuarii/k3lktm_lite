from app import db

class OliBekas(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    tanggal = db.Column(db.String(30), nullable=False)
    masuk = db.Column(db.Float, nullable=True)
    keluar = db.Column(db.Float, nullable=True)
    manifest = db.Column(db.String(100), nullable=True)

    def __repr__(self):
        return '<{}. {}>'.format(self.id, self.tanggal)
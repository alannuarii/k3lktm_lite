from app import db
import datetime

class WorkingPermit(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    tanggal = db.Column(db.String(30), nullable=False)
    jenis_pekerjaan = db.Column(db.String(150), nullable=False)
    detail_pekerjaan = db.Column(db.String(150), nullable=False)
    lokasi = db.Column(db.String(50), nullable=False)
    nama_pengawas_pekerjaan = db.Column(db.String(50), nullable=False)
    nomor_pengawas_pekerjaan = db.Column(db.String(50), nullable=False)
    tanggal_mulai = db.Column(db.String(30), nullable=False)
    tanggal_selesai = db.Column(db.String(30), nullable=False)
    jam_mulai = db.Column(db.String(20), nullable=False)
    jam_selesai = db.Column(db.String(20), nullable=False)
    klasifikasi = db.Column(db.Text, nullable=False)
    prosedur = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.datetime.now())

    def __repr__(self):
        return '<{} ({})>'.format(self.jenis_pekerjaan, self.tanggal)


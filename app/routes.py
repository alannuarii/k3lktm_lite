from datetime import datetime, timedelta
from app import app
from app import db
from flask import render_template, request, redirect, url_for, flash
from app.models.lb3 import LB3
from app.models.sludge import Sludge
from app.models.oli_bekas import OliBekas
from app.models.filter_bekas import FilterBekas
from app.models.majun_bekas import MajunBekas
from app.models.debit_proses import DebitProses
from app.models.ph_proses import PHProses
from app.models.debit_domestik import DebitDomestik
from app.models.ph_domestik import PHDomestik
from app.models.guestbook import Guestbook
from app.models.working_permit import WorkingPermit
from app.models.user import User
from PIL import Image
from io import BytesIO
from werkzeug.utils import secure_filename
from werkzeug.urls import url_parse
from googletrans import Translator
from flask_login import current_user, login_user, logout_user, login_required
import os
import base64
import socket


@app.route('/login', methods=['GET','POST'])
def login():
    tahun = datetime.now().strftime('%Y')

    if current_user.is_authenticated:
        return redirect(url_for('index'))

    if request.method=='POST':
        email = request.form['email']
        password = request.form['password']
        user = User.query.filter_by(email=email).first()

        if not user:
            flash('Anda memasukkan email yang salah')
            return redirect(url_for('login'))
        if not user.checkPassword(password):
            flash('Anda memasukkan password yang salah')
            return redirect(url_for('login'))

        login_user(user)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)

    return render_template('pages/login.html', title='Login | K3L KTM', tahun=tahun)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route('/')
@login_required
def index():
    hostname = socket.gethostname()
    ip = str(socket.gethostbyname(hostname))
    today = datetime.now().strftime('%A, %d %B %Y')
    today_1 = datetime.now().strftime('%d %B %Y')
    guests = Guestbook.query.filter(Guestbook.tanggal.like(today_1+'%')).all()
    # name = 'Aurelia Bilqis Azzahra'
    # email = 'aura@alan.web.id'
    # password = 'admin'
    # level = 2
    # admin = User(name=name, email=email, level=level)
    # admin.setPassword(password)
    # db.session.add(admin)
    # db.session.commit()
    return render_template('pages/home.html', title='Home | K3L KTM', active_home='active', ip = ip, today=today, guests=guests, today_1=today_1)


@app.route('/lb3-converter')
@login_required
def lb3():
    list_lb3 = LB3.query.all()
    list_nilai_satuan = []
    satuan = []
    for i in range(len(list_lb3)):
        list_nilai_satuan.append(list_lb3[i].nilai_satuan)
        satuan.append(list_lb3[i].satuan)

    return render_template('pages/lb3-converter.html', title='LB3 Converter | K3L KTM', active_lb3='active', list_lb3 = list_lb3, list_nilai_satuan = list_nilai_satuan, satuan = satuan)


@app.route('/logbook')
@login_required
def logbook():

    return render_template('pages/logbook.html', title='LogBook | K3L KTM', active_logbook='active')


@app.route('/logbook/limbah-domestik/debit')
@login_required
def debit_domestik():
    query = request.args.get('bulan')
    debit = DebitDomestik.query.filter_by(bulan=query).all()
    if query:
        query_datetime = datetime.strptime(query, '%Y-%m')
        bulan = query_datetime.strftime('%B')
        tahun = query_datetime.strftime('%Y')
        result = Translator().translate(bulan, src='en', dest='id')
        return render_template('pages/debit-domestik.html', title='Debit Limbah Domestik | K3L KTM', active_logbook='active', debits=debit, bulan=result.text, tahun=tahun)
    return render_template('pages/debit-domestik.html', title='Debit Limbah Domestik | K3L KTM', active_logbook='active', debits=debit)


@app.route('/logbook/limbah-domestik/ph')
@login_required
def ph_domestik():
    query = request.args.get('bulan')
    ph = PHDomestik.query.filter_by(bulan=query).all()
    if query:
        query_datetime = datetime.strptime(query, '%Y-%m')
        bulan = query_datetime.strftime('%B')
        tahun = query_datetime.strftime('%Y')
        result = Translator().translate(bulan, src='en', dest='id')
        return render_template('pages/ph-domestik.html', title='ph Limbah Domestik | K3L KTM', active_logbook='active', phs=ph, bulan=result.text, tahun=tahun)
    return render_template('pages/ph-domestik.html', title='ph Limbah Domestik | K3L KTM', active_logbook='active', phs=ph)


@app.route('/logbook/limbah-proses/debit')
@login_required
def debit_proses():
    query = request.args.get('bulan')
    debit = DebitProses.query.filter_by(bulan=query).all()
    if query:
        query_datetime = datetime.strptime(query, '%Y-%m')
        bulan = query_datetime.strftime('%B')
        tahun = query_datetime.strftime('%Y')
        result = Translator().translate(bulan, src='en', dest='id')
        return render_template('pages/debit-proses.html', title='Debit Limbah Proses | K3L KTM', active_logbook='active', debits=debit, bulan=result.text, tahun=tahun)
    return render_template('pages/debit-proses.html', title='Debit Limbah Proses | K3L KTM', active_logbook='active', debits=debit)


@app.route('/logbook/limbah-proses/ph')
@login_required
def ph_proses():
    query = request.args.get('bulan')
    ph = PHProses.query.filter_by(bulan=query).all()
    if query:
        query_datetime = datetime.strptime(query, '%Y-%m')
        bulan = query_datetime.strftime('%B')
        tahun = query_datetime.strftime('%Y')
        result = Translator().translate(bulan, src='en', dest='id')
        return render_template('pages/ph-proses.html', title='ph Limbah Proses | K3L KTM', active_logbook='active', phs=ph, bulan=result.text, tahun=tahun)
    return render_template('pages/ph-proses.html', title='ph Limbah Proses | K3L KTM', active_logbook='active', phs=ph)


@app.route('/logbook/input-ppa', methods=['GET', 'POST'])
@login_required
def input_ppa():
    if request.method == 'POST':
        if request.form['ppa'] == 'debitproses':
            tanggal = request.form['tanggal']
            debit = request.form['debit']
            bulan = request.form['bulan'][:7]
            debitproses = DebitProses(tanggal=tanggal, debit=debit, bulan=bulan)
            db.session.add(debitproses)
            db.session.commit()
            return redirect(url_for('debit_proses'))
        elif request.form['ppa'] == 'phproses':
            tanggal = request.form['tanggal']
            ph = request.form['ph']
            bulan = request.form['bulan'][:7]
            phproses = PHProses(tanggal=tanggal, ph=ph, bulan=bulan)
            db.session.add(phproses)
            db.session.commit()
            return redirect(url_for('ph_proses'))
        elif request.form['ppa'] == 'debitdomestik':
            tanggal = request.form['tanggal']
            debit = request.form['debit']
            bulan = request.form['bulan'][:7]
            debitdomestik = DebitDomestik(tanggal=tanggal, debit=debit, bulan=bulan)
            db.session.add(debitdomestik)
            db.session.commit()
            return redirect(url_for('debit_domestik'))
        elif request.form['ppa'] == 'phdomestik':
            tanggal = request.form['tanggal']
            ph = request.form['ph']
            bulan = request.form['bulan'][:7]
            phdomestik = PHDomestik(tanggal=tanggal, ph=ph, bulan=bulan)
            db.session.add(phdomestik)
            db.session.commit()
            return redirect(url_for('ph_domestik'))
    return render_template('pages/input-ppa.html', title='Input Data Harian | K3L KTM', active_logbook='active')


@app.route('/logbook/sludge', methods=['GET', 'POST'])
@login_required
def sludge():
    list_sludge = Sludge.query.all()
    if request.method == 'POST':
        if request.files:
            tanggal = request.form['tanggal']
            keluar = request.form['keluar']
            manifest = request.files['manifest']
            filename = secure_filename(manifest.filename)
            renamefile = 'Sludge-'+filename
            manifest.save(os.path.join(app.config['UPLOAD_FOLDER'], renamefile))
            sludge = Sludge(tanggal=tanggal, keluar=keluar, manifest=renamefile)
            db.session.add(sludge)
            db.session.commit()
            return redirect(url_for('sludge'))
        else:
            tanggal = request.form['tanggal']
            masuk = request.form['masuk'] 
            sludge = Sludge(tanggal=tanggal, masuk=masuk)
            db.session.add(sludge)
            db.session.commit()
            return redirect(url_for('sludge'))
    return render_template('pages/sludge.html', title='Sludge | K3L KTM', active_logbook='active', sludges=list_sludge)


@app.route('/logbook/oli-bekas', methods=['GET', 'POST'])
@login_required
def oli_bekas():
    list_oli_bekas = OliBekas.query.all()
    if request.method == 'POST':
        if request.files:
            tanggal = request.form['tanggal']
            keluar = float(request.form['keluar']) 
            manifest = request.files['manifest']
            filename = secure_filename(manifest.filename)
            renamefile = 'OliBekas-'+filename
            manifest.save(os.path.join(app.config['UPLOAD_FOLDER'], renamefile))
            oli_bekas = OliBekas(tanggal=tanggal, keluar=keluar, manifest=renamefile)
            db.session.add(oli_bekas)
            db.session.commit()
            return redirect(url_for('oli_bekas'))
        else:
            tanggal = request.form['tanggal']
            masuk = float(request.form['masuk']) 
            oli_bekas = OliBekas(tanggal=tanggal, masuk=masuk)
            db.session.add(oli_bekas)
            db.session.commit()
            return redirect(url_for('oli_bekas'))
    return render_template('pages/oli-bekas.html', title='Oli Bekas | K3L KTM', active_logbook='active', oli_bekas=list_oli_bekas)


@app.route('/logbook/filter-bekas', methods=['GET', 'POST'])
@login_required
def filter_bekas():
    list_filter_bekas = FilterBekas.query.all()
    if request.method == 'POST':
        if request.files:
            tanggal = request.form['tanggal']
            keluar = float(request.form['keluar']) 
            manifest = request.files['manifest']
            filename = secure_filename(manifest.filename)
            renamefile = 'FilterBekas-'+filename
            manifest.save(os.path.join(app.config['UPLOAD_FOLDER'], renamefile))
            filter_bekas = FilterBekas(tanggal=tanggal, keluar=keluar, manifest=renamefile)
            db.session.add(filter_bekas)
            db.session.commit()
            return redirect(url_for('filter_bekas'))
        else:
            tanggal = request.form['tanggal']
            masuk = float(request.form['masuk']) 
            filter_bekas = FilterBekas(tanggal=tanggal, masuk=masuk)
            db.session.add(filter_bekas)
            db.session.commit()
            return redirect(url_for('filter_bekas'))
    return render_template('pages/filter-bekas.html', title='Filter Bekas | K3L KTM', active_logbook='active', filter_bekas=list_filter_bekas)


@app.route('/logbook/majun-bekas', methods=['GET', 'POST'])
@login_required
def majun_bekas():
    list_majun_bekas = MajunBekas.query.all()
    if request.method == 'POST':
        if request.files:
            tanggal = request.form['tanggal']
            keluar = float(request.form['keluar']) 
            manifest = request.files['manifest']
            filename = secure_filename(manifest.filename)
            renamefile = 'MajunBekas-'+filename
            manifest.save(os.path.join(app.config['UPLOAD_FOLDER'], renamefile))
            majun_bekas = MajunBekas(tanggal=tanggal, keluar=keluar, manifest=renamefile)
            db.session.add(majun_bekas)
            db.session.commit()
            return redirect(url_for('majun_bekas'))
        else:
            tanggal = request.form['tanggal']
            masuk = float(request.form['masuk']) 
            majun_bekas = MajunBekas(tanggal=tanggal, masuk=masuk)
            db.session.add(majun_bekas)
            db.session.commit()
            return redirect(url_for('majun_bekas'))
    return render_template('pages/majun-bekas.html', title='Majun Bekas | K3L KTM', active_logbook='active', majun_bekas=list_majun_bekas)


@app.route('/guestbook/input', methods=['GET','POST'])
def input_tamu():
    if request.method == 'POST':
        nama = request.form['nama']
        instansi = request.form['instansi']
        alamat = request.form['alamat']
        telepon = request.form['telepon']
        tujuan = request.form['tujuan']
        foto = request.form['foto']
        new_foto = foto.replace('data:image/jpeg;base64,', '')
        bytes_decoded = base64.b64decode(new_foto)
        img = Image.open(BytesIO(bytes_decoded))
        out_jpg = img.convert("RGB")

        # Random Name 
        now = datetime.now()
        microsecond = now.strftime('%f')  
        filename = 'Tamu-'+microsecond+'.jpg'


        out_jpg.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        guestbook = Guestbook(nama=nama, instansi=instansi, alamat=alamat, telepon=telepon, tujuan=tujuan, foto=filename)
        db.session.add(guestbook)
        db.session.commit()
        return redirect(url_for('m_home'))
    return render_template('pages/input-tamu.html',title='Guest Book | K3L KTM', active_guestbook='active')


@app.route('/guestbook')
@login_required
def guestbook():
    list_guestbook = Guestbook.query.all()
    return render_template('pages/guestbook.html',title='Guest Book | K3L KTM', active_guestbook='active', guests=list_guestbook)


@app.route('/working-permit', methods=['GET','POST'])
@login_required
def working_permit():
    if request.method == 'POST':
        tanggal = request.form['tanggal']
        jenis_pekerjaan = request.form['jenis_pekerjaan']
        detail_pekerjaan = request.form['detail_pekerjaan']
        lokasi = request.form['lokasi']
        nama_pengawas_pekerjaan = request.form['nama_pengawas_pekerjaan']
        nomor_pengawas_pekerjaan = request.form['nomor_pengawas_pekerjaan']
        tanggal_mulai = request.form['tanggal_mulai']
        tanggal_selesai = request.form['tanggal_selesai']
        jam_mulai = request.form['jam_mulai']
        jam_selesai = request.form['jam_selesai']
        klasifikasi = str(request.form.getlist('klasifikasi'))
        prosedur = str(request.form.getlist('prosedur'))
        workingpermit = WorkingPermit(tanggal=tanggal, jenis_pekerjaan=jenis_pekerjaan, detail_pekerjaan=detail_pekerjaan, lokasi=lokasi, nama_pengawas_pekerjaan=nama_pengawas_pekerjaan, nomor_pengawas_pekerjaan=nomor_pengawas_pekerjaan, tanggal_mulai=tanggal_mulai, tanggal_selesai=tanggal_selesai, jam_mulai=jam_mulai, jam_selesai=jam_selesai, klasifikasi=klasifikasi, prosedur=prosedur)
        db.session.add(workingpermit)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('pages/working-permit.html',title='Working Permit | K3L KTM', active_wp='active')


@app.route('/safety-induction')
def safety_induction():
    return render_template('pages/safety-induction.html',title='Safety Induction | K3L KTM', active_si='active')


# Halaman Mobile 
@app.route('/m-home')
def m_home():
    return render_template('pages/m-home.html',title='Home | K3L KTM')



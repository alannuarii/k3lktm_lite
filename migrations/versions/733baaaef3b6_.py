"""empty message

Revision ID: 733baaaef3b6
Revises: 
Create Date: 2022-06-13 19:50:39.352567

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '733baaaef3b6'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('debit_domestik',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('debit', sa.Float(), nullable=False),
    sa.Column('tanggal', sa.String(length=30), nullable=False),
    sa.Column('bulan', sa.String(length=10), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('debit_proses',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('debit', sa.Float(), nullable=False),
    sa.Column('tanggal', sa.String(length=30), nullable=False),
    sa.Column('bulan', sa.String(length=10), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('filter_bekas',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('tanggal', sa.String(length=30), nullable=False),
    sa.Column('masuk', sa.Float(), nullable=True),
    sa.Column('keluar', sa.Float(), nullable=True),
    sa.Column('manifest', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('guestbook',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('tanggal', sa.DateTime(), nullable=True),
    sa.Column('nama', sa.String(length=80), nullable=False),
    sa.Column('instansi', sa.String(length=100), nullable=False),
    sa.Column('alamat', sa.String(length=150), nullable=False),
    sa.Column('telepon', sa.String(length=20), nullable=False),
    sa.Column('tujuan', sa.String(length=250), nullable=False),
    sa.Column('foto', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('l_b3',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('jenis_limbah', sa.String(length=250), nullable=False),
    sa.Column('nilai_satuan', sa.Float(), nullable=False),
    sa.Column('satuan', sa.String(length=60), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('majun_bekas',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('tanggal', sa.String(length=30), nullable=False),
    sa.Column('masuk', sa.Float(), nullable=True),
    sa.Column('keluar', sa.Float(), nullable=True),
    sa.Column('manifest', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('oli_bekas',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('tanggal', sa.String(length=30), nullable=False),
    sa.Column('masuk', sa.Float(), nullable=True),
    sa.Column('keluar', sa.Float(), nullable=True),
    sa.Column('manifest', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('ph_domestik',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('ph', sa.Float(), nullable=False),
    sa.Column('tanggal', sa.String(length=30), nullable=False),
    sa.Column('bulan', sa.String(length=10), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('ph_proses',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('ph', sa.Float(), nullable=False),
    sa.Column('tanggal', sa.String(length=30), nullable=False),
    sa.Column('bulan', sa.String(length=10), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('sludge',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('tanggal', sa.String(length=30), nullable=False),
    sa.Column('masuk', sa.Float(), nullable=True),
    sa.Column('keluar', sa.Float(), nullable=True),
    sa.Column('manifest', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=250), nullable=False),
    sa.Column('email', sa.String(length=60), nullable=False),
    sa.Column('password', sa.String(length=250), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('update_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_email'), 'user', ['email'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_user_email'), table_name='user')
    op.drop_table('user')
    op.drop_table('sludge')
    op.drop_table('ph_proses')
    op.drop_table('ph_domestik')
    op.drop_table('oli_bekas')
    op.drop_table('majun_bekas')
    op.drop_table('l_b3')
    op.drop_table('guestbook')
    op.drop_table('filter_bekas')
    op.drop_table('debit_proses')
    op.drop_table('debit_domestik')
    # ### end Alembic commands ###

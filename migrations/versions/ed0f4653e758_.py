"""empty message

Revision ID: ed0f4653e758
Revises: 39f35b08584a
Create Date: 2022-06-21 20:31:37.221200

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ed0f4653e758'
down_revision = '39f35b08584a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('level', sa.Integer(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'level')
    # ### end Alembic commands ###

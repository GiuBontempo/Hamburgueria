"""empty message

Revision ID: 041172383de8
Revises: a4a1a1ebb875
Create Date: 2022-01-27 22:33:10.207723

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '041172383de8'
down_revision = 'a4a1a1ebb875'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('funcionario', sa.Column('senha_hash', sa.String(length=70), nullable=False))
    op.drop_column('funcionario', 'senha')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('funcionario', sa.Column('senha', sa.VARCHAR(length=70), nullable=False))
    op.drop_column('funcionario', 'senha_hash')
    # ### end Alembic commands ###

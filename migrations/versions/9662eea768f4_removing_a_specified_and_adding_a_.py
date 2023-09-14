"""Removing a specified and adding a constraint

Revision ID: 9662eea768f4
Revises: 9d472b37e5e2
Create Date: 2023-09-14 14:03:39.974020

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9662eea768f4'
down_revision = '9d472b37e5e2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('account', schema=None) as batch_op:
        batch_op.alter_column('account_pin',
               existing_type=sa.VARCHAR(length=4),
               nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('account', schema=None) as batch_op:
        batch_op.alter_column('account_pin',
               existing_type=sa.VARCHAR(length=4),
               nullable=True)

    # ### end Alembic commands ###

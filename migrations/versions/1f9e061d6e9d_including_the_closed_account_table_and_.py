"""Including the closed account table and a column in account for status

Revision ID: 1f9e061d6e9d
Revises: 4db5960bc5af
Create Date: 2023-09-29 08:06:54.486416

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1f9e061d6e9d'
down_revision = '4db5960bc5af'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('closed_accounts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('acc_num', sa.String(length=15), nullable=False),
    sa.Column('acc_pin', sa.String(length=4), nullable=False),
    sa.Column('cus_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('acc_balance', sa.Integer(), nullable=True),
    sa.Column('date_closed', sa.DateTime(), nullable=True),
    sa.Column('acc_type', sa.String(length=240), nullable=True),
    sa.Column('bank_name', sa.String(length=240), nullable=False),
    sa.Column('date_acc_created', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['cus_id'], ['customer.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('account', schema=None) as batch_op:
        batch_op.add_column(sa.Column('status', sa.String(length=10), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('account', schema=None) as batch_op:
        batch_op.drop_column('status')

    op.drop_table('closed_accounts')
    # ### end Alembic commands ###

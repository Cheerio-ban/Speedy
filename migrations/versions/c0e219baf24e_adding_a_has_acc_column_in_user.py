"""Adding a has_acc column in user

Revision ID: c0e219baf24e
Revises: 11a7006d75eb
Create Date: 2023-09-15 17:49:56.594730

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c0e219baf24e'
down_revision = '11a7006d75eb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('has_acc',
               existing_type=sa.INTEGER(),
               nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('has_acc',
               existing_type=sa.INTEGER(),
               nullable=True)

    # ### end Alembic commands ###

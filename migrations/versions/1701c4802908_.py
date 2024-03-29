"""empty message

Revision ID: 1701c4802908
Revises: 60e1f1eaa7e7
Create Date: 2022-02-03 19:41:08.125103

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1701c4802908'
down_revision = '60e1f1eaa7e7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('question', schema=None) as batch_op:
        batch_op.alter_column('user_id',
               existing_type=sa.INTEGER(),
               nullable=False,
               existing_server_default=sa.text("'1'"))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('question', schema=None) as batch_op:
        batch_op.alter_column('user_id',
               existing_type=sa.INTEGER(),
               nullable=True,
               existing_server_default=sa.text("'1'"))

    # ### end Alembic commands ###

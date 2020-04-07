"""Added initial tables

Revision ID: fee3accad270
Revises: 687b719d2637
Create Date: 2020-04-06 19:24:01.985027

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'fee3accad270'
down_revision = '687b719d2637'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('tbl_user', 'update_time')
    op.drop_column('tbl_user', 'create_time')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tbl_user', sa.Column('create_time', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True))
    op.add_column('tbl_user', sa.Column('update_time', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True))
    # ### end Alembic commands ###

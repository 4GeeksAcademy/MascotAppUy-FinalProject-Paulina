"""empty message

Revision ID: 0eeeec6f719c
Revises: 750715863bf6
Create Date: 2024-08-15 18:18:23.057818

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0eeeec6f719c'
down_revision = '750715863bf6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('mascota', schema=None) as batch_op:
        batch_op.add_column(sa.Column('coord_x', sa.Numeric(precision=3, scale=6), nullable=True))
        batch_op.add_column(sa.Column('coord_y', sa.Numeric(precision=3, scale=6), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('mascota', schema=None) as batch_op:
        batch_op.drop_column('coord_y')
        batch_op.drop_column('coord_x')

    # ### end Alembic commands ###

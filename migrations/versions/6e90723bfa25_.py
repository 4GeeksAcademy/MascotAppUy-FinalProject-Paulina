"""empty message

Revision ID: 6e90723bfa25
Revises: 49533eefd2f2
Create Date: 2024-08-09 15:04:13.024706

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6e90723bfa25'
down_revision = '49533eefd2f2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('especie', schema=None) as batch_op:
        batch_op.alter_column('name',
               existing_type=sa.VARCHAR(length=25),
               type_=sa.String(length=50),
               existing_nullable=False)

    with op.batch_alter_table('raza', schema=None) as batch_op:
        batch_op.alter_column('name',
               existing_type=sa.VARCHAR(length=25),
               type_=sa.String(length=100),
               existing_nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('raza', schema=None) as batch_op:
        batch_op.alter_column('name',
               existing_type=sa.String(length=100),
               type_=sa.VARCHAR(length=25),
               existing_nullable=False)

    with op.batch_alter_table('especie', schema=None) as batch_op:
        batch_op.alter_column('name',
               existing_type=sa.String(length=50),
               type_=sa.VARCHAR(length=25),
               existing_nullable=False)

    # ### end Alembic commands ###

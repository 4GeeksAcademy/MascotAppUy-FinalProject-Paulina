"""empty message

Revision ID: 107dd970fac0
Revises: 
Create Date: 2024-08-28 12:29:24.633651

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '107dd970fac0'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('color',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=25), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('departamento',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=25), nullable=False),
    sa.Column('coord_x', sa.Numeric(precision=10, scale=6), nullable=True),
    sa.Column('coord_y', sa.Numeric(precision=10, scale=6), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('especie',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('favorito',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('localidad',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('departamento_id', sa.Integer(), nullable=False),
    sa.Column('coord_x', sa.Numeric(precision=10, scale=6), nullable=True),
    sa.Column('coord_y', sa.Numeric(precision=10, scale=6), nullable=True),
    sa.ForeignKeyConstraint(['departamento_id'], ['departamento.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('raza',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('especie_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['especie_id'], ['especie.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('password', sa.String(length=200), nullable=False),
    sa.Column('nombre', sa.String(length=50), nullable=False),
    sa.Column('fecha_registro', sa.Date(), nullable=True),
    sa.Column('telefono', sa.String(length=25), nullable=True),
    sa.Column('url_image', sa.String(length=250), nullable=True),
    sa.Column('is_active', sa.Boolean(), nullable=False),
    sa.Column('favorito_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['favorito_id'], ['favorito.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('mascota',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=120), nullable=False),
    sa.Column('edad', sa.String(length=120), nullable=True),
    sa.Column('sexo', sa.Enum('MACHO', 'HEMBRA', 'INDEFINIDO', name='sexo'), nullable=False),
    sa.Column('descripcion', sa.String(length=250), nullable=False),
    sa.Column('estado', sa.Enum('PERDIDO', 'ENCONTRADO', 'ADOPCION', 'REUNIDO', name='estado'), nullable=False),
    sa.Column('fecha_registro', sa.Date(), nullable=True),
    sa.Column('fecha_perdido', sa.Date(), nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('especie_id', sa.Integer(), nullable=False),
    sa.Column('localidad_id', sa.Integer(), nullable=False),
    sa.Column('raza_id', sa.Integer(), nullable=False),
    sa.Column('departamento_id', sa.Integer(), nullable=False),
    sa.Column('favorito_id', sa.Integer(), nullable=True),
    sa.Column('url_image', sa.String(length=250), nullable=True),
    sa.Column('coord_x', sa.Numeric(precision=10, scale=6), nullable=True),
    sa.Column('coord_y', sa.Numeric(precision=10, scale=6), nullable=True),
    sa.ForeignKeyConstraint(['departamento_id'], ['departamento.id'], ),
    sa.ForeignKeyConstraint(['especie_id'], ['especie.id'], ),
    sa.ForeignKeyConstraint(['favorito_id'], ['favorito.id'], ),
    sa.ForeignKeyConstraint(['localidad_id'], ['localidad.id'], ),
    sa.ForeignKeyConstraint(['raza_id'], ['raza.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('colores_mascotas',
    sa.Column('mascota_id', sa.Integer(), nullable=False),
    sa.Column('color_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['color_id'], ['color.id'], ),
    sa.ForeignKeyConstraint(['mascota_id'], ['mascota.id'], ),
    sa.PrimaryKeyConstraint('mascota_id', 'color_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('colores_mascotas')
    op.drop_table('mascota')
    op.drop_table('user')
    op.drop_table('raza')
    op.drop_table('localidad')
    op.drop_table('favorito')
    op.drop_table('especie')
    op.drop_table('departamento')
    op.drop_table('color')
    # ### end Alembic commands ###

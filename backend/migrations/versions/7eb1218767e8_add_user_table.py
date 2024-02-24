"""Add user table

Revision ID: 7eb1218767e8
Revises: 
Create Date: 2024-01-26 12:56:38.955222

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7eb1218767e8'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=80), nullable=False),
    sa.Column('full_name', sa.String(length=80), nullable=False),
    sa.Column('password', sa.String(length=128), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('role', sa.String(length=80), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=False),
    sa.Column('updated_at', sa.DateTime(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    # ### end Alembic commands ###

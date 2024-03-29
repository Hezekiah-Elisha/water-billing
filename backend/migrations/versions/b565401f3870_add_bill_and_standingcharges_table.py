"""Add Bill and StandingCharges table

Revision ID: b565401f3870
Revises: 7e326db9b981
Create Date: 2024-01-29 15:54:03.368925

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b565401f3870'
down_revision = '7e326db9b981'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('standing_charges',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('water_rent', sa.Float(), nullable=False),
    sa.Column('sewerage_rent', sa.Float(), nullable=False),
    sa.Column('consumption_charges', sa.Float(), nullable=False),
    sa.Column('billing_date', sa.DateTime(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('standing_charges')
    # ### end Alembic commands ###

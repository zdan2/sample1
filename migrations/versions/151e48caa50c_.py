"""empty message

Revision ID: 151e48caa50c
Revises: 
Create Date: 2025-03-20 12:52:54.400176

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '151e48caa50c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    # ### end Alembic commands ###

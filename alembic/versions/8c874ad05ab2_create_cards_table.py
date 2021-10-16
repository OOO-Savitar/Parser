"""create Cards  table

Revision ID: 8c874ad05ab2
Revises: 
Create Date: 2021-10-16 14:46:52.485959

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8c874ad05ab2'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'Cards',
        sa.Column('title', sa.Integer)
    )


def downgrade():
    pass

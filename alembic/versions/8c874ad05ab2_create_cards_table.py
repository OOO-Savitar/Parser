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
        'Cards_1',
        sa.Column('id', sa.Integer),
        sa.Column('title', sa.String(512)),
        sa.Column('price', sa.Integer),
        sa.Column('property_1', sa.String(512)),
        sa.Column('image_link', sa.String(512)),
        sa.Column('prod_link', sa.String(512))
    )


def downgrade():
    pass

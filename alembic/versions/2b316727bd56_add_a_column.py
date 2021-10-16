"""Add a column

Revision ID: 2b316727bd56
Revises: 8c874ad05ab2
Create Date: 2021-10-16 16:07:34.741979

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2b316727bd56'
down_revision = '8c874ad05ab2'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('Cards_1', sa.Column('last_transaction', sa.DateTime))


def downgrade():
    op.drop_column('Cards_1', 'last_transaction_date')

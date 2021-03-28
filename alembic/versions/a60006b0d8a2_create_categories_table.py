"""create categories table

Revision ID: a60006b0d8a2
Revises: 
Create Date: 2021-03-28 13:23:41.273363

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a60006b0d8a2'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'categories',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(50), nullable=False, unique=True),
        sa.Column('url', sa.String(100), nullable=False, unique=True),
        sa.Column('created_at', sa.DateTime, server_default=sa.func.current_timestamp()),
        sa.Column('updated_at', sa.DateTime, nullable=True),
    )


def downgrade():
    op.drop_table('categories')

"""rename address

Revision ID: 8f751e346118
Revises: d410619135f4
Create Date: 2025-08-31 10:26:53.143504
"""
from alembic import op
import sqlalchemy as sa  # kept for template consistency

# revision identifiers, used by Alembic.
revision = '8f751e346118'
down_revision = 'd410619135f4'
branch_labels = None
depends_on = None


def upgrade():
    # rename column without dropping data
    op.alter_column('departments', 'address', new_column_name='location')


def downgrade():
    # revert the rename
    op.alter_column('departments', 'location', new_column_name='address')

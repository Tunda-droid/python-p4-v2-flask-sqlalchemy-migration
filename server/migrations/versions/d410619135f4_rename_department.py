"""rename department

Revision ID: d410619135f4
Revises: 9ad691bb0212
Create Date: 2025-08-31 10:08:09.774687
"""
from alembic import op
import sqlalchemy as sa  # noqa: F401 (kept for consistency with Alembic templates)

# revision identifiers, used by Alembic.
revision = 'd410619135f4'
down_revision = '9ad691bb0212'
branch_labels = None
depends_on = None


def upgrade():
    # Rename existing table; preserves data.
    op.rename_table('department', 'departments')


def downgrade():
    # Revert the rename.
    op.rename_table('departments', 'department')

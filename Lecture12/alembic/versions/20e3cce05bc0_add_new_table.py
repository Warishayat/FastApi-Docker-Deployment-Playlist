"""add new table

Revision ID: 20e3cce05bc0
Revises: d898474e437a
Create Date: 2025-09-09 15:01:44.772434

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '20e3cce05bc0'
down_revision: Union[str, Sequence[str], None] = 'd898474e437a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass

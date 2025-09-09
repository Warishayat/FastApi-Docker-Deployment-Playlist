"""empty message

Revision ID: 069d4200debe
Revises: 7b41dfb09593
Create Date: 2025-09-09 14:47:27.739694

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '069d4200debe'
down_revision: Union[str, Sequence[str], None] = '7b41dfb09593'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass

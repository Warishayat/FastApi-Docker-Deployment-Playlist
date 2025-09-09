"""newcolum in authetication

Revision ID: d898474e437a
Revises: 069d4200debe
Create Date: 2025-09-09 14:55:57.215113

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd898474e437a'
down_revision: Union[str, Sequence[str], None] = '069d4200debe'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column("authentication",sa.Column("captcha",sa.Boolean(),nullable=False))
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column('authentication','captcha')
    pass

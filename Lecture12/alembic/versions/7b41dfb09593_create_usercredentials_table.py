"""create UserCredentials table

Revision ID: 7b41dfb09593
Revises: 
Create Date: 2025-09-09 14:35:12.780484

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7b41dfb09593'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table("authentication",sa.Column('id', sa.Integer(),nullable=False,primary_key=True),sa.Column('email',sa.String(),nullable=False,unique=True),sa.Column('name',sa.String(),nullable=False),sa.Column('password',sa.String(),nullable=False))
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table('authentication')
    pass

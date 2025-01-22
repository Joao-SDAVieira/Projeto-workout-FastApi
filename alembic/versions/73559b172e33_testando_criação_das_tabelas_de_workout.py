"""Testando criação das tabelas de workout

Revision ID: 73559b172e33
Revises: eaa712dce74f
Create Date: 2025-01-22 16:05:39.038909

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '73559b172e33'
down_revision: Union[str, None] = 'eaa712dce74f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass

"""Testando criação das tabelas de workout

Revision ID: ddabdf12522f
Revises: 73559b172e33
Create Date: 2025-01-22 16:15:22.242144

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ddabdf12522f'
down_revision: Union[str, None] = '73559b172e33'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass

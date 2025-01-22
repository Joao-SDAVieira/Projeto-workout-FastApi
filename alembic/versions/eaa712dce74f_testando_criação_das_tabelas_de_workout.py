"""Testando criação das tabelas de workout

Revision ID: eaa712dce74f
Revises: 39f73c558098
Create Date: 2025-01-22 16:00:19.192596

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'eaa712dce74f'
down_revision: Union[str, None] = '39f73c558098'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass

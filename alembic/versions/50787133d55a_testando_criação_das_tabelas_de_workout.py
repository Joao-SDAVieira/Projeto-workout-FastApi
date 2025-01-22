"""Testando criação das tabelas de workout

Revision ID: 50787133d55a
Revises: ddabdf12522f
Create Date: 2025-01-22 16:16:16.870055

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '50787133d55a'
down_revision: Union[str, None] = 'ddabdf12522f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass

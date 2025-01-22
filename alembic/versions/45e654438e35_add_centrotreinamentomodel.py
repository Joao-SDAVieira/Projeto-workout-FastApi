"""Add CentroTreinamentoModel

Revision ID: 45e654438e35
Revises: 50787133d55a
Create Date: 2025-01-22 16:17:38.339168

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '45e654438e35'
down_revision: Union[str, None] = '50787133d55a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass

"""create users table

Revision ID: 40386af76236
Revises: 
Create Date: 2023-10-25 11:43:35.701053

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '40386af76236'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

def upgrade() -> None:
    op.create_table(
        'users',
        sa.Column('id', sa.String, primary_key=True),
        sa.Column('email', sa.String, nullable=False),
        sa.Column('password', sa.String, nullable=False),
        sa.Column('display_name', sa.String, nullable=False, default="Tav"),
        sa.Column('created_date', sa.DateTime, nullable=False),
        sa.Column('is_admin', sa.Boolean, nullable=False, default=False)
    )


def downgrade() -> None:
    op.drop_table('account')

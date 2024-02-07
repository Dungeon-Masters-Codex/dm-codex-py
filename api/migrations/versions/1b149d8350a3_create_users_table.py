"""create users table

Revision ID: 1b149d8350a3
Revises: 
Create Date: 2023-10-26 09:02:31.234179

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1b149d8350a3'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True, index=True),
        sa.Column('username', sa.String, unique=True, nullable=False),
        sa.Column('password', sa.String, nullable=False),
        sa.Column('display_name', sa.String(25)),
        sa.Column('created_date', sa.DateTime)
    )

def downgrade() -> None:
    op.drop_table('users')

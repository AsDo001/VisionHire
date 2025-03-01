"""Added Hierarchy

Revision ID: 28587c58824e
Revises: e06c72b684e3
Create Date: 2024-10-05 17:45:54.602949

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '28587c58824e'
down_revision: Union[str, None] = 'e06c72b684e3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('hierarchies',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('super_id', sa.String(), nullable=False),
    sa.Column('sub_id', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['sub_id'], ['users.username'], ),
    sa.ForeignKeyConstraint(['super_id'], ['users.username'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('hierarchies')
    # ### end Alembic commands ###

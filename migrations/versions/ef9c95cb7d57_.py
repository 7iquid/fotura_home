"""empty message

Revision ID: ef9c95cb7d57
Revises: eb5ef70e8294
Create Date: 2021-07-21 21:48:26.340063

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ef9c95cb7d57'
down_revision = 'eb5ef70e8294'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Barcode_table', sa.Column('barcode_id', sa.String(length=100), nullable=True))
    op.create_foreign_key(None, 'Barcode_table', 'User', ['user_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'Barcode_table', type_='foreignkey')
    op.drop_column('Barcode_table', 'barcode_id')
    # ### end Alembic commands ###
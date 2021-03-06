"""empty message

Revision ID: 68ab0c5382ba
Revises: 8642846dee76
Create Date: 2021-07-21 22:25:13.269332

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '68ab0c5382ba'
down_revision = '8642846dee76'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key(None, 'Barcode_table', 'User', ['user_id'], ['id'])
    op.drop_column('Barcode_table', 'name_db')
    op.drop_column('Barcode_table', 'img_ko')
    op.drop_column('Barcode_table', 'date_entry')
    op.drop_column('Barcode_table', 'by')
    op.drop_column('Barcode_table', 'date_exit')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Barcode_table', sa.Column('date_exit', sa.DATETIME(), nullable=True))
    op.add_column('Barcode_table', sa.Column('by', sa.VARCHAR(length=100), nullable=True))
    op.add_column('Barcode_table', sa.Column('date_entry', sa.DATETIME(), nullable=True))
    op.add_column('Barcode_table', sa.Column('img_ko', sa.BLOB(), nullable=True))
    op.add_column('Barcode_table', sa.Column('name_db', sa.VARCHAR(length=100), nullable=True))
    op.drop_constraint(None, 'Barcode_table', type_='foreignkey')
    # ### end Alembic commands ###

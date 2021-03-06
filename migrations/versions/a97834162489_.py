"""empty message

Revision ID: a97834162489
Revises: 4664bd227e20
Create Date: 2021-07-23 15:48:57.765939

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a97834162489'
down_revision = '4664bd227e20'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('Barcode_table', 'mimetype_db',
               existing_type=sa.TEXT(),
               nullable=True)
    op.create_foreign_key(None, 'Barcode_table', 'User', ['user_id'], ['id'])
    op.drop_column('Barcode_table', 'date_entry')
    op.drop_column('Barcode_table', 'by')
    op.drop_column('Barcode_table', 'date_exit')
    op.drop_column('Barcode_table', 'name_db')
    op.drop_column('Barcode_table', 'img_ko')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Barcode_table', sa.Column('img_ko', sa.BLOB(), nullable=True))
    op.add_column('Barcode_table', sa.Column('name_db', sa.VARCHAR(length=100), nullable=True))
    op.add_column('Barcode_table', sa.Column('date_exit', sa.DATETIME(), nullable=True))
    op.add_column('Barcode_table', sa.Column('by', sa.VARCHAR(length=100), nullable=True))
    op.add_column('Barcode_table', sa.Column('date_entry', sa.DATETIME(), nullable=True))
    op.drop_constraint(None, 'Barcode_table', type_='foreignkey')
    op.alter_column('Barcode_table', 'mimetype_db',
               existing_type=sa.TEXT(),
               nullable=False)
    # ### end Alembic commands ###

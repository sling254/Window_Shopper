"""IntegerField

Revision ID: 1c03d5af70f1
Revises: de202f139537
Create Date: 2021-11-18 11:13:27.839097

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1c03d5af70f1'
down_revision = 'de202f139537'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('products', 'price',
               existing_type=sa.NUMERIC(precision=10, scale=2),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('products', 'price',
               existing_type=sa.NUMERIC(precision=10, scale=2),
               nullable=True)
    # ### end Alembic commands ###

"""empty message

Revision ID: 0ba416ae657f
Revises: c4ffbc8a4449
Create Date: 2020-03-09 14:43:23.771492

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0ba416ae657f'
down_revision = 'c4ffbc8a4449'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('course_type', sa.Column('_bg_iamge', sa.String(length=255), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('course_type', '_bg_iamge')
    # ### end Alembic commands ###

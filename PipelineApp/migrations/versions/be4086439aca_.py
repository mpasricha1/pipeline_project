"""empty message

Revision ID: be4086439aca
Revises: 64e229b234e8
Create Date: 2020-12-05 19:05:06.887424

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'be4086439aca'
down_revision = '64e229b234e8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('pipeline_location', sa.Column('new_column', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('pipeline_location', 'new_column')
    # ### end Alembic commands ###
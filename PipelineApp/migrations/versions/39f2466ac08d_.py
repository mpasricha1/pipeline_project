"""empty message

Revision ID: 39f2466ac08d
Revises: 6b97410df7de
Create Date: 2020-12-05 19:11:46.072275

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '39f2466ac08d'
down_revision = '6b97410df7de'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('pipeline_location', sa.Column('flow_direction', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('pipeline_location', 'flow_direction')
    # ### end Alembic commands ###

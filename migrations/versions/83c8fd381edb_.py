"""empty message

Revision ID: 83c8fd381edb
Revises: 
Create Date: 2020-05-22 12:42:44.383054

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '83c8fd381edb'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('course_tb',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(), nullable=True),
    sa.Column('last_name', sa.String(), nullable=True),
    sa.Column('email_address', sa.String(), nullable=True),
    sa.Column('contact', sa.String(), nullable=True),
    sa.Column('course_url', sa.String(), nullable=True),
    sa.Column('english', sa.String(), nullable=True),
    sa.Column('hindi', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('course_tb')
    # ### end Alembic commands ###
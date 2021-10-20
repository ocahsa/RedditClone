"""empty message

Revision ID: c38daf2b928a
Revises: 5298aca9cc15
Create Date: 2021-10-19 12:43:57.304736

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c38daf2b928a'
down_revision = '5298aca9cc15'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('subreddits', sa.Column('tag', sa.String(length=50), nullable=False))
    op.drop_constraint('subreddits_slash_name_key', 'subreddits', type_='unique')
    op.create_unique_constraint(None, 'subreddits', ['tag'])
    op.drop_column('subreddits', 'slash_name')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('subreddits', sa.Column('slash_name', sa.VARCHAR(length=50), autoincrement=False, nullable=False))
    op.drop_constraint(None, 'subreddits', type_='unique')
    op.create_unique_constraint('subreddits_slash_name_key', 'subreddits', ['slash_name'])
    op.drop_column('subreddits', 'tag')
    # ### end Alembic commands ###
"""empty message

Revision ID: 46200a5c86b5
Revises: 
Create Date: 2021-08-19 11:01:31.784801

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '46200a5c86b5'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=64), nullable=False),
    sa.Column('password', sa.String(length=128), nullable=True),
    sa.Column('full_name', sa.String(length=25), nullable=False),
    sa.Column('about_me', sa.String(length=140), nullable=True),
    sa.Column('date_of_birth', sa.Date(), nullable=True),
    sa.Column('email_confirmed', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_email'), 'user', ['email'], unique=True)
    op.create_index(op.f('ix_user_full_name'), 'user', ['full_name'], unique=False)
    op.create_table('peer_requests',
    sa.Column('peer_id', sa.Integer(), nullable=False),
    sa.Column('peered_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['peer_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['peered_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('peer_id', 'peered_id')
    )
    op.create_table('peers',
    sa.Column('peer1_id', sa.Integer(), nullable=False),
    sa.Column('peer2_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['peer1_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['peer2_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('peer1_id', 'peer2_id')
    )
    op.create_table('post',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=100), nullable=False),
    sa.Column('date_posted', sa.DateTime(), nullable=False),
    sa.Column('content', sa.Text(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('comment',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('content', sa.Text(), nullable=False),
    sa.Column('date_posted', sa.DateTime(), nullable=False),
    sa.Column('post_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['post_id'], ['post.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('comment')
    op.drop_table('post')
    op.drop_table('peers')
    op.drop_table('peer_requests')
    op.drop_index(op.f('ix_user_full_name'), table_name='user')
    op.drop_index(op.f('ix_user_email'), table_name='user')
    op.drop_table('user')
    # ### end Alembic commands ###

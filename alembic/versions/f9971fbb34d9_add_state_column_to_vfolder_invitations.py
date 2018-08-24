"""add state column to vfolder_invitations

Revision ID: f9971fbb34d9
Revises: 185852ff9872
Create Date: 2018-07-12 23:30:14.942845

"""
from alembic import op
import sqlalchemy as sa
import ai.backend.manager.models.base  # noqa


# revision identifiers, used by Alembic.
revision = 'f9971fbb34d9'
down_revision = '185852ff9872'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('vfolder_invitations', sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True))
    op.add_column('vfolder_invitations', sa.Column('state', sa.String(length=10), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('vfolder_invitations', 'state')
    op.drop_column('vfolder_invitations', 'created_at')
    # ### end Alembic commands ###
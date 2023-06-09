"""empty message

Revision ID: 1f919874f1c4
Revises: 87936c906825
Create Date: 2023-06-08 17:56:40.736317

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1f919874f1c4'
down_revision = '87936c906825'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('camera_storage',
    sa.Column('id', sa.UUID(), server_default=sa.text('gen_random_uuid()'), nullable=False),
    sa.Column('owner', sa.TEXT(), nullable=False),
    sa.Column('name', sa.TEXT(), nullable=False),
    sa.Column('model', sa.TEXT(), nullable=False),
    sa.Column('serial_number', sa.TEXT(), nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('pk__camera_storage')),
    sa.UniqueConstraint('id', name=op.f('uq__camera_storage__id'))
    )
    op.create_index(op.f('ix__camera_storage__model'), 'camera_storage', ['model'], unique=False)
    op.create_index(op.f('ix__camera_storage__name'), 'camera_storage', ['name'], unique=False)
    op.create_index(op.f('ix__camera_storage__owner'), 'camera_storage', ['owner'], unique=False)
    op.create_index(op.f('ix__camera_storage__serial_number'), 'camera_storage', ['serial_number'], unique=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix__camera_storage__serial_number'), table_name='camera_storage')
    op.drop_index(op.f('ix__camera_storage__owner'), table_name='camera_storage')
    op.drop_index(op.f('ix__camera_storage__name'), table_name='camera_storage')
    op.drop_index(op.f('ix__camera_storage__model'), table_name='camera_storage')
    op.drop_table('camera_storage')
    # ### end Alembic commands ###

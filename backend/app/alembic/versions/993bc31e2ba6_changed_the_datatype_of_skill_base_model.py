"""changed the datatype of Skill base model

Revision ID: 993bc31e2ba6
Revises: 
Create Date: 2023-07-17 17:50:52.447677

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '993bc31e2ba6'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.execute('ALTER TABLE skill ALTER COLUMN "Python" TYPE INTEGER USING "Python"::integer')
    op.alter_column('skill', 'Python',
               existing_type=sa.VARCHAR(),
               type_=sa.Integer(),
               existing_nullable=True,
               using='Python::integer')
    
    op.execute('ALTER TABLE skill ALTER COLUMN "OLGA" TYPE INTEGER USING "OLGA"::integer')
    op.alter_column('skill', 'OLGA',
               existing_type=sa.VARCHAR(),
               type_=sa.Integer(),
               existing_nullable=True,
               using='OLGA::integer')
    op.execute('ALTER TABLE skill ALTER COLUMN "HYSYS" TYPE INTEGER USING "HYSYS"::integer')
    op.alter_column('skill', 'HYSYS',
               existing_type=sa.VARCHAR(),
               type_=sa.Integer(),
               existing_nullable=True,
               using='HYSYS::integer')



    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('skill', 'HYSYS',
               existing_type=sa.Integer(),
               type_=sa.VARCHAR(),
               existing_nullable=True)
    op.alter_column('skill', 'OLGA',
               existing_type=sa.Integer(),
               type_=sa.VARCHAR(),
               existing_nullable=True)
    op.alter_column('skill', 'Python',
               existing_type=sa.Integer(),
               type_=sa.VARCHAR(),
               existing_nullable=True)
    # ### end Alembic commands ###

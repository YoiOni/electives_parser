"""initialization

Revision ID: f0e26f0eb6b9
Revises:
Create Date: 2022-05-18 21:29:54.116202

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "f0e26f0eb6b9"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "author",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(length=100), nullable=False),
        sa.Column("description", sa.String(length=255), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "minor",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("title", sa.String(length=255), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "tag",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(length=100), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "elective",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("title", sa.String(length=50), nullable=False),
        sa.Column("short_description", sa.String(length=50), nullable=True),
        sa.Column("full_description", sa.String(length=255), nullable=True),
        sa.Column("minor_id", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(
            ["minor_id"],
            ["minor.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "author_elective",
        sa.Column("elective_id", sa.Integer(), nullable=False),
        sa.Column("author_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["author_id"],
            ["author.id"],
        ),
        sa.ForeignKeyConstraint(
            ["elective_id"],
            ["elective.id"],
        ),
        sa.PrimaryKeyConstraint("elective_id", "author_id"),
    )
    op.create_table(
        "tag_elective",
        sa.Column("elective_id", sa.Integer(), nullable=False),
        sa.Column("tag_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["elective_id"],
            ["elective.id"],
        ),
        sa.ForeignKeyConstraint(
            ["tag_id"],
            ["tag.id"],
        ),
        sa.PrimaryKeyConstraint("elective_id", "tag_id"),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("tag_elective")
    op.drop_table("author_elective")
    op.drop_table("elective")
    op.drop_table("tag")
    op.drop_table("minor")
    op.drop_table("author")
    # ### end Alembic commands ###

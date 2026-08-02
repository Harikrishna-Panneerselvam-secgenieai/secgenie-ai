"""add investigation supporting models and relationships

Revision ID: 428b094a6174
Revises: 0a44cc4bf1e8
Create Date: 2026-07-31 20:21:49.563598

"""

from collections.abc import Sequence

import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

from alembic import op

revision: str = "428b094a6174"
down_revision: str | Sequence[str] | None = "0a44cc4bf1e8"
branch_labels = None
depends_on = None


def upgrade() -> None:
    """Upgrade schema."""

    # ---------------------------------------------------------
    # Create users table
    # ---------------------------------------------------------

    op.create_table(
        "users",
        sa.Column("username", sa.String(length=100), nullable=False),
        sa.Column("email", sa.String(length=255), nullable=False),
        sa.Column("role", sa.String(length=50), nullable=False),
        sa.Column("id", sa.UUID(), nullable=False),
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.Column(
            "updated_at",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.Column("created_by", sa.String(length=255), nullable=True),
        sa.Column("updated_by", sa.String(length=255), nullable=True),
        sa.Column(
            "is_deleted",
            sa.Boolean(),
            server_default="false",
            nullable=False,
        ),
        sa.Column("deleted_at", sa.DateTime(timezone=True), nullable=True),
        sa.Column("deleted_by", sa.String(length=255), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )

    op.create_index(
        "ix_users_email",
        "users",
        ["email"],
        unique=True,
    )

    # ---------------------------------------------------------
    # Create audit logs
    # ---------------------------------------------------------

    op.create_table(
        "audit_logs",
        sa.Column("user_id", sa.String(length=36), nullable=True),
        sa.Column("action", sa.String(length=100), nullable=False),
        sa.Column("entity_type", sa.String(length=100), nullable=False),
        sa.Column("entity_id", sa.String(length=36), nullable=True),
        sa.Column("metadata", sa.JSON(), nullable=False),
        sa.Column("id", sa.UUID(), nullable=False),
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.Column(
            "updated_at",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.Column("created_by", sa.String(length=255), nullable=True),
        sa.Column("updated_by", sa.String(length=255), nullable=True),
        sa.Column(
            "is_deleted",
            sa.Boolean(),
            server_default="false",
            nullable=False,
        ),
        sa.Column("deleted_at", sa.DateTime(timezone=True), nullable=True),
        sa.Column("deleted_by", sa.String(length=255), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )

    op.create_index(
        "ix_audit_logs_user_id",
        "audit_logs",
        ["user_id"],
        unique=False,
    )

    # ---------------------------------------------------------
    # Create findings
    # ---------------------------------------------------------

    op.create_table(
        "findings",
        sa.Column("investigation_id", sa.UUID(), nullable=False),
        sa.Column("title", sa.String(length=255), nullable=False),
        sa.Column("description", sa.String(length=2000)),
        sa.Column("severity", sa.String(length=50), nullable=False),
        sa.Column("category", sa.String(length=100), nullable=False),
        sa.Column("confidence_score", sa.Float()),
        sa.Column("status", sa.String(length=50), nullable=False),
        sa.Column("id", sa.UUID(), nullable=False),
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.Column(
            "updated_at",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.Column("created_by", sa.String(length=255)),
        sa.Column("updated_by", sa.String(length=255)),
        sa.Column(
            "is_deleted",
            sa.Boolean(),
            server_default="false",
            nullable=False,
        ),
        sa.Column("deleted_at", sa.DateTime(timezone=True)),
        sa.Column("deleted_by", sa.String(length=255)),
        sa.ForeignKeyConstraint(
            ["investigation_id"],
            ["investigations.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )

    op.create_index(
        "ix_findings_investigation_id",
        "findings",
        ["investigation_id"],
    )

    # ---------------------------------------------------------
    # Create investigation tasks
    # ---------------------------------------------------------

    op.create_table(
        "investigation_tasks",
        sa.Column("investigation_id", sa.UUID(), nullable=False),
        sa.Column("agent_name", sa.String(length=100), nullable=False),
        sa.Column("task_type", sa.String(length=100), nullable=False),
        sa.Column("status", sa.String(length=50), nullable=False),
        sa.Column("started_at", sa.DateTime(timezone=True)),
        sa.Column("completed_at", sa.DateTime(timezone=True)),
        sa.Column("result", sa.JSON()),
        sa.Column("error_message", sa.String(length=2000)),
        sa.Column("id", sa.UUID(), nullable=False),
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.Column(
            "updated_at",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.Column("created_by", sa.String(length=255)),
        sa.Column("updated_by", sa.String(length=255)),
        sa.Column(
            "is_deleted",
            sa.Boolean(),
            server_default="false",
            nullable=False,
        ),
        sa.Column("deleted_at", sa.DateTime(timezone=True)),
        sa.Column("deleted_by", sa.String(length=255)),
        sa.ForeignKeyConstraint(
            ["investigation_id"],
            ["investigations.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )

    op.create_index(
        "ix_investigation_tasks_investigation_id",
        "investigation_tasks",
        ["investigation_id"],
    )

    # ---------------------------------------------------------
    # Create timeline
    # ---------------------------------------------------------

    op.create_table(
        "investigation_timelines",
        sa.Column("investigation_id", sa.UUID(), nullable=False),
        sa.Column("event_type", sa.String(length=100), nullable=False),
        sa.Column("message", sa.String(length=2000), nullable=False),
        sa.Column("agent_name", sa.String(length=100)),
        sa.Column("event_time", sa.DateTime(timezone=True), nullable=False),
        sa.Column("id", sa.UUID(), nullable=False),
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.Column(
            "updated_at",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.Column("created_by", sa.String(length=255)),
        sa.Column("updated_by", sa.String(length=255)),
        sa.Column(
            "is_deleted",
            sa.Boolean(),
            server_default="false",
            nullable=False,
        ),
        sa.Column("deleted_at", sa.DateTime(timezone=True)),
        sa.Column("deleted_by", sa.String(length=255)),
        sa.ForeignKeyConstraint(
            ["investigation_id"],
            ["investigations.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )

    op.create_index(
        "ix_investigation_timelines_investigation_id",
        "investigation_timelines",
        ["investigation_id"],
    )

    # ---------------------------------------------------------
    # Create evidence
    # ---------------------------------------------------------

    op.create_table(
        "evidence",
        sa.Column("investigation_id", sa.UUID(), nullable=False),
        sa.Column("finding_id", sa.UUID()),
        sa.Column("evidence_type", sa.String(length=50), nullable=False),
        sa.Column("source", sa.String(length=255), nullable=False),
        sa.Column("data", sa.JSON(), nullable=False),
        sa.Column("collected_by", sa.String(length=100)),
        sa.Column("id", sa.UUID(), nullable=False),
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.Column(
            "updated_at",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.Column("created_by", sa.String(length=255)),
        sa.Column("updated_by", sa.String(length=255)),
        sa.Column(
            "is_deleted",
            sa.Boolean(),
            server_default="false",
            nullable=False,
        ),
        sa.Column("deleted_at", sa.DateTime(timezone=True)),
        sa.Column("deleted_by", sa.String(length=255)),
        sa.ForeignKeyConstraint(
            ["investigation_id"],
            ["investigations.id"],
        ),
        sa.ForeignKeyConstraint(
            ["finding_id"],
            ["findings.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )

    op.create_index(
        "ix_evidence_investigation_id",
        "evidence",
        ["investigation_id"],
    )

    op.create_index(
        "ix_evidence_finding_id",
        "evidence",
        ["finding_id"],
    )

    # ---------------------------------------------------------
    # IMPORTANT FIX
    # Convert owner_id before FK creation
    # ---------------------------------------------------------

    op.alter_column(
        "investigations",
        "owner_id",
        existing_type=sa.VARCHAR(length=36),
        type_=postgresql.UUID(),
        existing_nullable=True,
        postgresql_using="owner_id::uuid",
    )

    op.create_foreign_key(
        "fk_investigations_owner_id_users",
        "investigations",
        "users",
        ["owner_id"],
        ["id"],
    )


def downgrade() -> None:
    """Downgrade schema."""

    op.drop_constraint(
        "fk_investigations_owner_id_users",
        "investigations",
        type_="foreignkey",
    )

    op.drop_index(
        "ix_evidence_finding_id",
        table_name="evidence",
    )

    op.drop_index(
        "ix_evidence_investigation_id",
        table_name="evidence",
    )

    op.drop_table("evidence")

    op.drop_index(
        "ix_investigation_timelines_investigation_id",
        table_name="investigation_timelines",
    )

    op.drop_table("investigation_timelines")

    op.drop_index(
        "ix_investigation_tasks_investigation_id",
        table_name="investigation_tasks",
    )

    op.drop_table("investigation_tasks")

    op.drop_index(
        "ix_findings_investigation_id",
        table_name="findings",
    )

    op.drop_table("findings")

    op.drop_index(
        "ix_users_email",
        table_name="users",
    )

    op.drop_table("users")

    op.drop_index(
        "ix_audit_logs_user_id",
        table_name="audit_logs",
    )

    op.drop_table("audit_logs")

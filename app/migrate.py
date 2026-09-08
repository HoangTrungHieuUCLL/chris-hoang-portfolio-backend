"""Adds any model columns missing from an already-existing table.

Base.metadata.create_all() only creates tables that don't exist yet. It never
alters an existing table's columns. Since this project has no Alembic setup,
call ensure_schema() before querying so new fields added to models.py show up
in the live database automatically on the next deploy.
"""

from sqlalchemy import inspect, text
from sqlalchemy.schema import CreateColumn

from app.database import engine
from app.models import Project

TABLES = [Project]


def ensure_schema():
    inspector = inspect(engine)
    with engine.begin() as conn:
        for model in TABLES:
            table_name = model.__tablename__
            if not inspector.has_table(table_name):
                continue
            existing = {col["name"] for col in inspector.get_columns(table_name)}
            for column in model.__table__.columns:
                if column.name in existing:
                    continue
                ddl = str(CreateColumn(column).compile(dialect=engine.dialect))
                conn.execute(text(f"ALTER TABLE {table_name} ADD COLUMN {ddl}"))

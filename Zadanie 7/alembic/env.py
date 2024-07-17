import os
import sys
from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from alembic import context

# Dodaj ścieżkę do katalogu z plikiem my_models.py
sys.path.insert(0, os.path.realpath(os.path.join(os.path.dirname(__file__), '..')))

from my_models import Base  # Importuj swoje modele

# Interpret the config file for Python logging.
fileConfig(context.config.config_file_name)

# Alembic Config object, which provides access to values within the .ini file.
config = context.config

# Target metadata for 'autogenerate' support.
target_metadata = Base.metadata

def run_migrations_online():
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix='sqlalchemy.',
        poolclass=pool.NullPool
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()

run_migrations_online()

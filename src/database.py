# pylint: disable=C0114,  W3101
#import os
from sqlalchemy import create_engine, MetaData
import databases



# PG_DATABASE = os.environ.get("PG_DATABASE")
# PG_USER = os.environ.get("PG_USER")
# PG_PASSWORD = os.environ.get("PG_PASSWORD")
# PG_HOST = os.environ.get("PG_HOST")
# PG_PORT = os.environ.get("PG_PORT")


# SQLALCHEMY_DATABASE_URL = f"{PG_DATABASE}://{PG_USER}:{PG_PASSWORD}@{PG_HOST}/{PG_PORT}"
SQLALCHEMY_DATABASE_URL = "sqlite:///./user_database.db"

database = databases.Database(SQLALCHEMY_DATABASE_URL)

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

metadata = MetaData()
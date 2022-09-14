# pylint: disable=C0114,  W3101
import os
from sqlalchemy import create_engine, MetaData
import databases


POSTGRES_WEB_DB = os.environ.get("POSTGRES_WEB_DB")
POSTGRES_WEB_USER = os.environ.get("POSTGRES_WEB_USER")
POSTGRES_WEB_PASSWORD = os.environ.get("POSTGRES_WEB_PASSWORD")
POSTGRES_WEB_HOST = os.environ.get("POSTGRES_WEB_HOST")
POSTGRES_WEB_PORT = os.environ.get("POSTGRES_WEB_PORT")


SQLALCHEMY_DATABASE_URL = f"postgresql://{POSTGRES_WEB_USER}:{POSTGRES_WEB_PASSWORD}@{POSTGRES_WEB_HOST}:{POSTGRES_WEB_PORT}/{POSTGRES_WEB_DB}"


database = databases.Database(SQLALCHEMY_DATABASE_URL)

engine = create_engine(SQLALCHEMY_DATABASE_URL)

metadata = MetaData()

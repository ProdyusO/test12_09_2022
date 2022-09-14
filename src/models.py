# pylint: disable=C0114
from sqlalchemy import Column, Integer, Table, String
from database import metadata

notes = Table(
    "notes",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("title", String(100)),
    Column("img", String(100)),
    Column("date", String(100)),
    Column("city", String(100)),
    Column("bed", String(100)),
    Column("description", String(100)),
    Column("currencies", String(100)),
    Column("price", String(100)),
)
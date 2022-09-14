# pylint: disable=C0114
from sqlalchemy import Column, Integer, Table, String
from database import metadata

notes = Table(
    "notes",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("title", String(500)),
    Column("img", String(500)),
    Column("date", String(30)),
    Column("city", String(500)),
    Column("bed", String(30)),
    Column("description", String(500)),
    Column("currencies", String(30)),
    Column("price", String(30)),
)
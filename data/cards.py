import datetime
import sqlalchemy
from sqlalchemy import orm

from .db_session import SqlAlchemyBase


class Card(SqlAlchemyBase):
    __tablename__ = 'card'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)

    title = sqlalchemy.Column(sqlalchemy.String, nullable=True)

    content = sqlalchemy.Column(sqlalchemy.String, nullable=True)

    price = sqlalchemy.Column(sqlalchemy.Integer, autoincrement=False)

    filename = sqlalchemy.Column(sqlalchemy.String, nullable=True)

    material = sqlalchemy.Column(sqlalchemy.String, nullable=True)

    theme = sqlalchemy.Column(sqlalchemy.String, nullable=True)

    under_theme = sqlalchemy.Column(sqlalchemy.String, nullable=True)

    key_words = sqlalchemy.Column(sqlalchemy.String, nullable=True)

    rating = sqlalchemy.Column(sqlalchemy.Integer, autoincrement=False)

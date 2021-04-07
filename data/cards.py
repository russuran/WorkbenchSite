import datetime
import sqlalchemy
from sqlalchemy import orm

from .db_session import SqlAlchemyBase


class Card(SqlAlchemyBase):
    __tablename__ = 'card'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=False)

    title = sqlalchemy.Column(sqlalchemy.String, nullable=True)

    content = sqlalchemy.Column(sqlalchemy.String, nullable=True)

    price = sqlalchemy.Column(sqlalchemy.Integer, autoincrement=False)

    key_words = sqlalchemy.Column(sqlalchemy.String, nullable=True)

    photo = sqlalchemy.Column(sqlalchemy.LargeBinary, nullable=True)

    created_date = sqlalchemy.Column(sqlalchemy.DateTime,
                                     default=datetime.datetime.now)

import sqlalchemy
from .db_session import SqlAlchemyBase


class Album(SqlAlchemyBase):
    __tablename__ = 'Albums'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    album_name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    singer_id = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)


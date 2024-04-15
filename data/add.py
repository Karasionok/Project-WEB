import sqlalchemy
from .db_session import SqlAlchemyBase


class Track(SqlAlchemyBase):
    __tablename__ = 'Tracks'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    album_id = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    duration = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    path = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    singer_id = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)

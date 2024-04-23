import sqlalchemy

from .db_session import SqlAlchemyBase


class TrackUser(SqlAlchemyBase):
    __tablename__ = 'TrackUser'
    track_id = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    user_id = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
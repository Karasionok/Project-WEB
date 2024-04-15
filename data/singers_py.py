import sqlalchemy
from .db_session import SqlAlchemyBase


class Singer(SqlAlchemyBase):
    __tablename__ = 'Singers'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=True)

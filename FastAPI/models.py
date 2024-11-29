from database import Base
import sqlalchemy as _sql


class Todo(Base):
    __tablename__ = 'todo'
    id = _sql.Column(_sql.Integer, primary_key=True, unique=True)
    title = _sql.Column(_sql.String)
    completed = _sql.Column(_sql.Boolean)


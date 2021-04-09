from app import sa, session, Base

from datetime import datetime


# Model class of resources table in store DB
class Resource(Base):
    __tablename__ = 'resources'

    id = sa.Column(sa.Integer, unique=True, primary_key=True, autoincrement=True)
    title = sa.Column(sa.String(8), nullable=False, unique=True)
    amount = sa.Column(sa.Float)
    measurement = sa.Column(sa.String(8), nullable=False)
    price = sa.Column(sa.Float)
    create_at = sa.Column(sa.DateTime, default=datetime.utcnow)


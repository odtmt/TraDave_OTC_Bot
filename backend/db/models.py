from backend.db.database import Base
from sqlalchemy import Column, Integer, String, Float, DateTime
from datetime import datetime


class Trade(Base):

    __tablename__ = "trades"

    id = Column(Integer, primary_key=True)
    pair = Column(String)
    direction = Column(String)
    score = Column(Float)
    confidence = Column(Float)
    result = Column(String)
    timestamp = Column(DateTime, default=datetime.utcnow)
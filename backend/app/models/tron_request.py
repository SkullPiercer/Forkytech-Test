from sqlalchemy import Column, String, DateTime, Integer, Float
from sqlalchemy.sql import func

from app.core.db import Base


class TronRequest(Base):
    wallet_address = Column(String(100), nullable=False)
    balance = Column(Float, nullable=False)
    bandwidth = Column(Integer, nullable=False)
    energy_remaining = Column(Integer, nullable=False)
    requested_at = Column(DateTime, server_default=func.now())

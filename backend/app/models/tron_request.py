from sqlalchemy import Column, String, DateTime
from sqlalchemy.sql import func

from app.core.db import Base


class TronRequest(Base):
    wallet_address = Column(String(100), nullable=False)
    requested_at = Column(DateTime, server_default=func.now())

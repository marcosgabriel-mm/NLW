from src.models.settings.base import Base
from sqlalchemy import Column, Integer, DateTime, ForeignKey, String
from sqlalchemy.sql import func

class CheckIns(Base):
    __tablename__ = "check_ins"

    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, default=func.now())
    attendeeId = Column(String, ForeignKey("attendees.id"))

    def __repr__(self):
        return f"CheckIns [id={self.attendeeId}]"
    
from typing import TYPE_CHECKING

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.db.base_class import Base

if TYPE_CHECKING:
    from .user import User  # noqa: F401


class Skill(Base):
    id = Column(Integer, primary_key=True, index=True)
    Python = Column(Integer, index=True)
    OLGA = Column(Integer, index=True)
    owner_id = Column(Integer, ForeignKey("user.id"))
    owner = relationship("User", back_populates="skills")
    HYSYS = Column(Integer, index=True)

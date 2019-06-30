from datetime import datetime
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship
from repository.sqlite import Base
from model.category import Category
from model.user import User


class Item(Base):
    __tablename__ = "item"

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    description = Column(String(2000))
    last_update = Column(DateTime, default=datetime.utcnow,
                         onupdate=datetime.utcnow)
    category_id = Column(Integer, ForeignKey("category.id"))
    category = relationship(Category)
    owner_id = Column(Integer, ForeignKey("user.id"))
    owner = relationship(User)

    @property
    def serialize(self):
        return {
            'name': self.name,
            'description': self.description,
            'id': self.id,
        }

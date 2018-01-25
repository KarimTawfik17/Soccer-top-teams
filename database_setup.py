import sys
import os
from sqlalchemy import ForeignKey, Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
Base = declarative_base()


class League(Base):
    __tablename__ = 'league'
    name = Column(String(80), nullable=False)
    id = Column(Integer, primary_key=True)


class Team(Base):
    __tablename__ = 'team'
    name = Column(String(80), nullable=False)
    id = Column(Integer, primary_key=True)
    info = Column(String(500))
    league_id = Column(Integer, ForeignKey(League.id))
    league = relationship(League)

    # @property
    # def serialize(self):
    #     return {
    #         'name': self.name,
    #         'id': self.id,
    #         'price': self.price,
    #         'description': self.description,
    #         'course': self.course
    #     }


engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.create_all(engine)
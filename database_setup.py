import sys
import os
from sqlalchemy import ForeignKey, Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
Base = declarative_base()


# create league table
class League(Base):
    __tablename__ = 'league'
    name = Column(String(80), nullable=False)
    id = Column(Integer, primary_key=True)


# create team table
class Team(Base):
    __tablename__ = 'team'
    name = Column(String(80), nullable=False)
    id = Column(Integer, primary_key=True)
    info = Column(String(500))
    league_id = Column(Integer, ForeignKey(League.id))
    league = relationship(League)


# add serialization property for json responses
    @property
    def serialize(self):
        return {
            'name': self.name,
            'id': self.id,
            'info': self.info,
            'league': self.league.name,
        }


engine = create_engine('sqlite:///teams.db')
Base.metadata.create_all(engine)

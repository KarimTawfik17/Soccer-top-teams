from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, League, Team

engine = create_engine('sqlite:///teams.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

 for i in range(5):
 	league_name = raw_input("enter league name : ")
 	templeague = League(name = league_name)
 	session.add(templeague)

session.commit()

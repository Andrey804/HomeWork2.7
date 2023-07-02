from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base


engine = create_engine('postgresql://postgres:password@localhost:5432/school')

Base = declarative_base()

DBSession = sessionmaker(bind=engine)
session = DBSession()

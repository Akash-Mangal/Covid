import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

# setup db code
Base = declarative_base()

# create table as python class
class Image(Base):
    __tablename__ = 'images'
    id = Column(Integer,primary_key=True)
    path = Column(String)
    name = Column(String)
    age = Column(Integer)
    gender = Column(String)
    contact = Column(Integer)
    uploaded_on = Column(String,default=datetime.now().strftime(" %d %b, %Y at %I:%M %p"))
    result=Column(String)

    def __str__(self):
        return self.path
    
    def __repr__(self) -> str:
        return self.path

# create database
if __name__ == "__main__":
    engine = create_engine("sqlite:///db.sqlite3")
    Base.metadata.create_all(engine)
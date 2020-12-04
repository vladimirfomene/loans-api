from datetime import datetime
from sqlalchemy import create_engine, Column, String, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


engine = create_engine("postgresql://postgres:mysecretpassword@localhost:9000/loanapp")
Session = sessionmaker(bind=engine)

Base = declarative_base()


class Model():
    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    last_updated_by = Column(String)

    def __init__(self):
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

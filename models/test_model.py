from sqlalchemy import  Column, string, INTEGER, ForeignKey
from sqlalchemy.orm import relationship
from db.session import Base


class Test(Base):
    __tablename__ = "test"

    id = Column(INTEGER, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
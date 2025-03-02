from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#  Define SQLite database file
DATABASE_URL = "sqlite:///./app/models/language_data.db"

#  Create Engine & Session
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

#  Define LanguageDataset Table
class LanguageDataset(Base):
    __tablename__ = "language_data"

    id = Column(Integer, primary_key=True, index=True)
    text = Column(String, nullable=False)
    language = Column(String, nullable=False)

#  Create Table in DB
Base.metadata.create_all(bind=engine)

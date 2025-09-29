from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from app.core.config import DATEBASE_URL

engine = create_engine(DATEBASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, binf=engine)
Base = declarative_base()
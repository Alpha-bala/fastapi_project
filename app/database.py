from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker





# Replace with your actual MySQL details
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:123@localhost:3306/starlink"

# Create engine
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Base class for models
Base = declarative_base()

# SessionLocal for DB sessions
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

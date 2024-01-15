from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


#('SQLALCHEMY_DATABASE_URL' mein database se connect karne ke liye ek URL hai. 
# Jismein 'username', 'password', 'localhost', aur 'dbname' placeholders hain. 
# Jaise hi aap is URL ko set karenge, aap database se connect ho jaayenge.)
SQLALCHEMY_DATABASE_URL = os.getenv("SQLALCHEMY_DATABASE_URL")


#('engine' mein humne 'create_engine' function ka use karke database engine create kiya hai.
# Is engine ki madad se hum database se connect karenge.)
engine = create_engine(SQLALCHEMY_DATABASE_URL)


#('SessionLocal' ek sessionmaker hai jo database se interact karne ke liye banaya gaya hai. 
# FastAPI ke dependencies mein is session ka use hota hai.)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# ('Base' ek declarative_base hai jo SQLAlchemy mein declarative models ke liye base class provide karta hai.)
Base = declarative_base()



# ("Todo" ek model hai jo "Base" class ka subclass hai. Ismein humne "todos" table
# ke columns (id, title, description) ko define kiya hai.)
class Todo(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
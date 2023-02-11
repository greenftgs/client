import os
import sqlalchemy
from dotenv import loaddotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

load_dotenv()

user = os.getenv('User', 'postgres')
password = os.getenv('Password', 'postgres')
db_name = os.getenv('db_name', 'orm')
localhost = os.getenv('localhost')
port = os.getenv('port', 5432)

DATABASE_URL = f'postgresql://{user}:{password}@{localhost}:{port}/{db_name}'

engine = sqlalchemy.create_engine(DATABASE_URL)

Session = sessionmaker(bind=engine)
db = Session()
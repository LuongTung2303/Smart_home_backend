import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    DB_HOST = os.getenv("DB_HOST")
    DB_PORT = int(os.getenv("DB_PORT", 3306))
    DB_USER = os.getenv("DB_USER")
    DB_PASSWORD = os.getenv("DB_PASSWORD")
    DB_NAME = os.getenv("DB_NAME")
    SECRET_KEY = os.getenv("SECRET_KEY")

    ADA_IO_USERNAME = os.getenv("ADA_IO_USERNAME")
    ADA_IO_KEY = os.getenv("ADA_IO_KEY")

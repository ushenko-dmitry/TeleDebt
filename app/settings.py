import os

from dotenv import load_dotenv

load_dotenv()

APP_TOKEN = os.getenv("APP_TOKEN", "")

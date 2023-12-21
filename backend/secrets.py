from dotenv import load_dotenv
import os

load_dotenv()  # take environment variables from .env.

# to read the env variables is as simple as:
DB_HOST = os.environ.get("DB_HOST")
DB_NAME = os.environ.get("DB_NAME")
DB_PORT = os.environ.get("DB_PORT")

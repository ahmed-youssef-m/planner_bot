from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()


CONNECTION_STRING = os.getenv("MONGO_URI")
DATABASE_NAME = os.getenv("DB_NAME")
WEDDINGS_COLLECTION_NAME = "weddings"
VENUES_COLLECTION_NAME = "venues"
SESSIONS_COLLECTION_NAME="sessions"

def connect_to_mongodb(collection_name):
    try:
        client = MongoClient(CONNECTION_STRING)
        db = client[DATABASE_NAME]
        return db[collection_name]
    except Exception as e:
        print(f"Error connecting to MongoDB: {e}")
        return None

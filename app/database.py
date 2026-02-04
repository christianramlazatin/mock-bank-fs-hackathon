from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv
import os

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
DB_NAME = os.getenv("DB_NAME", "mock_db")

if not MONGO_URI:
    raise RuntimeError("MONGO_URI not set in .env")

# MongoDB client
client = AsyncIOMotorClient(MONGO_URI, serverSelectionTimeoutMS=5000)

# Database object
db = client[DB_NAME]

# Collections
accounts_collection = db.accounts
transactions_collection = db.transactions

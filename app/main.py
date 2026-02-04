from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.routes import accounts, transactions
from app.database import client


@asynccontextmanager
async def lifespan(app: FastAPI):
    await client.admin.command("ping")
    print("✅ Connected to MongoDB Atlas")
    yield


app = FastAPI(title="Mock Bank Backend", lifespan=lifespan)

# include routers
app.include_router(accounts.router)
app.include_router(transactions.router)


@app.get("/")
def root():
    return {"status": "Mock Bank API running"}

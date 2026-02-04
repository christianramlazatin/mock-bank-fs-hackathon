from fastapi import APIRouter, HTTPException
from app.database import accounts_collection

# Create router
router = APIRouter(prefix="/balance", tags=["Accounts"])


@router.get("/{account_id}")
async def check_balance(account_id: str):
    acc = await accounts_collection.find_one({"account_id": account_id}, {"_id": 0})
    if not acc:
        raise HTTPException(status_code=404, detail="Account not found")
    return acc

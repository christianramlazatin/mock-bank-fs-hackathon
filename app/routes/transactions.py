from fastapi import APIRouter, HTTPException
from app.database import accounts_collection, transactions_collection
from app.models import TransferRequest
from datetime import datetime
import uuid

router = APIRouter(tags=["Transactions"])

router = APIRouter(tags=["Transactions"])


@router.post("/transfer")
async def transfer_funds(req: TransferRequest):
    if req.amount <= 0:
        raise HTTPException(status_code=400, detail="Invalid amount")

    sender = await accounts_collection.find_one({"account_id": req.from_account})
    receiver = await accounts_collection.find_one({"account_id": req.to_account})

    if not sender:
        raise HTTPException(status_code=400, detail="Invalid account ID for sender")

    if not receiver:
        raise HTTPException(status_code=400, detail="Invalid account ID for receiver")

    if sender["balance"] < req.amount:
        raise HTTPException(status_code=400, detail="Insufficient balance")

    await accounts_collection.update_one(
        {"account_id": req.from_account}, {"$inc": {"balance": -req.amount}}
    )

    await accounts_collection.update_one(
        {"account_id": req.to_account}, {"$inc": {"balance": req.amount}}
    )

    timestamp = datetime.utcnow().isoformat()

    await transactions_collection.insert_many(
        [
            {
                "txn_id": str(uuid.uuid4()),
                "account_id": req.from_account,
                "type": "DEBIT",
                "amount": req.amount,
                "description": f"Transfer to {req.to_account}",
                "timestamp": timestamp,
            },
            {
                "txn_id": str(uuid.uuid4()),
                "account_id": req.to_account,
                "type": "CREDIT",
                "amount": req.amount,
                "description": f"Transfer from {req.from_account}",
                "timestamp": timestamp,
            },
        ]
    )

    return {"message": "Transfer successful"}


@router.get("/transactions/{account_id}")
async def transaction_history(account_id: str):
    acc = await accounts_collection.find_one({"account_id": account_id})
    if not acc:
        raise HTTPException(status_code=404, detail="Account not found")

    cursor = transactions_collection.find({"account_id": account_id}, {"_id": 0}).sort(
        "timestamp", -1
    )

    transactions = await cursor.to_list(length=100)

    return {"account_id": account_id, "transactions": transactions}

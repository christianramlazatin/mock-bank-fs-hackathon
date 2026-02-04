from pydantic import BaseModel


class TransferRequest(BaseModel):
    from_account: str
    to_account: str
    amount: int

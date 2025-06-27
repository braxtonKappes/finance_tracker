from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import schemas, crud, database
from ..utils import get_current_user

router = APIRouter(prefix="/transactions", tags=["transactions"])

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.TransactionOut)
def create_transaction(
    tx: schemas.TransactionCreate,
    db: Session = Depends(get_db),
    user_id: int = Depends(get_current_user)
):
    return crud.create_transaction(db, user_id, tx)

@router.get("/", response_model=list[schemas.TransactionOut])
def read_transactions(
    db: Session = Depends(get_db),
    user_id: int = Depends(get_current_user)
):
    return crud.get_transactions(db, user_id)

@router.put("/{tx_id}", response_model=schemas.TransactionOut)
def update_transaction(
    tx_id: int,
    updated_tx: schemas.TransactionCreate,
    db: Session = Depends(get_db),
    user_id: int = Depends(get_current_user)
):
    return crud.update_transaction(db, user_id, tx_id, updated_tx)

@router.delete("/{tx_id}")
def delete_transaction(
    tx_id: int,
    db: Session = Depends(get_db),
    user_id: int = Depends(get_current_user)
):
    return crud.delete_transaction(db, user_id, tx_id)

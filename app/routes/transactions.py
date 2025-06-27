from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import schemas, crud, database

router = APIRouter(prefix="/transactions")

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.TransactionOut)
def add_tx(tx: schemas.TransactionCreate, db: Session = Depends(get_db)):
    user_id = 1  # Temporary until JWT setup
    return crud.create_transaction(db, user_id, tx)

@router.get("/", response_model=list[schemas.TransactionOut])
def get_txs(db: Session = Depends(get_db)):
    user_id = 1
    return crud.get_transactions(db, user_id)

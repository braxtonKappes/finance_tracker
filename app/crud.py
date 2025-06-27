from sqlalchemy.orm import Session
from . import models, schemas
from passlib.context import CryptContext
from fastapi import HTTPException

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = pwd_context.hash(user.password)
    db_user = models.User(email=user.email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def create_transaction(db: Session, user_id: int, transaction: schemas.TransactionCreate):
    db_tx = models.Transaction(**transaction.dict(), user_id=user_id)
    db.add(db_tx)
    db.commit()
    db.refresh(db_tx)
    return db_tx


def get_transactions(db: Session, user_id: int):
    return db.query(models.Transaction).filter(models.Transaction.user_id == user_id).all()


def update_transaction(db: Session, user_id: int, tx_id: int, updated_tx: schemas.TransactionCreate):
    tx_record = db.query(models.Transaction).filter(
        models.Transaction.id == tx_id,
        models.Transaction.user_id == user_id
    ).first()

    if not tx_record:
        raise HTTPException(status_code=404, detail="Transaction not found")

    setattr(tx_record, "title", updated_tx.title)
    setattr(tx_record, "amount", updated_tx.amount)

    db.commit()
    db.refresh(tx_record)
    return tx_record


def delete_transaction(db: Session, user_id: int, tx_id: int):
    tx_record = db.query(models.Transaction).filter(
        models.Transaction.id == tx_id,
        models.Transaction.user_id == user_id
    ).first()

    if not tx_record:
        raise HTTPException(status_code=404, detail="Transaction not found")

    db.delete(tx_record)
    db.commit()
    return {"message": "Transaction deleted successfully"}

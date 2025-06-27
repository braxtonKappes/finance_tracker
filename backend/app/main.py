from fastapi import FastAPI
from .routes import auth, transactions
from .database import engine
from .models import Base

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Finance Tracker API",
    version="1.0.0"
)

app.include_router(auth.router, tags=["auth"])
app.include_router(transactions.router, tags=["transactions"])

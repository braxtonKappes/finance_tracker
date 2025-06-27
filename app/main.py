from fastapi import FastAPI
from .routes import auth, transactions
from .database import engine
from .models import Base

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(auth.router)
app.include_router(transactions.router)

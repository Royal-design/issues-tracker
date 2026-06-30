from fastapi import FastAPI
from app.api.router import router
from app.database import Base, engine
from app.seed import init_db 


Base.metadata.create_all(bind=engine)
app = FastAPI()

app.include_router(router)


init_db()


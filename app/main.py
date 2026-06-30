from fastapi import FastAPI
from app.api.router import router
from app.database import Base, engine

from app.middlewares.cors import configure_cors
from app.middlewares.process_time import add_process_time_header
from app.seed import init_db 


Base.metadata.create_all(bind=engine)
app = FastAPI()

configure_cors(app)
app.middleware("http")(add_process_time_header)
app.include_router(router)


init_db()


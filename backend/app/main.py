from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes.health import router as health_router

app = FastAPI(title="LifeOps API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(health_router, prefix="/api/v1")

from app.routes.actions import router as actions_router
app.include_router(actions_router)

from app.routes.inbox import router as inbox_router
app.include_router(inbox_router)

from app.services.storage import init_db
@app.on_event('startup')
def _startup():
    init_db()

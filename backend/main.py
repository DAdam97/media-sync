from contextlib import asynccontextmanager

from fastapi import Depends, FastAPI, HTTPException, Security
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from config import settings
from database import init_db
from routers import downloads, library, playlists


@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield


app = FastAPI(title="MediaSync", version="0.1.0", lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

_bearer = HTTPBearer()


def verify_api_key(credentials: HTTPAuthorizationCredentials = Security(_bearer)) -> None:
    if not settings.api_key or credentials.credentials != settings.api_key:
        raise HTTPException(status_code=401, detail="Invalid API key")


@app.get("/api/health")
async def health() -> dict[str, str]:
    return {"status": "ok"}


app.include_router(downloads.router, dependencies=[Depends(verify_api_key)])
app.include_router(library.router, dependencies=[Depends(verify_api_key)])
app.include_router(playlists.router, dependencies=[Depends(verify_api_key)])

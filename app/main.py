from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app import seed
from app.config import settings
from app.routers import contact, projects

app = FastAPI(title="Chris Hoang Portfolio API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origin_list,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(projects.router)
app.include_router(contact.router)


@app.on_event("startup")
def on_startup():
    # Creates tables on first boot, then keeps the project list in sync with
    # seed.py on every deploy — that's the whole "add a project" workflow.
    seed.run()


@app.get("/api/health")
def health():
    return {"status": "ok"}

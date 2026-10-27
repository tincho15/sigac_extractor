from fastapi import FastAPI

from app.presentation.routes.health import router as health_router

app = FastAPI(title="SIGAC Extractor")
app.include_router(health_router)

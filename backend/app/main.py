from fastapi import FastAPI
from app.api.api_v1.api import api_router

# สร้าง FastAPI application instance
app = FastAPI(
    title="Unified IT Asset Management (U-ITAM) API",
    description="API for managing IT assets across the organization.",
    version="1.0.0",
)


@app.get("/", tags=["Root"])
def read_root():
    """
    Root endpoint to check if the API is running.
    """
    return {"message": "Welcome to U-ITAM API!"}


# รวม API routers
app.include_router(api_router, prefix="/api/v1")
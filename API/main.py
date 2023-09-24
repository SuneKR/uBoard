from fastapi import FastAPI
from pymongo import MongoClient
from motor.motor_asyncio import AsyncIOMotorClient
from routers import router as pieceRouter

app = FastAPI()


@app.on_event("startup")
async def statup_db_client():
    app.mongodb_client = AsyncIOMotorClient("mongodb://localhost:27017")
    app.mongodb = app.mongodb_client["uBoard"]

@app.on_event("shutdown")
async def shutdown_db_client():
    app.mongodb_client.close()
    
app.include_router(pieceRouter, tags=["pieces"], prefix="/piece")

@app.get("/", tags=["Root"])
async def getStatus(): return { "status": "running"}

@app.get("/status")
async def getStatus(): return { "status": "running"}
from fastapi import FastAPI

app = FastAPI()

@app.get("/first-endpoint")
async def root(): return {"message": "Initial Test"}
from fastapi import FastAPI
import uvicorn

from async_scrap_on_fastapi.db.connection import database
from async_scrap_on_fastapi.endpoints.retrieve import router

app = FastAPI()


@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


@app.get('/')
def home():
    return {'status': 'OK'}

app.include_router(router)



if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, host="0.0.0.0", reload=True)
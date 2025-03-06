from fastapi import FastAPI
import uvicorn
from routers.main_router import api_router
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(
    title = 'space',
    version='0.0.1'
)

app.include_router(api_router)

if __name__ == "__main__":
    uvicorn.run("main:app",
                host="0.0.0.0",
                port=8000,
                reload = True)

# @app.get("/")
# async def read_item(item_id):
#     return {"item_id": item_id}
from typing import Optional
from fastapi import FastAPI
from app.database import Base, Engine
from app.routers import router
from starlette.staticfiles import StaticFiles


app = FastAPI()



def get_app() -> FastAPI:
    # Create API
    server = FastAPI(
        title='NBA-app-api',
        debug=bool,
        docs_url='/nba-app-docs',
        redoc_url='/nba-app-redocs'
    )

    server.include_router(router)

    @server.get("/")
    async def read_root():
        return {"Hello": "World"}

    return server


app = get_app()
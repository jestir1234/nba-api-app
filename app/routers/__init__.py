from fastapi import APIRouter
from app.routers.per_game_routes import router as per_game_router
from app.routers.player_routes import router as player_router


router = APIRouter()

router.include_router(
    per_game_router,
    prefix='/per_game',
    tags=['per_game'],
)

router.include_router(
    player_router,
    prefix='/player',
    tags=['player'],
)
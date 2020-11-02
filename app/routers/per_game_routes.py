from fastapi import APIRouter, Query, Depends, Body
import app.controllers.per_game_controller as controller
from app.schemas.per_game import PerGame
from starlette.requests import Request
from sqlalchemy.orm import Session

router = APIRouter()

@router.get('/id/{per_game_id}', response_model=PerGame)
async def get_per_game_by_id(
    *,
    request: Request
):
    return controller.get_per_game_by_id(request)


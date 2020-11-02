from fastapi import APIRouter, Query, Depends, Body
import app.controllers.player_controller as controller
from app.schemas.player import Player
from starlette.requests import Request
from sqlalchemy.orm import Session
from app.database import get_session

router = APIRouter()

@router.get('/id/{player_id}', response_model=Player)
async def get_user_data(
    *,
    request: Request,
    session: Session = Depends(get_session),
    player_id: int = Query(None, title='Player id', ge=0),
):
    return controller.get_player_by_id(request, session, player_id)


from fastapi import APIRouter
from model import user

router = APIRouter()


@router.get("/users/{username}", tags=["user"])
async def read_user(username: str):
    return user.get_user_info(username)

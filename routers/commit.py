from fastapi import APIRouter
from model import commit

router = APIRouter()


@router.get("/commits/{username}", tags=["user"])
async def get_commit(username: str):
    return commit.list_commits(username)

from fastapi import FastAPI
from routers import user, commit

app = FastAPI()

app.include_router(user.router)
app.include_router(commit.router)

@app.get("/")
async def root():
    return {}
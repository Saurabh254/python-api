import uvicorn
from fastapi import FastAPI
from .routers import page


# creating app object
app = FastAPI()
# including out page router
app.include_router(page.router)

# temp route


@app.get('/')
async def root():
    return {"message": "Head to /page/{page_number}"}

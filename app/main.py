import uvicorn
from fastapi import FastAPI
from .routers import page, importPage, removePage


# creating app object
app = FastAPI()
# including routers
app.include_router(page.router)
app.include_router(importPage.router)
app.include_router(removePage.router)


# temp route
@app.get('/')
async def root():
    return {"message": "Head to /page/{page_number}"}

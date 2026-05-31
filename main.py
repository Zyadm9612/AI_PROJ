from fastapi import FastAPI

from recommendation_service import router as recommendation_router
from new_chat import router as chat_router
from analysis import router as analysis_router

app = FastAPI(title="Phoenix AI Services")

app.include_router(recommendation_router)
app.include_router(chat_router)
app.include_router(analysis_router) 
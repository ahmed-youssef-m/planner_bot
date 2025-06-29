# from fastapi import FastAPI
# from routes import router
#
# app = FastAPI()
#
# app.include_router(router)

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import router  # your existing router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)

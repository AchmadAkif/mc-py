from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from api.v1 import compile

app = FastAPI()

app.include_router(compile.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"], # allow frontend access
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"Hello": "World"}

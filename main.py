#!/usr/bin/python
# -*- coding: UTF-8 -*-

from fastapi.exceptions import HTTPException
from starlette.responses import JSONResponse
from motor.motor_asyncio import AsyncIOMotorClient
from odmantic import AIOEngine, ObjectId
from fastapi.responses import HTMLResponse
from fastapi import FastAPI
import uvicorn
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware
from router import router_restaurants


load_dotenv()

origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:3000",
    "*"
]

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

API_VERSION = "/api/v1"
app.include_router(router_restaurants.router, prefix=API_VERSION)


@app.get("/", response_class=HTMLResponse)
async def home():
    return """
        <html>
            <head>
                <title>UNIIEAT</title>
            </head>
            <body>
                <div style="width:800px; margin:0 auto;">
                    <h1>Welcome to UNIIEAT Backend API Server</h1>
                    This is a backend API server, please get the API token then use these APIs.</br>
                    If you want to get the detail, please reference "http://host-ip:8000/docs".</br>
                    Remember to change the host ip address.</br>
                </div>
            </body>
        </html>
    """

#!/usr/bin/python
# -*- coding: UTF-8 -*-

from ODM.RestaurantData import *
from fastapi import APIRouter, FastAPI, File, Form, UploadFile
from fastapi import Depends
from odmantic import AIOEngine, ObjectId
from starlette.responses import JSONResponse
from motor.motor_asyncio import AsyncIOMotorClient
import os
from odmantic import AIOEngine, ObjectId
from internal.mongo_connection import MongoEngine
from internal.errorCode import ErrorCode


router = APIRouter(
    prefix="/restaurant",
    tags=["restaurant"],
    responses={404: {"description": "Not found"}},
)


@router.get("/", response_class=JSONResponse)
async def get_flight_data():
    restaurantData = await MongoEngine.getEngine().find(RestaurantData)
    return restaurantData

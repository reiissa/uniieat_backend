#!/usr/bin/python
# -*- coding: UTF-8 -*-

from ODM.RestaurantData import *
from fastapi import APIRouter, FastAPI
from starlette.responses import JSONResponse
from odmantic import ObjectId, Model, AIOEngine
from internal.mongo_connection import MongoEngine
from internal.errorCode import ErrorCode
import uvicorn


router = APIRouter(
    prefix="/restaurant",
    tags=["Restaurant"],
    responses={404: {"description": "Not found"}},
)


# insert
@router.post("/", response_class=JSONResponse)
async def insert_restaurant(restaurantData: RestaurantData):
    print(restaurantData)
    await MongoEngine.getEngine().save(restaurantData)
    return restaurantData


# select all
@router.get("/", response_class=JSONResponse)
async def get_restaurant():
    restaurantData = await MongoEngine.getEngine().find(RestaurantData)
    return restaurantData


# select by id
@router.get("/storeID/{storeID}", response_class=JSONResponse)
async def get_restaurant_by_id(storeID: str):
    restaurantData = await MongoEngine.getEngine().find_one(RestaurantData, RestaurantData.storeID == storeID)
    if restaurantData is None:
        return {
            "error code": hex(ErrorCode.noDataFound),
            "storeID is not found": storeID
        }
    else:
        return restaurantData


# select by name
@router.get("/name/{name}", response_class=JSONResponse)
async def get_restaurant_by_name(name: str):
    restaurantData = await MongoEngine.getEngine().find_one(RestaurantData, RestaurantData.name == name)
    if restaurantData is None:
        return {
            "error code": hex(ErrorCode.noDataFound),
            "Restaurant is not found": name
        }
    else:
        return restaurantData


# # update
# @router.patch("/id/{id}", response_model=RestaurantData)
# async def update_tree_by_id(id: str, patch: RestaurantData):
#     restaurantData = await MongoEngine.getEngine().find_one(RestaurantData, RestaurantData.id == ObjectId(id))
#     if restaurantData is None:
#         return {
#             "error code": hex(ErrorCode.noDataFound),
#             "storeID is not found": id
#         }

#     patch_dict = patch.dict(exclude_unset=True)
#     for name, value in patch_dict.items():
#         setattr(restaurantData, name, value)
#     await MongoEngine.getEngine().save(restaurantData)
#     return restaurantData

#!/usr/bin/python
# -*- coding: UTF-8 -*-
from pymongo import MongoClient
from motor.motor_asyncio import AsyncIOMotorClient
from odmantic import AIOEngine, ObjectId
import os
from dotenv import load_dotenv
load_dotenv()


class MongoEngine:

    MONGO_USERNAME = os.getenv("MONGO_USERNAME")
    MONGO_PASSWORD = os.getenv("MONGO_PASSWORD")
    MONGO_HOST = os.getenv("MONGO_HOST")
    MONGO_AUTHSOURCE = os.getenv("MONGO_AUTHSOURCE")

    client = AsyncIOMotorClient(host=MONGO_HOST, port=27017, connect=True,
                                username=MONGO_USERNAME, password=MONGO_PASSWORD, authSource=MONGO_AUTHSOURCE)
    engine = AIOEngine(motor_client=client, database="unieat")

    _instance = None

    def __init__(self):
        if MongoEngine._instance is not None:
            raise Exception('only one instance can exist')
        else:
            self._id = id(self)
            MongoEngine._instance = self

    def get_id(self):
        return self._id

    @staticmethod
    def getEngine():
        if MongoEngine._instance is None:
            MongoEngine()
        return MongoEngine._instance.engine

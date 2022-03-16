#!/usr/bin/python
# -*- coding: UTF-8 -*-

from typing import Optional
from odmantic import Model, Field, EmbeddedModel, ObjectId


class _status(EmbeddedModel):
    Mon: Optional[str] = Field("", example="06:00–23:00")
    Tue: Optional[str] = Field("", example="06:00–23:00")
    Wen: Optional[str] = Field("", example="06:00–23:00")
    Thu: Optional[str] = Field("", example="806:00–23:00")
    Feb: Optional[str] = Field("", example="06:00–23:00")
    Sat: Optional[str] = Field("", example="06:00–23:00")
    Sun: Optional[str] = Field("", example="06:00–23:00")


class _address(EmbeddedModel):
    area: Optional[str] = Field("", example="100")
    name: Optional[str] = Field("", example="台北市中正區南昌路一段44號")


class RestaurantData(Model):
    name: Optional[str] = Field("", example="摩斯漢堡")
    open: Optional[str] = Field("", example="true")
    phone: Optional[str] = Field("", example="02 2394 4845")
    image: Optional[str] = Field("", example="")
    score: Optional[str] = Field("", example="52039")
    status: Optional[_status] = Field(
        None, key_name="status", example=_status())
    address: Optional[_address] = Field(
        None, key_name="address", example=_address())

    class Config:
        collection = "restaurants"

#!/usr/bin/python
# -*- coding: UTF-8 -*-

class ErrorCode:
    
    success = 0x00000000
    error = 0x10000000
    loginError = error | 1
    idNotFound = error | 2
    noDataFound = error | 4
    
    
    
    pass
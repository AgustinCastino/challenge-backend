from service import loginService
from flask import request

def login():
    return loginService.login()
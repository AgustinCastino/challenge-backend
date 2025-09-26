from exceptions.exceptions import NotFoundError, HttpError, ServerError
from flask import jsonify


def handleError(e):
    if isinstance(e, NotFoundError):
        return e.to_dict()
    
    if isinstance(e, HttpError):
        return e.to_dict()
    
    raise ServerError("Error inesperado")
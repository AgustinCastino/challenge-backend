class ServiceError(Exception):
    def __init__(self, message, http_status = 400):
        self.message = message
        self.http_status = http_status
        super().__init__(message)

    def to_dict(self):
        return {
            "error": self.__class__.__name__,  
            "message": self.message,
            "http_status": self.http_status
        }

class NotFoundError(ServiceError):
    def __init__(self, message="Recurso no encontrado"):
        super().__init__(message, http_status=404)
        
class ServerError(ServiceError):
    def __init__(self, message="Error interno del servidor"):
        super().__init__(message, http_status=500)

class HttpError(ServiceError):
    def __init__(self, message="Error HTTP", http_status=400):
        super().__init__(message, http_status=http_status)

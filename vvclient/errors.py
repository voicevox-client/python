class HTTPException(Exception):
    def __init__(self, message, status_code):
        self.message = message
        self.status_code = status_code
        super().__init__(message)

    def __str__(self):
        return f"{self.status_code}: {self.message}"


class NotFoundError(HTTPException):
    def __init__(self, message: str):
        super().__init__(message, 404)

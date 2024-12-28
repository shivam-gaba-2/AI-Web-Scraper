from fastapi import HTTPException

class UnauthorizedException(HTTPException):
    def __init__(self, detail: str = "Unauthorized"):
        super().__init__(status_code=401, detail=detail)

class BadRequestException(HTTPException):
    def __init__(self, detail: str = "Bad Request"):
        super().__init__(status_code=400, detail=detail)

class InvalidUrlException(HTTPException):
    def __init__(self, detail: str = "Invalid URL"):
        super().__init__(status_code=404, detail=detail)

class RequestTimeoutException(HTTPException):
    def __init__(self, detail: str = "Request timed out"):
        super().__init__(status_code=408, detail=detail)

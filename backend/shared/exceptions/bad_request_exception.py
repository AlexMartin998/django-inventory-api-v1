from .custom_exception import CustomException


class BadRequestException(CustomException):
    def __init__(self, message: str = "Bad Request"):
        super().__init__(message)

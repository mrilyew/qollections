class ApiException(Exception):
    def __init__(self, message):
        super().__init__(message)

class NotFoundException(Exception):
    def __init__(self, message):
        super().__init__(message)

class InvalidPassedParam(Exception):
    def __init__(self, message):
        super().__init__(message)

class NotPassedException(Exception):
    def __init__(self, message):
        super().__init__(message)

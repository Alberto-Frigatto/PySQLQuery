from abc import ABCMeta


class ConstraintException(Exception, metaclass=ABCMeta):
    def __init__(self, message: str) -> None:
        super().__init__(message)

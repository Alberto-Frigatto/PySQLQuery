from abc import ABCMeta, abstractmethod


class Constraint(metaclass=ABCMeta):
    @abstractmethod
    def __str__(self) -> str:
        pass

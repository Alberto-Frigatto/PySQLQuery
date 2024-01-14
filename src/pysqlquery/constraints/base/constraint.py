'''
Defines the abstract base class for constructing abstract SQL constraint classes.
'''

from abc import ABCMeta, abstractmethod


class Constraint(metaclass=ABCMeta):
    '''
    Abstract class for construct abstract SQL constraint classes.

    This class provides the basic structure for construct
    abstract classes for kind of SQL constraints.

    This class must be inherited by abstract one.
    '''

    @abstractmethod
    def __str__(self) -> str:
        '''
        Returns
        -------
        str
            A string representation of the class instance in SQL format.
        '''

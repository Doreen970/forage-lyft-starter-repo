#a function that shows whether a car needs to be serviced or not

from abc import ABC, abstractmethod


class Serviceable(ABC):
    @abstractmethod
    def needs_service(self):
        pass
from abc import ABC, abstractmethod

class ResourcesInterface(ABC):

    isAvailable: bool

    @abstractmethod
    def addResource(self):
        pass

    @abstractmethod
    def available(self, isAvailable: bool):
        pass

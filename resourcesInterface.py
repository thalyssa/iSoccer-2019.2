from abc import ABC, abstractmethod

class ResourcesInterface(ABC):

    isAvailable: bool

    @abstractmethod
    def addResource(self):
        pass

    def available(self, isAvailable: bool):
        self.isAvailable = isAvailable
        #TODO: ESCREVER A INFORMAÇÃO NO JSON

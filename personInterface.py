from abc import ABC, abstractmethod


class PersonInterface(ABC):
    name: str
    email: str
    cpf: str
    phone: str

    @abstractmethod
    def register(self):
        pass

    def writeOnFile(self):
        pass
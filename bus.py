import resourcesInterface

class Bus(resourcesInterface):

    licensePlate: str
    qtdSeats: int

    def addResource(self):

        self.licensePlate = input('\nDigite a placa do ônibus: ')
        self.qtdSeats = int(input('\nAgora digite a quantidade de assentos: '))


        #TODO - ESCREVER A INFORMAÇÃO NO JSON



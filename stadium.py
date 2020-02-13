import resourcesInterface

class Stadium(resourcesInterface):

    def __init__(self):
        self.isAvailable = True

    stadiumName: str
    qtdSeats: int
    qtdToilets: int
    qtdBars: int

    def addResource(self):

        print('\n--- CADASTRO DE ESTÁDIO ---\n')

        self.stadiumName = input('\nDigite o nome do estádio: ')
        self.qtdSeats = int(input('\nAgora digite a quantidade de torcedores suportados: '))
        self.qtdToilets = int(input('\nDigite também a quantidade de banheiros: '))
        self.qtdBars = int(input('\nPor último, a quantidade de lanchonetes: '))

        #TODO - ESCREVER OS DADOS NUM JSON
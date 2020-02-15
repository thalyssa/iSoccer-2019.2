from personInterface import PersonInterface
from view import View


class PartnerConcrete(PersonInterface, View):
    address: str
    tax_value: str

    def register(self):
        input('Digite as informações do sócio a ser cadastrado à seguir')
        self.name = input('Nome:')
        self.address = input('Endereço: ')
        self.email = input('E-mail: ')
        self.cpf = input('CPF: ')
        self.salary = input('Taxa de contribuição: ')
        self.phone = input('Telefone: ')

        self.writeOnFile()

        print('Sócio cadastrado!')
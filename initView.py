from view import View
from loggedView import LoggedView


class InitView(View):
    def prompt(self):
        print("Bem vindo ao iSoccer!\nPor favor, escolha uma opção: ")
        print("1 - Login")
        print("2 - Sair")


        option = input("\n")
        return option

    def run(self, option: str):
        if option.strip() == '1':
            self.login()
        elif option == '2':
            self.state.running = False
        else:
            print('Opção inválida')

    def login(self):
        username = input('Digite o usuário: ')
        password = input('Digite a senha: ')

        if username == 'admin' and password == 'admin':
            v = LoggedView(self.state)
            self.switch_view(v)
        else:
            print('Erro nas credenciais')

from view import View
from employees.employeeFactory import EmployeeFactory


class EmployeeManagmentView(View):
    e = EmployeeFactory()

    def prompt(self):
        print('GERENCIAMENTO DE FUNCIONÁRIOS')
        print('1 - Cadastro de funcionários')
        print('2 - Alterar status de jogador (apto/inapto)')
        print('3 - Voltar')

        option = input('\n')
        return option

    def run(self, option):
        if option == '1':
            self.e.prompt()
        elif option == '2':
            pass
        elif option == '3':
            self.back()

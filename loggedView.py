from view import View
from employees.employeeManagmentView import EmployeeManagmentView
from partner.partnerManagmentView import PartnerManagmentView


class LoggedView(View):
    def prompt(self):
        print('\niSoccer')
        print('PAINEL PRINCIPAL')
        print('Escolha sua opção:')
        print('1 - Gerenciamento de funcionários')
        print('2 - Gerenciamento de sócio-torcedores')
        print('3 - Gerenciamento de recursos')
        print('4 - Gerador de relatórios')
        print('5 - Voltar')

        option = input('\n')
        return option

    def run(self, option):
        if option == '1':
            v = EmployeeManagmentView(self.state)
            self.switch_view(v)
        elif option == '2':
            v = PartnerManagmentView(self.state)
            self.switch_view(v)
        elif option == '3':
            pass
        elif option == '4':
            pass
        elif option == '5':
            self.back()

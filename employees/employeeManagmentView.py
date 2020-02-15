from view import View
from employees.employeeFactory import EmployeeFactory
import json


class EmployeeManagmentView(View):

    def prompt(self):
        print('GERENCIAMENTO DE FUNCIONÁRIOS')
        print('1 - Cadastro de funcionários')
        print('2 - Alterar status de jogador (apto/inapto)')
        print('3 - Voltar')

        option = input('\n')
        return option

    def run(self, option):
        if option == '1':
            v = EmployeeFactory(self.state)
            self.switch_view(v)
        elif option == '2':
            self.changePlayerStatus()
        elif option == '3':
            self.back()

    def changePlayerStatus(self):

        cpf = input('Digite o CPF do jogador em questão: ')

        with open(self.state.employees_json_path, 'r') as file:
            employees_data = json.load(file)

        player = []

        for employee in employees_data['jogadores']:
            if cpf in employee:
                employee.append(employee)

        length = len(player)

        if length < 1:
            print('\nNenhum resultado encontrado.')
            return
        else:
            status = bool(player[1]['canPlay'])
            if status is True:
                print('O jogador se encontra apto à jogar. Você está prestes a declará-lo inapto, tem certeza?')
            else:
                print('O jogador se encontra inapto à jogar. Você está prestes a declará-lo apto, tem certeza?')

            print('1 - Sim')
            print('2 - Não')

            option = input('\n')

            if option == '1':
                employees_data['jogadores']['canPlay'] = not status
            elif option == '2':
                self.back()
            else:
                print('Opção inválida')

        with open(self.state.employees_json_path, 'w') as file:
            json.dump(employees_data, file)

        print('Status alterado com sucesso')

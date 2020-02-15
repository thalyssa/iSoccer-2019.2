from employees.employeeConcrete import EmployeeConcrete
import state


class EmployeeFactory(EmployeeConcrete):
    s = state.State()
    e = EmployeeConcrete(s)

    def prompt(self):
        print('Primeiramente defina o cargo do funcionário a ser cadastrado: ')
        print('1 - Presidente')
        print('2 - Médico')
        print('3 - Técnico')
        print('4 - Preparadores Físicos')
        print('5 - Motoristas')
        print('6 - Cozinheiros')
        print('7 - Advogados')
        print('8 - Jogador')

        option = input('\n')
        return option

    def run(self, option):
        if int(option) in range(1, 9):
            self.e.defineRole(option)
        else:
            print('Opção inválida')
from personInterface import PersonInterface
from view import View
import json
import state
from employees.doctorConcrete import DoctorConcrete
from employees.driverConcrete import DriverConcrete
from employees.playerConcrete import PlayerConcrete

class EmployeeConcrete(PersonInterface, View):
    salary: str
    employee_role: str

    def register(self):

        input('Digite as informações do funcionário a ser cadastrado à seguir')
        self.name = input('Nome:')
        self.email = input('E-mail: ')
        self.cpf = input('CPF: ')
        self.salary = input('Salário: ')
        self.phone = input('Telefone: ')

        self.writeOnFile()

        print('Funcionário cadastrado!')

    def defineRole(self, option: str):

        with open(state.roles_json_path, 'r')as file:
            employee_roles_dict = json.load(file)

        self.employee_role = employee_roles_dict[option]

        if option == '2':
            m = DoctorConcrete()
            return m.register()
        if option == '5':
            m = DriverConcrete()
            return m.register()
        if option == '8':
            j = PlayerConcrete()
            return j.register()
        else:
            self.register()

    def writeOnFile(self):

        with open(state.employees_json_path, 'r') as file:
            employee_info = json.load(file)

        employee_data = {'Nome': self.name, 'E-mail': self.email, 'CPF': self.cpf, 'Salário': self.salary,
                         'Telefone': self.phone}

        var = employee_info[self.employee_role].append(employee_data)

        with open(state.employees_json_path, 'w') as file:
            json.dump(var, file)

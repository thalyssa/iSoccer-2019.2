from view import View
import json


class PartnerManagmentView(View):

    def prompt(self):
        print('GERENCIAMENTO DE SÓCIO-TORCEDORES')
        print('1 - Cadastro de sócio-torcedor')
        print('2 - Alterar status do pagamento (Adimplente/Inadimplente)')
        print('3 - Alterar valor da contribuição')
        print('4 - Voltar')

        option = input('\n')
        return option

    def run(self, option):
        if option == '1':
            pass
        elif option == '2':
            pass
        elif option == '3':
            pass
        elif option == '4':
            pass
        else:
            print('Opção inválida')


    def changeTaxValue(self):

        print('ALTERAÇÃO DE TAXA')
        print('Selecione o tipo de sócio que terá a taxa alterada: ')
        print('1 - Júnior')
        print('2 - Sênior')
        print('3 - Elite')

        option = input('\n')

        if int(option) in range(1, 4):
            with open(self.state.fan_partners_json_pat, 'r') as file:
                partners_data = json.load(file)

            partners_list = []

            for partner in partners_data[int(option)]:
                partners_list.append(partner)

            length = len(partners_list)

            if length < 1:
                print('\nNenhum resultado encontrado.')
                return
            else:
                pass
        else:
            print('Opção inválida')
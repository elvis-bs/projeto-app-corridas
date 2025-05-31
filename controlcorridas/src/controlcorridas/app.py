"""
controle de gastos e ganho das corridas de uber
"""

from datetime import date, datetime
import requests
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW


class controlcorridas(toga.App):
    def startup(self): 
        main_box = toga.Box(style=Pack(direction=COLUMN))
        main_box.add(toga.Label('INSIRA OS DADOS DO DIA'))

        main_box.add(toga.Label('insira o dia da corrida'))
        self.data_criacao = toga.DateInput()
        main_box.add(
        self.data_criacao
        )
        

        main_box.add(toga.Label('insira os dados de abastecimento'))
        self.gasolina = toga.NumberInput()
        main_box.add(
        self.gasolina
        )

        self.km_label = toga.Label('insira os km')
        main_box.add(
            self.km_label
        )
        self.km = toga.NumberInput()
        main_box.add(
            self.km
        )


        self.ganho_label = toga.Label('insira o ganho do dia')
        main_box.add(
            self.ganho_label
        )
        self.ganho = toga.NumberInput('INSIRA O VALOR DO DO GANHO')
        main_box.add(
        self.ganho
        )

        
        main_box.add(  
                toga.Button('Registrar',on_press=self.enviar)   
        )
        

        

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()
    
    def enviar(self,widget):
        data = dict ()
        self.main_window.info_dialog('controle de corridas','dados inseridos com sucesso')
        print(f"controle de corridas,{self.gasolina.value},{self.km.value},{self.ganho.value},{self.data_criacao.value}")
        data = {'data_criacao':str(self.data_criacao.value),'gasolina':float(self.gasolina.value),'ganho':float(self.ganho.value),'km':float(self.km.value)}
        print (data)

        requests.post("http://localhost:8000/controle/api/add",json=data)
    

        
    



        




def main():
    return controlcorridas()

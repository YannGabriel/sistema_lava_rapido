

from datetime import datetime, timedelta 

class Carro:
  def __init__(self, marca, cor, tamanho, placa):
    self.marca = marca
    self.cor = cor
    self.tamanho = tamanho
    self.placa = placa
    self.tamanho_pequeno = 30
    self.tamanho_medio = 40
    self.tamanho_grande = 1
      
  def conversao_horas(self):
    data_hora = datetime.now()
    data_hora_ptbr =  data_hora.strftime("%d/%m/%Y - %H:%M")
    
    if self.tamanho == "P" or self.tamanho == "p":
      horario_saida = data_hora  + timedelta(minutes = self.tamanho_pequeno)
      data_ptbr = horario_saida.strftime("%d/%m/%Y - %H:%M")
      print(f"""
O carro de porte pequeno chegou ás {data_hora_ptbr},
e tem como horário de saída sugerido : {data_ptbr}
            """)
    elif self.tamanho == "M" or self.tamanho == "m":
      horario_saida = data_hora  + timedelta(minutes = self.tamanho_medio)
      data_ptbr = horario_saida.strftime("%d/%m/%Y - %H:%M")
      print(f"""
O carro de porte pequeno chegou ás {data_hora_ptbr},
e tem como horário de saída sugerido : {data_ptbr}
            """)
    elif self.tamanho == "G" or self.tamanho == "g":
      horario_saida = data_hora  + timedelta(hour = self.tamanho_grande)
      data_ptbr = horario_saida.strftime("%d/%m/%Y - %H:%M")
      print(f"""
O carro de porte pequeno chegou ás {data_hora_ptbr},
e tem como horário de saída sugerido : {data_ptbr}
            """)
    else: 
      print("A opção de valor não esta cporreta, tente novamente!")
    

c1 = Carro("chevrolet", "Verde", "m", "ABC-1234" )
c1.conversao_horas()
      
      

      
      

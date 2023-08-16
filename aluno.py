#
#
# autor: Michel
#
# data: 16/08/2023

# classe aluno (filha de pessoa)
from pessoa import Pessoa

class Aluno(Pessoa):
  
  nota1 = None
  nota2 = None
  
  def __init__(self, nome, CPF):
    super().__init__(nome, CPF)
    
  def calMedia(self):
    media = (self.nota1 + self.nota2) / 2
    return media
#
#
# autor: Michel
#
# data: 16/08/2023

# classe pessoa (filha de endereco)
# importar a classe Endereco
from endereco import Endereco

class Pessoa(Endereco):
  
  def __init__(self, nome, CPF):
    self.nome = nome
    self.CPF = CPF
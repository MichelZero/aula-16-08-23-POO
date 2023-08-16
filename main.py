#
#
# autor: Michel
#
# data: 16/08/2023

# teste das classes

# importar as classes (versão 1)
# from endereco import Endereco
# from pessoa import Pessoa

# importar as classes (versão 2)
from pessoa import Pessoa

# criar objetos
p1 = Pessoa("Davi", "12345678901")
# e1 = Endereco("rua das casa", "Cajazeiras")

p1.rua = "rua das casas"
p1.cidade = "Cajazeiras"
# imprimir os dados do cliente
print(f"{p1.nome}, com o CPF {p1.CPF}")
print(f"endereço: {p1.rua}")
print(f"cidade: {p1.cidade}")
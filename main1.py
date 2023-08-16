#
#
# autor: Michel
#
# data: 16/08/2023

# teste das classes

# importar as classes (versão 1)
from endereco import Endereco
from pessoa import Pessoa

# criar objetos
p1 = Pessoa("Davi", "12345678901")
e1 = Endereco("rua das casa", "Cajazeiras")

# imprimir os dados do cliente
print(f"{p1.nome}, com o CPF {p1.CPF}")
print(f"endereço: {e1.rua}")
print(f"cidade: {e1.cidade}")
#
#
# autor: Michel
#
# data: 16/08/2023

# teste das classes

# importar as classes (versão 3)
from aluno import Aluno

# criar objetos
a1 = Aluno("Davi", "12345678901")

a1.nota1 = 8
a1.nota2 = 9
a1.rua = "rua das casas"
a1.cidade = "Cajazeiras"
# imprimir os dados do aluno
print(f"{a1.nome}, com o CPF {a1.CPF}")
print(f"endereço: {a1.rua}")
print(f"cidade: {a1.cidade}")
print(f"média: {a1.calMedia()}")
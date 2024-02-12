from funcion import *

numero = 100

tools = Funcion()

print(tools.verificar_primo(numero))

lista = [1, 50, 2, 50, 3, 50, 2, 2, 10, 50, 50, 50]

print(
    f'El valor más repetido de la lista es {tools.valor_modal(lista)[0]} con {tools.valor_modal(lista)[1]} repeticiones')

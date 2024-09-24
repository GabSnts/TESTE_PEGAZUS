#6-substitua todos os "joao" da lista por "maria"

"""

    A solução foi escolhida por ser simples e utilizar poucas linhas de código.

    O uso do list comprehension é uma forma eficiente de percorrer listas e utilizando o metodo replace, conseguimos alterar somente os valores indicados.

"""

lista = ["joao", "ana", "joana","joao", "ricardo", "joao"]

lista = [item.replace("joao", "maria") for item in lista]

print (lista)
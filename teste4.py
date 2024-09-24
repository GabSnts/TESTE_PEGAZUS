#4-Retire todos os espaços em branco, crie uma nova lista e adicione esses itens nela

"""
    A solução persiste em percorrer todos os valores da lista e utilizar o método strip() para retirar os espaços em branco extras.
""" 

lista1 = []
lista = ["   joao   ","   maria   ","  joana  "]

for item in lista:
    lista1.append(item.strip())


print(lista1)

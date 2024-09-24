#7-criar um loop while em Python que itera sobre os itens de uma lista e imprime os itens enquanto o valor de uma variável é menor ou igual a 5.
# Após imprimir cada item, o valor da variável é incrementado em 1
#explique detalhadamente por que escolheu essa solução e não outra

"""
    A solução foi escolhida por ser simples e de fácil entendimento.

    A solução consiste em setar uma váriavel de indexação e imprimir o valor da lista de acordo com o indice, 
    incrementando a variável de indexação a cada iteração.

"""

lista = ["item1", "item2", "item3", "item4", "item5", "item6", "item7", "item8", "item9", "item10"]
i = 0

while i <= 5:
    print(lista[i])
    i += 1

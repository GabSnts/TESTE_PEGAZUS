#2-Use o JSON abaixo para capturar o preço do produto B
#explique detalhadamente por que escolheu essa solução e não outra

"""
    Utilizando a estrutura de dicionário, percorremos o JSON e acessamos o valor do preço do produto B.

    A solução foi escolhida por ser um JSON simples e direto, sendo assim podemos acessar o valor do preço do produto B diretamente.

    ponto fraco, caso o JSON seja alterada futuramente, será necessário uma revisão do código para garantir o funcionamento
"""

responsejson = {
    "nome": "Loja Exemplo",
    "endereço": {
        "rua": "Rua Exemplo",
        "cidade": "Exemplo City"
    },
    "produtos": [
        {"id": 1, "nome": "Produto A", "preço": 29.99},
        {"id": 2, "nome": "Produto B", "preço": 19.99}
    ]
}

b_price = responsejson["produtos"][1]["preço"]
print(b_price)
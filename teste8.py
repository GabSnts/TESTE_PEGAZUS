#8-usando a biblioteca requests, faça uma requisição http para o endpoint https://jsonplaceholder.typicode.com/todos. 
# cada objeto dentro do json possui a chave "completed". que indica se a task foi completada ou não. 
# Faça uma função que trate a resposta e retorne a quantidade de tasks completadas, e a quantid ade de tasks pendentes
#explique detalhadamente por que escolheu essa solução e não outra


"""
    A solução consiste em criar uma função que realiza a requisição na URL indicada e a transforma em um JSON, 
    definimos as váriaveis de tasks completadas e pendentes e percorremos o JSON incrementando nas váriaveis de acordo com o status da task.
    a função retorna as váriaveis com o total de cada status.

    acessamos a função get_tasks() e imprimimos o resultado.

    A solução foi escolhida por ser prático trabalhar com modelos JSON e ser um código de fácil entendimento.

"""

import requests 

def get_tasks():
    response = requests.get("https://jsonplaceholder.typicode.com/todos")
    tasks = response.json()

    completed_tasks = 0
    pending_tasks = 0

    for task in tasks:
        if task.get("completed"):
            completed_tasks += 1
        else:
            pending_tasks += 1

    return completed_tasks, pending_tasks

completed_tasks, pending_tasks = get_tasks()

print(f'Tasks completadas: {completed_tasks}\nTasks pendentes: {pending_tasks}')

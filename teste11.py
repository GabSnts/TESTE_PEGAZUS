#11-crie uma lista e adicione um item novo a ela utilizando a metodolofia LIFO

import queue

q_lifo = queue.LifoQueue()

q_lifo.put("item1")
q_lifo.put("item2")
q_lifo.put("item3")
q_lifo.put("item4")
q_lifo.put("item5")

print(q_lifo.queue)

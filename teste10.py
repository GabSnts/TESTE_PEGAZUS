#10-crie uma lista e adicione um item novo a ela utilizando a metodologia FIFO

import queue

q_fifo = queue.Queue()

q_fifo.put("item1")
q_fifo.put("item2")
q_fifo.put("item3")
q_fifo.put("item4")
q_fifo.put("item5")

print(q_fifo.queue)

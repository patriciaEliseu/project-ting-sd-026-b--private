class Queue:
    def __init__(self):
        self.queue = list()

    def __len__(self):
        return len(self.queue)

    # add elemento a fila e modificar o seu tamanho
    def enqueue(self, value):
        self.queue.append(value)

    # removerá um elemento que está a mais tempo na fila e
    # modificar o seu tamanho

    def dequeue(self):
        if len(self.queue) == 0:
            raise IndexError("Fila vazia, não é possível remover elementos.")
        return self.queue.pop(0)

    # lança a excecão qdo o indice for invalido
    def search(self, index):
        if index < 0 or index >= len(self.queue):
            raise IndexError("Índice Inválido ou Inexistente")
        return self.queue[index]

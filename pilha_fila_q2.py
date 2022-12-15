class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self,item):
        return self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

soma = 0
count = 0
pilha = Stack()
while True:
    n = int(input())
    if n ==0:
        break
    pilha.push(n)
peso_desejado = int(input())
while True:
    soma +=pilha.peek()
    count+=1
    print(f"Peso retirado: {pilha.peek()}")
    if peso_desejado == pilha.pop():
        break
print(f"Anilhas retiradas: {count}")
print(f"Peso total movimentado: {soma}")





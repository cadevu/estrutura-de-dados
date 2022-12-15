
"""
Questão 2 questionário de pilhas
nota : 4,29/5,000
obs : não fazer gambiarras

"""
def organiza(entrada,qtd):
    final = []
    prioridade = [int(entrada[i]) for i in range(len(entrada)) if i%2 != 0]
    atividade = [entrada[i] for i in range(len(entrada)) if i%2 == 0]
    for i in range(len(prioridade)):
        temp = [prioridade[i],atividade[i]]
        final.append(temp)
    final = sorted(final)

    final = final[qtd:]
    if qtd > 0 :
        for i in final:
            if i[0] == temp:
                final.remove(final[final.index(i)-1])
                final.remove(i)
            temp = i[0]
    return final
entrada = input().split()
qtd = int(input())



prioridades = organiza(entrada,qtd)
print(f"Tamanho da fila: {len(prioridades)}")
for i in prioridades:
    print(f'Atividade: {i[1]}, Prioridade: #{i[0]}')




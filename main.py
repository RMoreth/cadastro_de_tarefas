import os
tarefa = []

while True:
    nova_tarefa = str(input("Adicione uma tarefa:\n"))

    tarefa.append(nova_tarefa)
    r = str(
        input("Adicionar nova tarefa?[s/n]")).strip().lower()[:1]

    os.system('cls')
    if r == "n":
        break
print("Lista de tarefas:")
for t in tarefa:
    print(t)

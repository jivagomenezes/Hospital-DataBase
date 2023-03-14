# Exercicio: Criar um ficheiro de logs.txt
# User          Date
# - - - - - - - - - - -
# REIS, Tiago          2023-01-17_14:59
# REIS, Ana            2023-01-17_15:49

fname = "logs1.txt"
with open(fname, mode="w", encoding="utf-8") as file:
     rows = f"User\t\t\tDate\n{'-' * 20}"
     file.write(rows)

from datetime import datetime

def get_user():
    nome = input("Escreva um nome: ")
    # Os argumentos de split significam : " " = separa nos espaços
    #                                      1 = numero de seprações, nesse caso 2 pq r[0] e r[1]
    r = nome.split(" ", 1)
    user = r[1].upper() + ', ' +r[0]
    return user

# Função que retorna o tempo actual
def get_time():
    # O now apos datetime significa que apanhamos o tempo actual
    # strftime = formato de tempo
    date = datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
    return date

# Declaração e inicialização do registro
registro = ""
# Precisamos repetir essa operação x vezes
for i in range(2):
    # Chamar as duas funções 
    u = get_user()
    d = get_time()
    # print(f"{u} ---> {d}")
    registro = registro + f"{u}\t{d}\n"

# Abrir o ficheiro para escrever as informações do registro nele 
with open("logs2.txt", mode="w", encoding="utf-8") as file:
    file.write(registro)
from asyncio import exceptions
from cgitb import text
import logging

logging.basicConfig(level=logging.INFO, filename="logs_exemplos,log")

users = []

def user_add():
    
    name = input("Digite o nome do usuário: ")
    age = input("Digite a idade do usuário: ")
    
    
    users.append({"name": name, "age": age})
    
        
    logging.INFO("\nUsuário cadastrado com sucesso!")
    
def users_list():
    print("\n")
    for user in users:
        print(f"{name} - {age} anos".format(user["name"], user["age"]))

while True:
    option = int(input("\nDigite a opção desejada:\n 1 - Cadastrar pessoas\n 2 - Listar pessoas\n 3 - Sair\n"))
    
    if option == 1:
        user_add()
    elif option == 2:
        users_list()
    elif option == 3:
        exit()
    else:
        print("Opção inválida!")
import time

print("\n------------ EXEMPLO 1 ------------")
def decorator(funcao):
    def wrapper():
        print("Estou antes da execução da função passada como argumento")
        print("Estou depois da execução da função passada como argumento")
        funcao()
        
    return wrapper

def outra_funcao():
    print("Sou um belo argumento!")
    
funcao_decorada = decorator(outra_funcao) 
funcao_decorada()

print("\n------------ EXEMPLO 2 ------------")

def calcula_tempo(funcao):
    def wrapper():
        tempo_inicio = time.time()
        funcao()
        tempo_final = time.time()
        
        calculo = tempo_final - tempo_inicio
        
        print(f'A função {funcao.__name__}, levou o total de {calculo} para ser executada')
        
    return wrapper

lista = [1, 2, 3, 4, 5, 6]

@calcula_tempo
def run():
    for n in range(lista):
        yield

run()

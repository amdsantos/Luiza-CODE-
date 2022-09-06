class Professor:
    def __init__(self, nome, idade, salario):
        self.nome = nome
        self.idade = idade
        self.salario = salario
        
    def get_dados(self):
        if self.nome == 'João':
            return f'Nome: {self.nome}\nIdade: {self.idade}\nSalário: {self.salario}'
        return f'Nome: {self.nome}\nIdade: {self.idade}\nSalário: Você não pode acessar essa informação'
   
        
    
user1 = Professor('João', 25, 1500).get_dados()
user2 = Professor('Pedro', 25, 1500).get_dados()
print(user1, '\n')
print(user2)
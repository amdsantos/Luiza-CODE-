class Professor:
    def __init__(self, nome, idade, salario):
        self.nome = nome
        self.idade = idade
        self.salario = salario
        
    def get_dados(self):
        if self.nome == 'João':
            return f'Nome: {self.nome}\nIdade: {self.idade}\nSalário: {self.salario}'
        return f'Nome: {self.nome}\nIdade: {self.idade}\nSalário: Você não pode acessar essa informação'
   
        
    
pessoa = Professor('João', 25, 1500).get_dados()

print(pessoa)
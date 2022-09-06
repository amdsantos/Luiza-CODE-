class Pessoa:
    def __init__(self, nome, idade, cpf, fumante):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.fumante = fumante
        
    def get_dados(self):
        if self.fumante == "F":
            return f'{self.nome} tem {self.idade} anos,  portadora do CPF: {self.cpf} - Pessoa fumante'
        else:
            return f'{self.nome} tem {self.idade} anos,  portadora do CPF: {self.cpf} - Não fumante'
       
        
pessoa1 = Pessoa('Amanda Santos Mantovani', '26', '45369602875', 'N').get_dados()
print(pessoa1)
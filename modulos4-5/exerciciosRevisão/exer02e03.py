class Pessoa:
    
    def __init__(self, nome, endereco, telefone):
        self.nome = nome
        self.endereco = endereco
        self.telefone = telefone
        
        

class PessoaFisica(Pessoa):
    def __init__(self, nome, idade, cpf, endereco, telefone, estado_civil):
        super().__init__(nome, endereco, telefone)
        self.idade = idade
        self.cpf = cpf
        self.estado_civil = estado_civil
        
    def get_dados(self):
        return f'Nome: {self.nome}\nidade: {self.idade}\nCPF: {self.cpf}\nEndereço: {self.endereco}\nTelefone: {self.telefone}\nEstado Civil: {self.estado_civil}'
        
        
pessoa = PessoaFisica('Amanda','25', 45369602875, 'Rua João Matiusso', 11934381971, 'Casada').get_dados()



class PessoaJuridica(Pessoa):
    
    def __init__(self, nome, endereco, telefone, cnpj):
        super().__init__(nome, endereco, telefone)
        self.cnpj = cnpj
    
    def get_empresa(self):
        return f'Nome: {self.nome}\nCNPJ: {self.cnpj}\nEndereço: {self.endereco}\nTelefone: {self.telefone}'
    
empresa = PessoaJuridica('Cake Boss', 2635496897485, 'Casa Azul', 11999999999).get_empresa()

print(pessoa, '\n')
print(empresa)
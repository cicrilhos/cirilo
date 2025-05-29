nome = str(input('Digite seu nome: '))

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        print(f'Olá, meu nome é {self.nome} e tenho {self.idade} anos.')

pessoa = Pessoa('João', 25)

descricao = """
RA RA RA RA RA RA RA RA RA RA RA RA RA RA RA RA RA RA RA RA RA RA RA RA RA RA RA RA RA RA RA RA RA RA RA RA RA RA RA RA RA RA RA RA RA RA RA RA RA RA RA RA RA RA RA RA RA RA RA RA RA RA RA RA RA RASPUTIN LOVER OF RUSSIAN QUEEN
"""
print(descricao)

pessoa.apresentar()

nome = 'leandro'
sobrenome: 'lovo'
idade = 20
verdadeiro = True
falso = False
frutas = ['maçã', 'banana', 'laranja', 0]

dicionario = {
    'Aluno 1': 'Davi',
    'Aluno 2': 'Daniel',
    0: "Valor 0",
    'frutas': frutas,
}
print(dicionario['Aluno 1'])
print(dicionario)

array = {
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
}

def funcao_exemplo():
    print('Função exemplo executada')

funcao_exemplo()


for fruta in frutas:
    print('Fruta: ', fruta)

if(verdadeiro):
    print('verdadeiro')
else:
    print('Falso')

# while(idade<30):
#     print('Idade: ', idade)

if not(verdadeiro):
    pass

print('Fim')
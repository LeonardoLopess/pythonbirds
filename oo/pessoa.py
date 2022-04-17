class Pessoa:
    def __init__(self, *filhos, nome=None, idade=36):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'


if __name__ == '__main__':
    renzo = Pessoa(nome='Renzo')
    Leonardo = Pessoa(renzo, nome='Leonardo')
    print(Pessoa.cumprimentar(Leonardo))
    print(id(Leonardo))
    print(Leonardo.cumprimentar())
    print(Leonardo.nome)
    print(Leonardo.idade)
    for filhos in Leonardo.filhos:
        print(filhos.nome)


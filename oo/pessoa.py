class Pessoa:
    olhos = 2

    def __init__(self, *filhos, nome=None, idade=36,):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f' {cls} - olhos {cls.olhos}'


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
    Leonardo.sobrenome = 'Lopes'
    del Leonardo.filhos
    Leonardo.olhos = 1
    del Leonardo.olhos
    print(Leonardo.__dict__)
    print(renzo.__dict__)
    Pessoa.olhos = 3
    print(Pessoa.olhos)
    print(Leonardo.olhos)
    print(renzo.olhos)
    print(id(Pessoa.olhos), id(Leonardo.olhos), id(renzo.olhos))
    print(Pessoa.metodo_estatico(), Leonardo.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classe(), Leonardo.nome_e_atributos_de_classe())


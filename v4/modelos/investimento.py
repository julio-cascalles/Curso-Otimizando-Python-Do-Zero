from modelos.movimento import Movimento


class Investimento(Movimento):
    def valida(self, **args):
        historico = args['historico']
        pessoa = args['pessoa']
        custo = self.quantidade * historico.cotacao
        if custo > pessoa.capital:
            raise ValueError(f'{pessoa.nome} não possui saldo suficiente.')

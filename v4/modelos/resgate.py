from modelos.movimento import Movimento


class Resgate(Movimento):
    def valida(self, **args):
        disponivel = Movimento.total(
            empresa=self.empresa,
            pessoa=self.pessoa,
        )
        if self.quantidade > disponivel:
            raise ValueError('Não há saldo disponível para este resgate.')
        self.quantidade *= -1

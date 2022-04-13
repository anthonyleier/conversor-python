from classes.pagamento import Pagamento


class Empresa():
    def __init__(self, dadosArquivo):
        self.nome = dadosArquivo[72:102]
        self.cnpj = dadosArquivo[18:32]
        self.banco = dadosArquivo[102:132]
        self.listaPagamentos = []

    def inserirEndereco(self, dadosArquivo):
        self.rua = dadosArquivo[142:172]
        self.numero = dadosArquivo[172:177]
        self.cidade = dadosArquivo[192:212]
        self.cepBase = dadosArquivo[212:217]
        self.cepComplemento = dadosArquivo[217:220]
        self.estado = dadosArquivo[220:222]
        self.formaPagamento = dadosArquivo[11:13]
        self.cep = self.cepBase + self.cepComplemento

    def adicionarPagamento(self, dadosArquivo):
        pagamento = Pagamento()
        pagamento.nomeFavorecido = dadosArquivo[43:73]
        pagamento.data = dadosArquivo[93:101]
        pagamento.valor = dadosArquivo[119:134]
        pagamento.numero = dadosArquivo[73:93]
        pagamento.forma = self.formaPagamento
        self.listaPagamentos.append(pagamento)

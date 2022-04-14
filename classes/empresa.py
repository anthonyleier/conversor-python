from classes.pagamento import Pagamento
from formatar import formatarTexto, formatarCNPJ, formatarFormaPagamento, formatarData, formatarMoeda


class Empresa():
    def __init__(self, dadosArquivo):
        self.nome = formatarTexto(dadosArquivo[72:102])
        self.cnpj = formatarCNPJ(dadosArquivo[18:32])
        self.banco = formatarTexto(dadosArquivo[102:132])
        self.listaPagamentos = []

    def inserirEndereco(self, dadosArquivo):
        self.rua = formatarTexto(dadosArquivo[142:172])
        self.numero = formatarTexto(dadosArquivo[172:177])
        self.cidade = formatarTexto(dadosArquivo[192:212])
        self.cepBase = formatarTexto(dadosArquivo[212:217])
        self.cepComplemento = formatarTexto(dadosArquivo[217:220])
        self.estado = formatarTexto(dadosArquivo[220:222])
        self.formaPagamento = formatarFormaPagamento(dadosArquivo[11:13])
        self.cep = f"{self.cepBase}-{self.cepComplemento}"

    def adicionarPagamento(self, dadosArquivo):
        pagamento = Pagamento()
        pagamento.nomeFavorecido = formatarTexto(dadosArquivo[43:73])
        pagamento.data = formatarData(dadosArquivo[93:101])
        pagamento.valor = formatarMoeda(dadosArquivo[119:134])
        pagamento.numero = dadosArquivo[73:93]
        pagamento.forma = self.formaPagamento
        self.listaPagamentos.append(pagamento)

    def __str__(self):
        string = f"{self.nome} | {self.cnpj} | {self.banco} | {self.listaPagamentos}"
        return string

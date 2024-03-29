from classes.pagamento import Pagamento
from formatar import formatarTexto, formatarCNPJ, formatarFormaPagamento


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
        self.estado = formatarTexto(dadosArquivo[220:222])
        self.formaPagamento = formatarFormaPagamento(dadosArquivo[11:13])
        cepBase = formatarTexto(dadosArquivo[212:217])
        cepComplemento = formatarTexto(dadosArquivo[217:220])
        self.cep = f"{cepBase}-{cepComplemento}"

    def adicionarPagamento(self, dadosArquivo):
        pagamento = Pagamento(dadosArquivo)
        pagamento.forma = self.formaPagamento
        self.listaPagamentos.append(pagamento)

    def __str__(self):
        string = f"{self.nome} | {self.cnpj}"
        return string

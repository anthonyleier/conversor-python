from formatar import formatarTexto, formatarData, formatarMoeda


class Pagamento():
    def __init__(self, dadosArquivo):
        self.nomeFavorecido = formatarTexto(dadosArquivo[43:73])
        self.data = formatarData(dadosArquivo[93:101])
        self.valor = formatarMoeda(dadosArquivo[119:134])
        self.numero = formatarTexto(dadosArquivo[73:93])
        self.forma = "Desconhecido"

    def __str__(self):
        string = f"{self.nomeFavorecido} | {self.data} | {self.valor}"
        return string

class GeradorRelatorio():
    def __init__(self):
        self.html = "<html><body>"
        self.css = "<style> table, th, td { border: 1px solid black; } </style>"

    def montarTabelaEmpresa(self, empresa):
        cabecalho = ""
        cabecalho += "<tr>"
        cabecalho += "<th>Nome da Empresa</th>"
        cabecalho += "<th>Numero de Inscricao da Empresa</th>"
        cabecalho += "<th>Nome do Banco</th>"
        cabecalho += "<th>Nome da Rua</th>"
        cabecalho += "<th>Numero do Local</th>"
        cabecalho += "<th>Nome da Cidade</th>"
        cabecalho += "<th>CEP</th>"
        cabecalho += "<th>Sigla do Estado</th>"
        cabecalho += "</tr>"

        conteudo = ""
        conteudo += "<tr>"
        conteudo += f"<td>{empresa.nome}</td>"
        conteudo += f"<td>{empresa.cnpj}</td>"
        conteudo += f"<td>{empresa.banco}</td>"
        conteudo += f"<td>{empresa.rua}</td>"
        conteudo += f"<td>{empresa.numero}</td>"
        conteudo += f"<td>{empresa.cidade}</td>"
        conteudo += f"<td>{empresa.cep}</td>"
        conteudo += f"<td>{empresa.estado}</td>"
        conteudo += "</tr>"

        self.html += "<br><table>" + cabecalho + conteudo + "</table><br>"

    def montarTabelaPagamentos(self, listaPagamentos):
        cabecalho = ""
        cabecalho += "<tr>"
        cabecalho += "<th>Nome do Favorecido</th>"
        cabecalho += "<th>Data de Pagamento</th>"
        cabecalho += "<th>Valor do Pagamento</th>"
        cabecalho += "<th>Numero do Documento Atribuido pela Empresa</th>"
        cabecalho += "<th>Forma de Lancamento</th>"
        cabecalho += "</tr>"

        conteudo = ""
        for pagamento in listaPagamentos:
            conteudo += "<tr>"
            conteudo += f"<td>{pagamento.nomeFavorecido}</td>"
            conteudo += f"<td>{pagamento.data}</td>"
            conteudo += f"<td>{pagamento.valor}</td>"
            conteudo += f"<td>{pagamento.numero}</td>"
            conteudo += f"<td>{pagamento.forma}</td>"
            conteudo += "</tr>"

        self.html += "<br><table>" + cabecalho + conteudo + "</table><br>"

    def montarHTML(self, caminho):
        self.html += self.css + "</body></html>"
        with open(caminho, 'w', encoding='utf-8') as arquivo:
            arquivo.write(self.html)

    def __str__(self):
        string = self.html
        return string

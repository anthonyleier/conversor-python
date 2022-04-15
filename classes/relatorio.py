class Relatorio():
    def __init__(self):
        self.html = """
        <style> table, th, td
        { border: 1px solid black; }
        </style>
        """

    def montarTabelaEmpresa(self, empresa):
        cabecalho = f"""
        <tr>
            <th>Nome da Empresa</th>
            <th>Numero de Inscricao da Empresa</th>
            <th>Nome do Banco</th>
            <th>Nome da Rua</th>
            <th>Numero do Local</th>
            <th>Nome da Cidade</th>
            <th>CEP</th>
            <th>Sigla do Estado</th>
        </tr>
        """

        conteudo = f"""
        <tr>
            <td>{empresa.nome}</td>
            <td>{empresa.cnpj}</td>
            <td>{empresa.banco}</td>
            <td>{empresa.rua}</td>
            <td>{empresa.numero}</td>
            <td>{empresa.cidade}</td>
            <td>{empresa.cep}</td>
            <td>{empresa.estado}</td>
        </tr>
        """

        tabela = "<br><table>" + cabecalho + conteudo + "</table><br>"
        self.html += tabela
        return tabela

    def montarTabelaPagamentos(self, listaPagamentos):
        cabecalho = f"""
        <tr>
            <th>Nome do Favorecido</th>
            <th>Data de Pagamento</th>
            <th>Valor do Pagamento</th>
            <th>Numero do Documento Atribuido pela Empresa</th>
            <th>Forma de Lancamento</th>
        </tr>
        """
        conteudo = ""
        for pagamento in listaPagamentos:
            conteudo += f"""
            <tr>
                <td>{pagamento.nomeFavorecido}</td>
                <td>{pagamento.data}</td>
                <td>{pagamento.valor}</td>
                <td>{pagamento.numero}</td>
                <td>{pagamento.forma}</td>
            </tr>
            """

        tabela = "<br><table>" + cabecalho + conteudo + "</table><br>"
        self.html += tabela
        return tabela

    def criarHTML(self, caminho):
        try:
            with open(caminho, 'w', encoding='utf-8') as arquivo:
                arquivo.write(self.html)

        except Exception as erro:
            mensagem = f"Erro ao gravar o arquivo {caminho}: {erro}"
            print(mensagem)

        return self.html

    def __str__(self):
        return self.html

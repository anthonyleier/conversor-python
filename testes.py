import unittest
from main import tratamentoArquivos
from classes.empresa import Empresa
from classes.relatorio import Relatorio
from classes.pagamento import Pagamento


arquivoTeste = 'entrada.txt'


def lerLinha(index):
    index -= 1
    with open(arquivoTeste, 'r', encoding='utf-8') as arquivo:
        linhas = arquivo.readlines()
    return linhas[index]


def lerResposta():
    with open('resposta.html', 'r', encoding='utf-8') as arquivo:
        dados = arquivo.read()
    return dados


def removeTags(stringHTML):
    stringHTML = stringHTML.replace("<html>", "")
    stringHTML = stringHTML.replace("<body>", "")
    stringHTML = stringHTML.replace("<br>", "")
    stringHTML = stringHTML.replace("</table>", "")
    return stringHTML


class PagamentoTestes(unittest.TestCase):
    def test_init(self):
        linha = lerLinha(3)
        pagamento = Pagamento(linha)
        self.assertEqual(pagamento.nomeFavorecido, 'EMPRESA FORNECEDOR 1')
        self.assertEqual(pagamento.data, '07/06/2017')
        self.assertEqual(pagamento.valor, 'R$ 0,10')
        self.assertEqual(pagamento.numero, '0000000001')
        self.assertEqual(pagamento.forma, 'Desconhecido')


class EmpresaTestes(unittest.TestCase):
    def test_init(self):
        linha = lerLinha(1)
        empresa = Empresa(linha)
        self.assertEqual(empresa.nome, 'GRUPO NEXXERA')
        self.assertEqual(empresa.cnpj, '95.774.212/0001-32')
        self.assertEqual(empresa.banco, 'HSBC')

    def test_inserirEndereco(self):
        linha = lerLinha(1)
        empresa = Empresa(linha)
        linha = lerLinha(2)
        empresa.inserirEndereco(linha)
        self.assertEqual(empresa.nome, 'GRUPO NEXXERA')
        self.assertEqual(empresa.cnpj, '95.774.212/0001-32')
        self.assertEqual(empresa.banco, 'HSBC')

    def test_adicionarPagamento(self):
        linha = lerLinha(1)
        empresa = Empresa(linha)
        linha = lerLinha(2)
        empresa.inserirEndereco(linha)
        linha = lerLinha(3)
        empresa.adicionarPagamento(linha)
        self.assertIn('EMPRESA FORNECEDOR 1',
                      empresa.listaPagamentos[0].nomeFavorecido)


class RelatorioTestes(unittest.TestCase):
    def test_init(self):
        relatorio = Relatorio()
        self.assertEqual(relatorio.html, '<html><body>')
        self.assertEqual(
            relatorio.css, '<style> table, th, td { border: 1px solid black; } </style>')

    def test_montarTabelaEmpresa(self):
        linha = lerLinha(1)
        empresa = Empresa(linha)
        linha = lerLinha(2)
        empresa.inserirEndereco(linha)
        relatorio = Relatorio()
        relatorio.montarTabelaEmpresa(empresa)
        resposta = lerResposta()
        self.assertIn(relatorio.html, resposta)

    def test_montarTabelaPagamentos(self):
        linha = lerLinha(1)
        empresa = Empresa(linha)
        linha = lerLinha(2)
        empresa.inserirEndereco(linha)
        linha = lerLinha(3)
        empresa.adicionarPagamento(linha)
        relatorio = Relatorio()
        relatorio.montarTabelaPagamentos(empresa.listaPagamentos)
        resposta = lerResposta()
        self.assertIn(removeTags(relatorio.html), resposta)

    def test_montarHTML(self):
        linha = lerLinha(1)
        empresa = Empresa(linha)
        linha = lerLinha(2)
        empresa.inserirEndereco(linha)
        linha = lerLinha(3)
        empresa.adicionarPagamento(linha)
        relatorio = Relatorio()
        relatorio.montarTabelaEmpresa(empresa)
        relatorio.montarTabelaPagamentos(empresa.listaPagamentos)
        relatorio.montarHTML('saida.html')
        resposta = lerResposta()
        self.assertIn(relatorio.html, resposta)


class MainTestes(unittest.TestCase):
    def test_tratamentoArquivos(self):
        arquivoEntrada = 'entrada.txt'
        arquivoSaida = 'saida.html'
        html = tratamentoArquivos(arquivoEntrada, arquivoSaida)
        resposta = lerResposta()
        self.assertEqual(html, resposta)


class FormatarTestes(unittest.TestCase):
    pass


if __name__ == '__main__':
    unittest.main()

import unittest
from main import tratamentoArquivos
from classes.empresa import Empresa
from classes.relatorio import Relatorio
from classes.pagamento import Pagamento


arquivoTeste = 'entrada.txt'

tabelaEmpresa = "<table><tr><th>Nome da Empresa</th><th>Numero de Inscricao da Empresa</th><th>Nome do Banco</th><th>Nome da Rua</th><th>Numero do Local</th><th>Nome da Cidade</th><th>CEP</th><th>Sigla do Estado</th></tr><tr><td>GRUPO NEXXERA</td><td>95.774.212/0001-32</td><td>HSBC</td><td>Rua Madalena Barbi</td><td>181</td><td>Centro-Florianopolis</td><td>88015-190</td><td>SC</td></tr></table>"
tabelaPagamentos = "<table><tr><th>Nome do Favorecido</th><th>Data de Pagamento</th><th>Valor do Pagamento</th><th>Numero do Documento Atribuido pela Empresa</th><th>Forma de Lancamento</th></tr><tr><td>EMPRESA FORNECEDOR 1</td><td>07/06/2017</td><td>R$ 0,10</td><td>0000000001</td><td>Crédito em Conta Corrente</td></tr><tr><td>EMPRESA FORNECEDOR 2</td><td>07/06/2017</td><td>R$ 200,20</td><td>0000000002</td><td>Crédito em Conta Corrente</td></tr><tr><td>EMPRESA FORNECEDOR 3</td><td>07/06/2017</td><td>R$ 30.300,30</td><td>0000000003</td><td>Crédito em Conta Corrente</td></tr></table>"
htmlFinal = "<html><body><br><table><tr><th>Nome da Empresa</th><th>Numero de Inscricao da Empresa</th><th>Nome do Banco</th><th>Nome da Rua</th><th>Numero do Local</th><th>Nome da Cidade</th><th>CEP</th><th>Sigla do Estado</th></tr><tr><td>GRUPO NEXXERA</td><td>95.774.212/0001-32</td><td>HSBC</td><td>Rua Madalena Barbi</td><td>181</td><td>Centro-Florianopolis</td><td>88015-190</td><td>SC</td></tr></table><br><br><table><tr><th>Nome do Favorecido</th><th>Data de Pagamento</th><th>Valor do Pagamento</th><th>Numero do Documento Atribuido pela Empresa</th><th>Forma de Lancamento</th></tr><tr><td>EMPRESA FORNECEDOR 1</td><td>07/06/2017</td><td>R$ 0,10</td><td>0000000001          </td><td>Crédito em Conta Corrente</td></tr><tr><td>EMPRESA FORNECEDOR 2</td><td>07/06/2017</td><td>R$ 200,20</td><td>0000000002          </td><td>Crédito em Conta Corrente</td></tr><tr><td>EMPRESA FORNECEDOR 3</td><td>07/06/2017</td><td>R$ 30.300,30</td><td>0000000003          </td><td>Crédito em Conta Corrente</td></tr></table><br><style> table, th, td { border: 1px solid black; } </style></body></html>"


def lerLinha(index):
    index -= 1
    with open(arquivoTeste, 'r', encoding='utf-8') as arquivo:
        linhas = arquivo.readlines()
    return linhas[index]


class PagamentoTestes(unittest.TestCase):
    def test_init(self):
        linha = lerLinha(3)
        pagamento = Pagamento(linha)
        self.assertEqual(pagamento.nomeFavorecido, 'EMPRESA FORNECEDOR 1')
        self.assertEqual(pagamento.data, '07/06/2017')
        self.assertEqual(pagamento.valor, 'R$ 0,10')
        self.assertEqual(pagamento.numero, '0000000001')
        self.assertEqual(pagamento.forma, 'Desconhecido')


# class EmpresaTestes(unittest.TestCase):
#     def test_init(self):
#         linha = lerLinha(1)
#         empresa = Empresa(linha)
#         self.assertEqual(empresa.nome, 'GRUPO NEXXERA')
#         self.assertEqual(empresa.cnpj, '95.774.212/0001-32')
#         self.assertEqual(empresa.banco, 'HSBC')

#     def test_inserirEndereco(self):
#         linha = lerLinha(1)
#         empresa = Empresa(linha)
#         linha = lerLinha(2)
#         empresa.inserirEndereco(linha)
#         self.assertEqual(empresa.nome, 'GRUPO NEXXERA')
#         self.assertEqual(empresa.cnpj, '95.774.212/0001-32')
#         self.assertEqual(empresa.banco, 'HSBC')

#     def test_adicionarPagamento(self):
#         linha = lerLinha(1)
#         empresa = Empresa(linha)
#         linha = lerLinha(2)
#         empresa.inserirEndereco(linha)
#         linha = lerLinha(3)
#         empresa.adicionarPagamento(linha)
#         self.assertIn('EMPRESA FORNECEDOR 3',
#                       empresa.listaPagamentos[0].nomeFavorecido)


# class RelatorioTestes(unittest.TestCase):
#     def test_init(self):
#         relatorio = Relatorio()
#         self.assertEqual(relatorio.html, '<html><body>')
#         self.assertEqual(
#             relatorio.css, '<style> table, th, td { border: 1px solid black; } </style>')

#     def test_montarTabelaEmpresa(self):
#         linha = lerLinha(1)
#         empresa = Empresa(linha)
#         linha = lerLinha(2)
#         empresa.inserirEndereco(linha)
#         relatorio = Relatorio()
#         relatorio.montarTabelaEmpresa(empresa)
#         self.assertIn(tabelaEmpresa, relatorio.html)

#     def test_montarTabelaPagamentos(self):
#         linha = lerLinha(1)
#         empresa = Empresa(linha)
#         linha = lerLinha(2)
#         empresa.inserirEndereco(linha)
#         linha = lerLinha(3)
#         empresa.adicionarPagamento(linha)
#         relatorio = Relatorio()
#         relatorio.montarTabelaPagamentos(empresa.listaPagamentos)
#         self.assertIn(tabelaPagamentos, relatorio.html)

#     def test_montarHTML(self):
#         linha = lerLinha(1)
#         empresa = Empresa(linha)
#         linha = lerLinha(2)
#         empresa.inserirEndereco(linha)
#         linha = lerLinha(3)
#         empresa.adicionarPagamento(linha)
#         relatorio = Relatorio()
#         relatorio.montarTabelaEmpresa(empresa)
#         relatorio.montarTabelaPagamentos(empresa.listaPagamentos)
#         relatorio.montarHTML('saida.html')
#         self.assertIn(relatorio.html, htmlFinal)


# class MainTestes(unittest.TestCase):
#     def test_tratamentoArquivos(self):
#         arquivoEntrada = 'entrada.txt'
#         arquivoSaida = 'saida.html'
#         html = tratamentoArquivos(arquivoEntrada, arquivoSaida)
#         self.assertEqual(html, htmlFinal)


if __name__ == '__main__':
    unittest.main()

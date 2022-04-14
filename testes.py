import unittest
from main import tratamentoArquivos
from classes.empresa import Empresa
from classes.relatorio import Relatorio
from classes.pagamento import Pagamento
from formatar import formatarTexto, formatarCNPJ
from formatar import formatarFormaPagamento, formatarData, formatarMoeda

arquivoEntradaTeste = 'files/entrada.txt'
arquivoSaidaTeste = 'files/saida_teste.html'

arquivoSaidaCorreto = 'files/resposta.html'


def lerLinha(index):
    index -= 1
    with open(arquivoEntradaTeste, 'r', encoding='utf-8') as arquivo:
        linhas = arquivo.readlines()
    return linhas[index]


def lerResposta():
    with open(arquivoSaidaCorreto, 'r', encoding='utf-8') as arquivo:
        dados = arquivo.read()
    return dados


def removerIdentacao(texto):
    texto = texto.replace("\n", "")
    texto = texto.replace(" ", "")
    return texto


class PagamentoTestes(unittest.TestCase):
    def setUp(self):
        linha = lerLinha(3)
        self.pagamento1 = Pagamento(linha)

        linha = lerLinha(4)
        self.pagamento2 = Pagamento(linha)

        linha = lerLinha(5)
        self.pagamento3 = Pagamento(linha)

    def teste_criacao(self):
        self.assertEqual(self.pagamento1.nomeFavorecido,
                         'EMPRESA FORNECEDOR 1')
        self.assertEqual(self.pagamento1.data, '07/06/2017')
        self.assertEqual(self.pagamento1.valor, 'R$ 0,10')
        self.assertEqual(self.pagamento1.numero, '0000000001')
        self.assertEqual(self.pagamento1.forma, 'Desconhecido')

        self.assertEqual(self.pagamento2.nomeFavorecido,
                         'EMPRESA FORNECEDOR 2')
        self.assertEqual(self.pagamento2.data, '07/06/2017')
        self.assertEqual(self.pagamento2.valor, 'R$ 200,20')
        self.assertEqual(self.pagamento2.numero, '0000000002')
        self.assertEqual(self.pagamento2.forma, 'Desconhecido')

        self.assertEqual(self.pagamento3.nomeFavorecido,
                         'EMPRESA FORNECEDOR 3')
        self.assertEqual(self.pagamento3.data, '07/06/2017')
        self.assertEqual(self.pagamento3.valor, 'R$ 30.300,30')
        self.assertEqual(self.pagamento3.numero, '0000000003')
        self.assertEqual(self.pagamento3.forma, 'Desconhecido')


class EmpresaTestes(unittest.TestCase):
    def setUp(self):
        linha = lerLinha(1)
        self.empresa = Empresa(linha)

        linha = lerLinha(2)
        self.empresa.inserirEndereco(linha)

    def teste_criacao(self):
        self.assertEqual(self.empresa.nome, 'GRUPO NEXXERA')
        self.assertEqual(self.empresa.cnpj, '95.774.212/0001-32')
        self.assertEqual(self.empresa.banco, 'HSBC')

    def teste_endereco(self):
        self.assertEqual(self.empresa.rua, 'Rua Madalena Barbi')
        self.assertEqual(self.empresa.numero, '181')
        self.assertEqual(self.empresa.cidade, 'Centro-Florianopolis')
        self.assertEqual(self.empresa.estado, 'SC')
        self.assertEqual(self.empresa.formaPagamento,
                         'Crédito em Conta Corrente')
        self.assertEqual(self.empresa.cep, '88015-190')

    def teste_adicionarPagamento(self):
        linha = lerLinha(3)
        self.empresa.adicionarPagamento(linha)
        self.assertEqual('EMPRESA FORNECEDOR 1',
                         self.empresa.listaPagamentos[0].nomeFavorecido)


class RelatorioTestes(unittest.TestCase):
    def setUp(self):
        self.relatorio = Relatorio()
        linha = lerLinha(1)
        self.empresa = Empresa(linha)
        linha = lerLinha(2)
        self.empresa.inserirEndereco(linha)
        linha = lerLinha(3)
        self.empresa.adicionarPagamento(linha)
        linha = lerLinha(4)
        self.empresa.adicionarPagamento(linha)
        linha = lerLinha(5)
        self.empresa.adicionarPagamento(linha)

    def teste_montarTabelaEmpresa(self):
        tabela = self.relatorio.montarTabelaEmpresa(self.empresa)
        resposta = lerResposta()
        self.assertIn(removerIdentacao(tabela), removerIdentacao(resposta))

    def teste_montarTabelaPagamentos(self):
        tabela = self.relatorio.montarTabelaPagamentos(
            self.empresa.listaPagamentos)
        resposta = lerResposta()
        self.assertIn(removerIdentacao(tabela), removerIdentacao(resposta))

    def teste_montarHTML(self):
        self.relatorio.montarTabelaEmpresa(self.empresa)
        self.relatorio.montarTabelaPagamentos(self.empresa.listaPagamentos)
        self.relatorio.montarHTML(arquivoSaidaTeste)
        resposta = lerResposta()
        self.assertIn(removerIdentacao(self.relatorio.html),
                      removerIdentacao(resposta))


class FormatarTestes(unittest.TestCase):
    def teste_formatarTexto(self):
        textoTeste = "  TESTE DE TEXTO  "
        textoCorreto = "TESTE DE TEXTO"
        self.assertEqual(textoCorreto, formatarTexto(textoTeste))

    def teste_formatarCNPJ(self):
        textoTeste = "24854745000186"
        textoCorreto = "24.854.745/0001-86"
        self.assertEqual(textoCorreto, formatarCNPJ(textoTeste))

    def teste_formatarFormaPagamento(self):
        textoTeste = "21"
        textoCorreto = "Tributo - DARJ"
        self.assertEqual(textoCorreto, formatarFormaPagamento(textoTeste))

    def teste_formatarData(self):
        textoTeste = "14042022"
        textoCorreto = "14/04/2022"
        self.assertEqual(textoCorreto, formatarData(textoTeste))

    def teste_formatarMoeda(self):
        textoTeste = "0000000003030030"
        textoCorreto = "R$ 30.300,30"
        self.assertEqual(textoCorreto, formatarMoeda(textoTeste))


class MainTestes(unittest.TestCase):
    def test_tratamentoArquivos(self):
        html = tratamentoArquivos(arquivoEntradaTeste, arquivoSaidaTeste)
        resposta = lerResposta()
        self.assertEqual(removerIdentacao(html), removerIdentacao(resposta))


if __name__ == '__main__':
    unittest.main()

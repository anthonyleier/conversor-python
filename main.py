import os
import sys
from classes.empresa import Empresa
from classes.relatorio import Relatorio


def coletarLinhasArquivo(caminho):
    try:
        with open(caminho, 'r', encoding='utf-8') as arquivo:
            linhas = arquivo.readlines()
            return linhas

    except Exception as erro:
        mensagem = f"Erro ao ler o arquivo {caminho}: {erro}"
        print(mensagem)


def tratamentoArquivos(arquivoEntrada, arquivoSaida):
    linhasArquivo = coletarLinhasArquivo(arquivoEntrada)

    for index, linha in enumerate(linhasArquivo):
        try:
            tipoRegistro = linha[7:8]

            # Header de Arquivo
            if tipoRegistro == "0":
                print("Criando a estrutura da empresa...")
                empresa = Empresa(linha)

            # Header de Lote
            if tipoRegistro == "1":
                print("Preenchendo os dados de endereço...")
                empresa.inserirEndereco(linha)

            # Registro de Detalhe
            if tipoRegistro == "3":
                print("Adicionando registro de pagamento...")
                empresa.adicionarPagamento(linha)

        except Exception as erro:
            linhaAtual = index + 1
            mensagem = f"Erro na leitura da linha {linhaAtual}: {erro}"
            print(mensagem)

    relatorio = Relatorio()
    print("Criando tabela de empresa...")
    relatorio.montarTabelaEmpresa(empresa)

    print("Criando tabela de pagamentos...")
    relatorio.montarTabelaPagamentos(empresa.listaPagamentos)

    print("Finalizando relatório em HTML...")
    return relatorio.criarHTML(arquivoSaida)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit("Exemplo de uso: python main.py entrada.txt saida.html")

    arquivoEntrada = sys.argv[1]
    arquivoSaida = sys.argv[2]

    if not os.path.exists(arquivoEntrada):
        sys.exit(f"Arquivo de entrada não encontrado ({arquivoEntrada})")

    tratamentoArquivos(arquivoEntrada, arquivoSaida)

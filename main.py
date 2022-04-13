import sys
from classes.empresa import Empresa
from classes.geradorRelatorio import GeradorRelatorio

if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit("Exemplo de uso: python main.py entrada.txt saida.html")

    arquivoEntrada = sys.argv[1]
    arquivoSaida = sys.argv[2]

    with open(arquivoEntrada, 'r', encoding='utf-8') as arquivo:
        linhasArquivo = arquivo.readlines()

    for linha in linhasArquivo:
        tipoRegistro = linha[7:8]

        # Header de Arquivo
        if tipoRegistro == "0":
            empresa = Empresa(linha)

        # Header de Lote
        if tipoRegistro == "1":
            empresa.inserirEndereco(linha)

        # Registro de Detalhe
        if tipoRegistro == "3":
            empresa.adicionarPagamento(linha)

    geradorRelatorio = GeradorRelatorio()
    geradorRelatorio.montarTabelaEmpresa(empresa)
    geradorRelatorio.montarTabelaPagamentos(empresa.listaPagamentos)
    geradorRelatorio.montarHTML(arquivoSaida)

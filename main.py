import sys
from classes.empresa import Empresa
from classes.geradorRelatorio import GeradorRelatorio

if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit("Exemplo de uso: python main.py entrada.txt saida.html")

    arquivoEntrada = sys.argv[1]
    arquivoSaida = sys.argv[2]

    with open(arquivoEntrada, 'r') as arquivo:
        linhasArquivo = arquivo.readlines()

    for linha in linhasArquivo:
        if linha[7:8] == "0":
            empresa = Empresa(linha)

        if linha[7:8] == "1":
            empresa.inserirEndereco(linha)

        if linha[7:8] == "3":
            empresa.adicionarPagamento(linha)

    geradorRelatorio = GeradorRelatorio()
    geradorRelatorio.montarTabelaEmpresa(empresa)
    geradorRelatorio.montarTabelaPagamentos(empresa.listaPagamentos)
    geradorRelatorio.montarHTML(arquivoSaida)

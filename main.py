import sys
from classes.empresa import Empresa
from funcoes import leituraArquivo, gerarRelatorio
from layout import montarTabela1

if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit("Exemplo de uso: python main.py entrada.txt saida.html")

    arquivoEntrada = sys.argv[1]
    arquivoSaida = sys.argv[2]

    infos = leituraArquivo(arquivoEntrada)
    html = montarTabela1(infos)

    with open(arquivoSaida, 'w') as arquivo:
        arquivo.write(html)

    # empresa = Empresa(cabecalho)
    # empresa.adicionarDetalhes(detalhes)
    # empresa.gerarRelatorio(arquivoSaida)

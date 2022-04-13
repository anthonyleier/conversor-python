def leituraArquivo(caminho):
    with open(caminho, 'r') as arquivo:
        linhas = arquivo.readlines()
        headerArquivo = linhas[0]
        headerLote = linhas[1]
        conteudoLote = linhas[2]

    nomeEmpresa = headerArquivo[72:102]  # GRUPO NEXXERA
    cnpjEmpresa = headerArquivo[18:32]  # 95774212000132
    nomeBanco = headerArquivo[102:132]  # HSBC

    rua = headerLote[142:172]  # Rua Madalena Barbi
    local = headerLote[172:177]  # 181
    cidade = headerLote[192:212]  # Centro-Florianopolis
    cepBase = headerLote[212:217]  # 88015
    cepComplemento = headerLote[217:220]  # 190
    cep = cepBase + cepComplemento
    estado = headerLote[220:222]  # SC

    formaPagamento = headerLote[11:13]  # Credito em Conta Corrente

    nomeFavorecido = conteudoLote[43:73]  # EMPRESA FORNECEDOR 1
    dataPagamento = conteudoLote[93:101]  # 07/06/2017
    valorPagamento = conteudoLote[119:134]  # 0,10
    numeroDocumento = conteudoLote[73:93]  # 0000000001

    infos = []
    infos.append(nomeEmpresa)
    infos.append(cnpjEmpresa)
    infos.append(nomeBanco)
    infos.append(rua)
    infos.append(local)
    infos.append(cidade)
    infos.append(cep)
    infos.append(estado)

    return infos


def gerarRelatorio():
    pass

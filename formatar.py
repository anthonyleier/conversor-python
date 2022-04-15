import locale
from datetime import datetime


formasPagamento = {
    '01': 'Credito em Conta Corrente',
    '02': 'Cheque Pagamento / Administrativo',
    '03': 'DOC/TED',
    '04': 'Cartão Salário',
    '05': 'Crédito em Conta Poupança',
    '06': 'Liberação de Títulos HSBC',
    '07': 'Emissão de Cheque Salário',
    '08': 'Liquidação de Parcelas de Cobrança Não Registrada',
    '09': 'Arrecadação de Tributos Federais',
    '10': 'OP à Disposição',
    '11': 'Pagamento de Contas e Tributos com Código de Barras',
    '12': 'DOC Mesma Titularidade',
    '13': 'Pagamentos de Guias',
    '14': 'Crédito em Conta Corrente Mesma Titularidade',
    '16': 'Tributo - DARF Normal',
    '17': 'Tributo - GPS (Guia da Previdencia Social)',
    '18': 'Tributo - DARF Simples',
    '19': 'Tributo - IPTU - Prefeituras',
    '20': 'Pagamento com Autenticação',
    '21': 'Tributo - DARJ',
}


def formatarTexto(texto):
    return texto.strip()


def formatarCNPJ(cnpj):
    cnpj = cnpj.strip()
    cnpj = f"{cnpj[:2]}.{cnpj[2:5]}.{cnpj[5:8]}/{cnpj[8:12]}-{cnpj[12:]}"
    return cnpj


def formatarFormaPagamento(codigo):
    codigo = codigo.strip()
    return formasPagamento[codigo]


def formatarData(data):
    data = data.strip()
    data = datetime.strptime(data, '%d%m%Y')
    data = data.strftime("%d/%m/%Y")
    return data


def formatarMoeda(valor):
    valor = valor.strip()
    valor = float(valor) * 0.01
    locale.setlocale(locale.LC_ALL, 'pt_BR')
    valor = locale.currency(valor, grouping=True)
    return valor

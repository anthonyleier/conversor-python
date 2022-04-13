def montarTabela1(infos):
    html = "<html>"
    html += "<table>"

    html += """
    <style>
table, th, td {
  border:1px solid black;
}
table {
    width:100%;
}
</style>
"""

    html += "<tr>"
    html += "<th>Nome da Empresa</th>"
    html += "<th>Numero de Inscricao da Empresa</th>"
    html += "<th>Nome do Banco</th>"
    html += "<th>Nome da Rua</th>"
    html += "<th>Numero do Local</th>"
    html += "<th>Nome da Cidade</th>"
    html += "<th>CEP</th>"
    html += "<th>Sigla do Estado</th>"
    html += "</tr>"

    html += "<tr>"
    for info in infos:
        html += f"<td>{info}</td>"
    html += "</tr>"

    html += "<html>"

    return html

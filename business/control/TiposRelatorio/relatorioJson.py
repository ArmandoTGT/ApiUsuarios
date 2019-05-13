import json
from business.TiposRelatorio.templateRelatorio import templateRelatorio

class relatorio_json(templateRelatorio):

    def geraRelatorio(self, dados):
        #print('Dados:', dados)
        relatorio = {}
        relatorio['QuantidadeAcessos'] = dados[0]
        relatorio['MinutosPassados'] = dados[1]
        relatorio['Acesso/Segundos'] = dados[2]

        relatorio_json = json.dumps(relatorio, sort_keys=True)

        return relatorio_json

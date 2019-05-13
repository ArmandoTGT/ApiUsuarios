from business.TiposRelatorio.templateRelatorio import templateRelatorio
from lxml import etree


class relatorio_html(templateRelatorio):

    def geraRelatorio(self, dados):
        # create XML 
        relatorio_xml = etree.Element('relatorioXML')
        quantidadeAcessos = etree.Element('quantidadeAcessos')
        quantidadeAcessos.text = str(dados[0])
        relatorio_xml.append(quantidadeAcessos)


        quantidadeAcessos = etree.Element('MinutosPassados')
        quantidadeAcessos.text = str(dados[1])
        relatorio_xml.append(quantidadeAcessos)


        quantidadeAcessos = etree.Element('AcessoSegundos')
        quantidadeAcessos.text = str(dados[2])
        relatorio_xml.append(quantidadeAcessos)

        return etree.tostring(relatorio_xml, pretty_print=True)


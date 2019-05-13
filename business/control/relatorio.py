from business.TiposRelatorio.relatorioJson import relatorio_json
from business.TiposRelatorio.relatorioHtml import relatorio_html


class relatorio:
	def __init__(self, tipo):

		tipo = tipo.lower()

		if (tipo == 'json'):
			self.__MeuRelatorio = relatorio_json()
		elif (tipo == 'html'):
			self.__MeuRelatorio = relatorio_html()

	def getRelatorio(self, dados):
		self.__MeuRelatorio.relatorio(dados)

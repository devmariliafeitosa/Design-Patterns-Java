from template_method.relatorios.relatorio_base import RelatorioBase

class RelatorioHTML(RelatorioBase):

    def formatar_dados(self, dados):
        # Organiza os dados em formato mais simples (lista)
        texto = ""
        total = 0

        for d in dados:
            texto += f"- {d['mes']}: R$ {d['valor']}\n"
            total += d['valor']

        texto += f"\nTOTAL: R$ {total}\n"
        return texto

    def exportar(self, conteudo):
        # Exibe o relatório no terminal (simulando HTML)
        print("\n[Relatório HTML]\n")
        print(conteudo)
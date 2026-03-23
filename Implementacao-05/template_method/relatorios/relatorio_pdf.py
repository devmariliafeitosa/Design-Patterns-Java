from template_method.relatorios.relatorio_base import RelatorioBase

class RelatorioPDF(RelatorioBase):

    def formatar_dados(self, dados):
        # Organiza os dados em formato de tabela simples (simulando PDF)
        texto = ""
        total = 0

        for d in dados:
            texto += f"{d['mes']:<12} | R$ {d['valor']:>6}\n"
            total += d['valor']

        texto += f"\nTOTAL        | R$ {total:>6}\n"
        return texto

    def exportar(self, conteudo):
        # Exibe o relatório no terminal (simulando exportação em PDF)
        print("\n[Relatório PDF]\n")
        print(conteudo)
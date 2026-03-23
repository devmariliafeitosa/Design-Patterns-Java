from template_method.relatorios.relatorio_pdf import RelatorioPDF
from template_method.relatorios.relatorio_html import RelatorioHTML

def main():
    # Cria e executa o relatório em formato PDF
    print("Gerando relatório PDF...")
    pdf = RelatorioPDF()
    pdf.gerar_relatorio()

    # Cria e executa o relatório em formato HTML
    print("\nGerando relatório HTML...")
    html = RelatorioHTML()
    html.gerar_relatorio()

if __name__ == "__main__":
    # Ponto de entrada do programa
    main()
from abc import ABC, abstractmethod
from template_method.dados.banco_dados import BancoDeDados

class RelatorioBase(ABC):

    def gerar_relatorio(self):
        # Método principal (Template Method)
        # Define o passo a passo fixo para gerar o relatório
        dados = self.ler_dados()
        dados_formatados = self.formatar_dados(dados)
        conteudo = self.adicionar_cabecalho(dados_formatados)
        conteudo = self.adicionar_rodape(conteudo)
        self.exportar(conteudo)

    def ler_dados(self):
        # Responsável por buscar os dados do "banco de dados"
        banco = BancoDeDados()
        return banco.buscar_dados()

    def adicionar_cabecalho(self, conteudo):
        # Adiciona o título e formatação inicial do relatório
        return (
            "==============================\n"
            "   RELATÓRIO FINANCEIRO\n"
            "==============================\n\n"
            + conteudo
        )

    def adicionar_rodape(self, conteudo):
        # Adiciona a parte final do relatório
        return (
            conteudo
            + "\n==============================\n"
              "        FIM DO RELATÓRIO\n"
              "=============================="
        )

    @abstractmethod
    def formatar_dados(self, dados):
        # Método abstrato
        # Cada tipo de relatório define como os dados serão organizados
        pass

    @abstractmethod
    def exportar(self, conteudo):
        # Método abstrato
        # Define como o relatório será exibido (no terminal, arquivo, etc.)
        pass
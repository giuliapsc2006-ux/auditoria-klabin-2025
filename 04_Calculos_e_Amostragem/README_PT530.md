# Evidências do PT 530 revisado

Os arquivos estão separados por natureza metodológica:

1. `01_Varredura_Integral/resultado_varredura_integral.csv`: testes aplicados a 100% da população. Não é amostragem.
2. `02_Selecao_Dirigida/selecao_dirigida_itens_de_risco.csv`: itens selecionados por exceção ou risco. Não permite projeção estatística.
3. `03_Amostra_Probabilistica/amostra_aleatoria_400_itens.csv`: amostra aleatória simples de 400 itens da população residual, semente 2026.
4. `resumo_pt530.csv`: parâmetros e resultados resumidos.
5. `metadados_pt530.json`: hash da base, contagens e advertência de uso.
6. `Planilha_PT530_Revisada.xlsx`: memória editável do procedimento.

A amostra apresentou zero exceções nas quatro regras programadas. Pela regra de três, o limite superior aproximado da taxa de exceção é 0,75%, com 95% de confiança, exclusivamente para a população residual sintética.

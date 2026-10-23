# Dossiê de Auditoria - Klabin S.A. (Exercício 2025)
**Universidade de Brasília — UnB**  
**Disciplina:** Auditoria 1 — CCA0024 — Turma 02 — 2026.2  
**Professor:** Lucas Oliveira Gomes Ferreira  
**Aluno:** [Giulia Prates Souto Cardoso]  
**Matrícula:** [241021462]  
## 1. Objetivo do Repositório
Este repositório contém os papéis de trabalho, as memórias de cálculo e a base de dados simulada referentes ao Dossiê de Auditoria da companhia Klabin S.A. (KLBN11), elaborados como requisito de avaliação da disciplina Auditoria 1. O trabalho contempla o planejamento e a execução simulada com base nas demonstrações contábeis de 2025.
## 2. Organização dos Arquivos
A estrutura do trabalho está dividida da seguinte forma:
- 📁 **`/01_Demonstracoes_Contabeis`**: Contém as DFP de 2025 da Klabin, Notas Explicativas e o Relatório do Auditor Independente original (fontes públicas reais).
- 📁 **`/02_Papeis_de_Trabalho`**: Arquivo PDF contendo os 27 Papéis de Trabalho (PT EC a PT 600) exigidos no roteiro.
- 📁 **`/03_Base_Simulada`**: arquivo compactado contendo a base de dados simulada com 500.000 linhas referente ao Ativo Imobilizado da Klabin e o código fonte em Python (`gerador_dados.ipynb`).
- 📁 **`/04_Calculos_e_Amostragem`**: Planilha demonstrando os cálculos de Materialidade (PT 320) e seleção de Amostras (PT 530).
### Dicionário de Variáveis da Base:
*   **Num_Plaqueta:** Código alfanumérico único para identificação física e rastreabilidade do ativo imobilizado.
*   **Categoria:** Classificação contábil do ativo (ex: Máquinas, Edificações, Florestas Plantadas).
*   **Data_Aquisicao:** Data de entrada do ativo em operação ou data do plantio.
*   **Valor_Aquisicao_BRL:** Custo histórico de aquisição ou formação do ativo em Reais (R$).
*   **Unidade_Negocio:** Centro de custo onde o ativo está alocado.
*   **Depreciacao_Acumulada_BRL:** Montante acumulado de depreciação/exaustão até 31/12/2025.
*   **Valor_Liquido_Contabil_BRL:** Valor residual do ativo (Aquisição deduzida da Depreciação).
## 4. Instruções para Reprodução dos Dados
Para gerar novamente a base de dados e reproduzir os "erros" de auditoria inseridos para os testes do PT 530:
1. Acesse o Google Colab.
2. Faça o upload do arquivo `gerador_dados.ipynb` presente na pasta `/03_Base_Simulada`.
3. Execute a célula de código. O arquivo `.csv` será gerado automaticamente mantendo a mesma semente randômica (seed 2026).

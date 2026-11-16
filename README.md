# Dossiê de Auditoria - Klabin S.A. - Exercício 2025

**Universidade de Brasília - UnB**  
**Disciplina:** Auditoria 1 - CCA0024 - Turma 02 - 2026.2  
**Professor:** Lucas Oliveira Gomes Ferreira  
**Aluna:** Giulia Prates Souto Cardoso  
**Matrícula:** 241021462

## 1. Objetivo

Este repositório reúne o dossiê acadêmico, as demonstrações financeiras utilizadas, a base sintética, os códigos e os papéis de trabalho relativos à Klabin S.A. O exercício utiliza informações públicas e dados sintéticos e não constitui auditoria contratada nem fornece opinião ou asseguração independente.

## 2. Revisão metodológica

Esta versão incorpora ajustes realizados após a avaliação preliminar:

1. separação entre testes automatizados sobre 100% da base, seleção dirigida e amostragem probabilística;
2. aplicação de amostra aleatória simples de 400 itens à população residual, com semente 2026;
3. registro do risco amostral e do limite superior aproximado de 0,75% para a taxa de exceção, restrito à população sintética;
4. eliminação de conclusões que associavam exceções artificiais a falhas de controles da Klabin S.A.;
5. revisão dos PT 265, 320, 330, 450, 500, 530, 540 e 600;
6. revisão da conclusão integrada, sem emissão ou sustentação de opinião profissional independente.

## 3. Organização do repositório

- `01_Demonstracoes_Contabeis`: DFP de 2025, comparativos, notas, relatório do auditor e relação de fontes.
- `02_Papeis_de_Trabalho`: dossiê final em PDF, versão editável em Word e anexos do PT 530.
- `03_Base_Simulada`: base original, gerador original, script de análise revisado e instruções.
- `04_Calculos_e_Amostragem`: varredura integral, seleção dirigida, amostra probabilística e memória editável.
- `Matriz_Cobertura_Normas.xlsx`: vinculação entre normas, papéis e evidências.

## 4. Base sintética

A base contém 500.015 registros. O código gera inicialmente 500.000 itens e acrescenta 15 cópias para simular duplicidades. A soma do valor líquido contábil da população é R$ 54.069.914.441,78 e não corresponde ao saldo divulgado do imobilizado consolidado da Klabin S.A. Essa diferença é limitação do desenho original da base.

As exceções, inclusive valores negativos, datas futuras e duplicidades, foram inseridas artificialmente. Elas não representam registros, distorções ou deficiências reais da companhia.

## 5. Reprodução do PT 530

```bash
python -m pip install -r 03_Base_Simulada/requirements.txt
python 03_Base_Simulada/analise_pt530.py \
  --base 03_Base_Simulada/base_imobilizado_klabin_2025.csv \
  --saida resultados_pt530
```

## 6. Classificação dos procedimentos

- **EP**: realizado com evidência pública;
- **PA**: planejado por falta de acesso;
- **SD**: simulado para fins didáticos.

Nenhuma confirmação, inspeção física, acesso a sistemas, entrevista ou comunicação com terceiros foi apresentada como realizada.

## 7. Conclusão

Os documentos públicos permitem compreender a entidade e identificar riscos. Os testes sobre a base demonstram técnicas de análise e amostragem em uma população artificial. O conjunto não fornece evidência suficiente para emitir ou sustentar opinião profissional independente sobre as demonstrações individuais ou consolidadas da Klabin S.A.

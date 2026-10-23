import pandas as pd
import numpy as np
from datetime import datetime
from google.colab import files
# 1. Configurações Iniciais
num_linhas = 500000
np.random.seed(2026) # Para garantir que a base gerada seja sempre igual
# 2. Categorias e Parâmetros reais típicos da Klabin
categorias = ['Máquinas e Equipamentos', 'Edificações e Benfeitorias', 
              'Equipamentos Florestais', 'Móveis e Utensílios', 'Veículos', 'Florestas Plantadas']
prob_categorias = [0.45, 0.15, 0.10, 0.05, 0.05, 0.20]
taxas_depreciacao_anual = {
    'Máquinas e Equipamentos': 0.05,      # 20 anos
    'Edificações e Benfeitorias': 0.04,   # 25 anos
    'Equipamentos Florestais': 0.10,      # 10 anos
    'Móveis e Utensílios': 0.10,          # 10 anos
    'Veículos': 0.20,                     # 5 anos
    'Florestas Plantadas': 0.14           # ~7 anos (ciclo do eucalipto/pinus)
}
# 3. Gerando os dados base
cat_escolhidas = np.random.choice(categorias, num_linhas, p=prob_categorias)
datas_base = pd.date_range(start='2015-01-01', end='2025-12-31')
datas_aquisicao = np.random.choice(datas_base, num_linhas)
valores_aquisicao = np.round(np.random.lognormal(mean=11, sigma=1.5, size=num_linhas), 2)
df = pd.DataFrame({
    'Num_Plaqueta': [f"KLB-{str(i).zfill(7)}" for i in range(1, num_linhas + 1)],
    'Categoria': cat_escolhidas,
    'Data_Aquisicao': datas_aquisicao,
    'Valor_Aquisicao_BRL': valores_aquisicao,
    'Unidade_Negocio': np.random.choice(['Unidade Puma', 'Unidade Monte Alegre', 'Florestal PR', 'Sede SP', 'Unidade Correia Pinto'], num_linhas)
})
# 4. Calculando Depreciação até 31/12/2025
df['Taxa_Anual'] = df['Categoria'].map(taxas_depreciacao_anual)
df['Anos_Uso'] = (pd.to_datetime('2025-12-31') - df['Data_Aquisicao']).dt.days / 365.25
df['Depreciacao_Acumulada_BRL'] = np.round(df['Valor_Aquisicao_BRL'] * df['Taxa_Anual'] * df['Anos_Uso'], 2)
# O bem não pode depreciar mais que 100% de seu valor
df['Depreciacao_Acumulada_BRL'] = np.minimum(df['Depreciacao_Acumulada_BRL'], df['Valor_Aquisicao_BRL'])
df['Valor_Liquido_Contabil_BRL'] = df['Valor_Aquisicao_BRL'] - df['Depreciacao_Acumulada_BRL']
# 5. INSERINDO EXCEÇÕES (ERROS DE AUDITORIA PARA O PT 530)
# Erro A: 25 itens com Valor Líquido NEGATIVO (Erro na rotina do sistema)
idx_erros_neg = np.random.choice(df.index, 25, replace=False)
df.loc[idx_erros_neg, 'Valor_Liquido_Contabil_BRL'] = -45200.50
# Erro B: 40 itens com data de aquisição no FUTURO (Ex: Inserido 2026 em vez de 2025)
idx_erros_data = np.random.choice(df.drop(idx_erros_neg).index, 40, replace=False)
df.loc[idx_erros_data, 'Data_Aquisicao'] = pd.to_datetime('2026-08-15')
# Erro C: 15 plaquetas duplicadas (Falta de controle físico)
idx_duplicados = np.random.choice(df.index, 15, replace=False)
df_duplicado = df.loc[idx_duplicados].copy()
df = pd.concat([df, df_duplicado], ignore_index=True)
# 6. Limpeza e Exportação
df = df.drop(columns=['Taxa_Anual', 'Anos_Uso'])
nome_arquivo = 'base_imobilizado_klabin_2025.csv'
df.to_csv(nome_arquivo, index=False)
print(f"Base gerada com {len(df)} linhas!")
files.download(nome_arquivo)

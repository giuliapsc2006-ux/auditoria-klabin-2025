#!/usr/bin/env python3
import argparse, hashlib, json
from pathlib import Path
import numpy as np, pandas as pd

def main():
 ap=argparse.ArgumentParser(description='Refaz o PT 530 sobre a base sintética entregue.')
 ap.add_argument('--base',default='base_imobilizado_klabin_2025.csv')
 ap.add_argument('--saida',default='resultados_pt530')
 ap.add_argument('--semente',type=int,default=2026)
 ap.add_argument('--amostra',type=int,default=400)
 a=ap.parse_args(); base=Path(a.base); out=Path(a.saida); out.mkdir(parents=True,exist_ok=True)
 df=pd.read_csv(base,parse_dates=['Data_Aquisicao']); corte=pd.Timestamp('2025-12-31'); me=83_279_105.00
 df['exc_negativo']=df.Valor_Liquido_Contabil_BRL<0
 df['exc_data_futura']=df.Data_Aquisicao>corte
 df['exc_plaqueta_duplicada']=df.Num_Plaqueta.duplicated(keep=False)
 df['exc_equacao']=((df.Valor_Aquisicao_BRL-df.Depreciacao_Acumulada_BRL)-df.Valor_Liquido_Contabil_BRL).abs()>0.01
 risk_mask=df[['exc_negativo','exc_data_futura','exc_plaqueta_duplicada','exc_equacao']].any(axis=1)|(df.Valor_Liquido_Contabil_BRL.abs()>=me)
 risk=df[risk_mask].copy(); residual=df[~risk_mask].copy()
 rng=np.random.default_rng(a.semente); idx=rng.choice(residual.index.to_numpy(),size=a.amostra,replace=False); sample=df.loc[idx].copy().sort_index()
 sample['metodo_selecao']='Amostragem aleatória simples da população residual'; sample['semente']=a.semente
 dev=int(sample[['exc_negativo','exc_data_futura','exc_plaqueta_duplicada','exc_equacao']].any(axis=1).sum()); upper=(3/a.amostra if dev==0 else None)
 risk.to_csv(out/'selecao_dirigida_itens_de_risco.csv',index=False,encoding='utf-8-sig'); sample.to_csv(out/'amostra_aleatoria_400_itens.csv',index=False,encoding='utf-8-sig')
 rows=[['Valor líquido negativo',int(df.exc_negativo.sum())],['Data após 31/12/2025',int(df.exc_data_futura.sum())],['Linhas em grupos de plaquetas duplicadas',int(df.exc_plaqueta_duplicada.sum())],['Equação contábil divergente',int(df.exc_equacao.sum())]]
 pd.DataFrame(rows,columns=['Teste','Ocorrencias']).to_csv(out/'resultado_varredura_integral.csv',index=False,encoding='utf-8-sig')
 meta={'arquivo':base.name,'sha256':hashlib.sha256(base.read_bytes()).hexdigest(),'registros':len(df),'ids_unicos':int(df.Num_Plaqueta.nunique()),'saldo_liquido':round(float(df.Valor_Liquido_Contabil_BRL.sum()),2),'selecao_dirigida':len(risk),'populacao_residual':len(residual),'tamanho_amostra':a.amostra,'excecoes_amostra':dev,'limite_superior_aprox_95':upper,'advertencia':'Resultados restritos à base sintética; não representam a Klabin S.A.'}
 (out/'metadados_pt530.json').write_text(json.dumps(meta,ensure_ascii=False,indent=2),encoding='utf-8'); print(json.dumps(meta,ensure_ascii=False,indent=2))
if __name__=='__main__': main()

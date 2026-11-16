# Base sintética do ativo imobilizado

## Arquivos que devem ser preservados nesta pasta
- `base_imobilizado_klabin_2025.csv`
- `gerador_base_500k.py`

Esses dois arquivos já estão no repositório e **não devem ser substituídos**.

## Arquivo novo
- `analise_pt530.py`: executa a varredura integral, a seleção dirigida e a amostragem probabilística revisada.

## Características da base entregue
- 500.015 registros;
- 500.000 números de plaqueta únicos;
- 15 registros duplicados além da primeira ocorrência;
- 25 valores líquidos negativos inseridos pelo gerador;
- 40 datas de aquisição posteriores a 31/12/2025;
- soma do valor líquido contábil: R$ 54.069.914.441,78.

## Limitação essencial
A população é totalmente sintética e não foi extraída do razão auxiliar, ERP ou cadastro patrimonial da Klabin S.A. O total da base não corresponde ao saldo divulgado do imobilizado consolidado. As exceções foram inseridas pelo próprio código e não constituem distorções, deficiências de controle ou falhas sistêmicas da companhia.

## Execução
```bash
python -m pip install -r 03_Base_Simulada/requirements.txt
python 03_Base_Simulada/analise_pt530.py \
  --base 03_Base_Simulada/base_imobilizado_klabin_2025.csv \
  --saida resultados_pt530
```

import pandas as pd
import numpy as np

# 1. Carregar o arquivo (utilizando ';' como separador)
df = pd.read_csv('notas.csv', sep=';')

# 2. Limpar a coluna 'RA': remover texto "RA", espaços e converter vazios em NaN
df['RA'] = df['RA'].astype(str).str.replace('RA', '', case=False).str.strip()
df['RA'] = df['RA'].replace(['nan', '', 'None'], np.nan)

# 3. Padronizar a coluna 'Nome' (opcional para melhor organização)
df['Nome'] = df['Nome'].astype(str).str.strip().str.title()
df['Nome'] = df['Nome'].replace(r'\s+', ' ', regex=True)

# 4. Limpar colunas numéricas: trocar vírgula por ponto e converter para número
colunas_notas = ['Nota01', 'TF01', 'Nota02', 'TF02']
for col in colunas_notas:
    df[col] = df[col].astype(str).str.strip().str.replace(',', '.')
    # O parâmetro errors='coerce' converte textos inválidos (ex: 'FALTOU') e espaços em NaN (N/A)
    df[col] = pd.to_numeric(df[col], errors='coerce')

# 5. Identificar e separar as linhas que contêm valores N/A (NaN) em qualquer coluna
mascara_na = df.isna().any(axis=1)

df_com_na = df[mascara_na]
df_limpo = df[~mascara_na]

# 6. Organizar os itens limpos (ordenando em ordem alfabética pelo Nome, por exemplo)
df_limpo = df_limpo.sort_values(by='Nome').reset_index(drop=True)

# 7. Exibir ou salvar os resultados
print("--- Dados Limpos e Organizados ---")
print(df_limpo.head())

print("\n--- Dados Separados com N/A ---")
print(df_com_na.head())

# Salvar os DataFrames em novos arquivos CSV
df_limpo.to_csv('notas_organizadas.csv', index=False, sep=';')
df_com_na.to_csv('notas_com_problemas.csv', index=False, sep=';')
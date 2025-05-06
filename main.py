import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler

# ID: ID of each client
# LIMIT_BAL: Amount of given credit in NT dollars (includes individual and family/supplementary credit
# SEX: Gender (1=male, 2=female)
# EDUCATION: (1=graduate school, 2=university, 3=high school, 4=others, 5=unknown, 6=unknown)
# MARRIAGE: Marital status (1=married, 2=single, 3=others)
# AGE: Age in years
# PAY_0: Repayment status in September, 2005 (-1=pay duly, 1=payment delay for one month, 2=payment delay for two months, … 8=payment delay for eight months, 9=payment delay for nine months and above)
# PAY_2: Repayment status in August, 2005 (scale same as above)
# PAY_3: Repayment status in July, 2005 (scale same as above)
# PAY_4: Repayment status in June, 2005 (scale same as above)
# PAY_5: Repayment status in May, 2005 (scale same as above)
# PAY_6: Repayment status in April, 2005 (scale same as above)
# BILL_AMT1: Amount of bill statement in September, 2005 (NT dollar)
# BILL_AMT2: Amount of bill statement in August, 2005 (NT dollar)
# BILL_AMT3: Amount of bill statement in July, 2005 (NT dollar)
# BILL_AMT4: Amount of bill statement in June, 2005 (NT dollar)
# BILL_AMT5: Amount of bill statement in May, 2005 (NT dollar)
# BILL_AMT6: Amount of bill statement in April, 2005 (NT dollar)
# PAY_AMT1: Amount of previous payment in September, 2005 (NT dollar)
# PAY_AMT2: Amount of previous payment in August, 2005 (NT dollar)
# PAY_AMT3: Amount of previous payment in July, 2005 (NT dollar)
# PAY_AMT4: Amount of previous payment in June, 2005 (NT dollar)
# PAY_AMT5: Amount of previous payment in May, 2005 (NT dollar)
# PAY_AMT6: Amount of previous payment in April, 2005 (NT dollar)
# default.payment.next.month: Default payment (1=yes, 0=no)

# Leitura do arquivo CSV
df = pd.read_csv('data/UCI_Credit_Card.csv')

# Exibe as primeiras linhas do DataFrame
print("\nPrimeiras linhas do dataset:")
print(df.head())

# Informações gerais sobre o DataFrame
print("\nInformações gerais do DataFrame:")
print(df.info())

# Verificação de valores nulos
print("\nVerificação de valores nulos:")
print(df.isnull().sum())

# Exibição dos nomes das colunas
print("\nNomes das colunas:")
print(df.columns.tolist())

# Estatísticas descritivas
print("\nEstatísticas descritivas:")
print(df.describe())

# Contagem de valores únicos por coluna
print("\nValores únicos por coluna:")
print(df.nunique())

# Verificação de registros duplicados
print("\nQuantidade de registros duplicados:")
print(df.duplicated().sum())

# Define estilo dos gráficos
sns.set(style='whitegrid')

# Histograma das variáveis numéricas
print("Gerando histogramas das variáveis numéricas...")
df.hist(bins=30, figsize=(20, 15), edgecolor='black')
plt.tight_layout()
plt.savefig("histogramas_variaveis.png")  # Salva em arquivo
plt.close()

# Frequência de inadimplência
print("Distribuição de inadimplentes (default.payment.next.month):")
print(df['default.payment.next.month'].value_counts())

# Gráfico de barras da inadimplência
plt.figure(figsize=(6, 4))
sns.countplot(x='default.payment.next.month', data=df)
plt.title("Frequência de Inadimplência")
plt.xlabel("Inadimplente (1 = sim, 0 = não)")
plt.ylabel("Quantidade")
plt.tight_layout()
plt.savefig("frequencia_inadimplencia.png")
plt.close()

# Boxplots para algumas variáveis importantes
variaveis_boxplot = ['LIMIT_BAL', 'AGE', 'BILL_AMT1', 'PAY_AMT1', 'EDUCATION', 'MARRIAGE']
plt.figure(figsize=(18, 10))
for i, col in enumerate(variaveis_boxplot, 1):
    plt.subplot(2, 3, i)
    sns.boxplot(x=df[col])
    plt.title(f'Boxplot de {col} (Antes)')
plt.tight_layout()
plt.savefig("boxplots_antes.png")
plt.close()

print("Análise exploratória finalizada. Imagens salvas no diretório.")

# Verificando valores únicos em EDUCATION e MARRIAGE
print("Valores únicos em EDUCATION:", df['EDUCATION'].unique())
print("Valores únicos em MARRIAGE:", df['MARRIAGE'].unique())

# Tratando valores inconsistentes
df['EDUCATION'] = df['EDUCATION'].replace([0, 5, 6], 4)  # agrupando como "outros"
df['MARRIAGE'] = df['MARRIAGE'].replace(0, 3)  # tratando como "outros"

# Verificando valores novamente
print("Após tratamento:")
print("EDUCATION:", df['EDUCATION'].unique())
print("MARRIAGE:", df['MARRIAGE'].unique())

# Codificação (get_dummies)
df_encoded = pd.get_dummies(df, columns=['SEX', 'EDUCATION', 'MARRIAGE'], drop_first=True)

# Normalização
scaler = StandardScaler()
numerical_cols = ['LIMIT_BAL', 'AGE'] + [f'BILL_AMT{i}' for i in range(1,7)] + [f'PAY_AMT{i}' for i in range(1,7)]
df_encoded[numerical_cols] = scaler.fit_transform(df_encoded[numerical_cols])

plt.figure(figsize=(18, 10))
for i, col in enumerate(variaveis_boxplot, 1):
    plt.subplot(2, 3, i)
    sns.boxplot(x=df[col])
    plt.title(f'Boxplot de {col} (Depois)')
plt.tight_layout()
plt.savefig("boxplots_depois.png")
plt.close()
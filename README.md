# Checklist para o Trabalho de Análise de Crédito

## 📌 1. Leitura e Exploração Inicial dos Dados (EDA)
- [x] Importar bibliotecas (`pandas`, `numpy`, `matplotlib`, `seaborn`)
- [x] Carregar o CSV com `pandas.read_csv()`
- [x] Verificar os primeiros registros (`df.head()`)
- [x] Verificar tipos de dados e valores nulos (`df.info()`, `df.isnull().sum()`)

## 📊 2. Análise Exploratória de Dados (EDA)
- [x] Estatísticas descritivas (`df.describe()`)
- [x] Distribuições das variáveis numéricas (histogramas, boxplots)
- [x] Correlação entre variáveis (heatmap com seaborn)
- [x] Frequência de inadimplência (`default.payment.next.month`)

## 🛠️ 3. Pré-processamento
- [x] Tratar valores inconsistentes em variáveis categóricas (`EDUCATION`, `MARRIAGE`)
- [x] Codificar variáveis se necessário (ex.: `pd.get_dummies`)
- [x] Normalizar dados com `StandardScaler` ou `MinMaxScaler`
- [x] Verificar outliers e decidir se vai removê-los ou não

## 🤖 4. Modelagem
- [ ] Separar os dados em treino e teste (ex.: 70%/30%)
- [ ] Treinar pelo menos 2 algoritmos:
  - [ ] `LogisticRegression`
  - [ ] `RandomForestClassifier`
  - [ ] `XGBoost` (opcional)
- [ ] Avaliar os modelos com:
  - [ ] Acurácia
  - [ ] Precisão
  - [ ] Recall
  - [ ] F1-Score
  - [ ] Curva ROC-AUC
  - [ ] Matriz de confusão
- [ ] Otimizar hiperparâmetros com `GridSearchCV` ou `RandomizedSearchCV`

## 🚀 5. Entrega Interativa
**Escolher uma opção:**
- [ ] **Opção A:** Criar um Jupyter Notebook organizado com seções de markdown
- [ ] **Opção B:** Criar um app com Streamlit que permita:
  - [ ] Ajustar parâmetros dos modelos
  - [ ] Visualizar métricas em tempo real

## 📦 6. Entregáveis
- [ ] Notebook `.ipynb` ou pasta com scripts + `requirements.txt`
- [ ] Relatório resumido (pode ser em markdown ou PDF)
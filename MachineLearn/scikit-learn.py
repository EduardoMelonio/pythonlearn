import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

# Simulando um dataset com indicadores técnicos
np.random.seed(42)
n = 1000

data = pd.DataFrame({
    'RSI': np.random.uniform(10, 90, n),
    'MACD': np.random.normal(0, 1, n),
    'Volume': np.random.uniform(1e5, 1e7, n),
    'Bollinger_Upper': np.random.uniform(50000, 60000, n),
    'Bollinger_Lower': np.random.uniform(40000, 50000, n),
    'Close': np.random.uniform(45000, 55000, n)
})

# Criando a variável alvo: 1 se o preço sobe 1% ou mais na próxima barra, senão 0
future_returns = np.random.uniform(-0.02, 0.02, n)
data['Target'] = (future_returns > 0.01).astype(int)

# Seleção de features e target
X = data[['RSI', 'MACD', 'Volume', 'Bollinger_Upper', 'Bollinger_Lower', 'Close']]
y = data['Target']

# Divisão treino/teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Treinamento do modelo
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Avaliação
y_pred = model.predict(X_test)
report = classification_report(y_test, y_pred, output_dict=True)
report_df = pd.DataFrame(report).transpose()

import ace_tools as tools; tools.display_dataframe_to_user(name="Relatório de Classificação", dataframe=report_df)

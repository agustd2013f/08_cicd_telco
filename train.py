import joblib
import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split


def train_model():
  np.random.seed(42)
  n_samples = 1000

  tenure = np.random.randint(1, 72, n_samples)
  monthly_charges = np.random.uniform(20.0, 120.0, n_samples)
  total_charges = tenure * monthly_charges + np.random.normal(0, 50, n_samples)

  churn_prob = 1 / (
      1
      + np.exp(
          -(
              0.05 * monthly_charges
              - 0.08 * tenure
              - 0.001 * total_charges
              + 0.5
          )
      )
  )
  churn = (churn_prob > 0.5).astype(int)

  df = pd.DataFrame({
      'tenure': tenure,
      'monthly_charges': monthly_charges,
      'total_charges': total_charges,
      'churn': churn,
  })

  X = df[['tenure', 'monthly_charges', 'total_charges']]
  y = df['churn']

  X_train, X_test, y_train, y_test = train_test_split(
      X, y, test_size=0.2, random_state=42
  )

  model = LogisticRegression()
  model.fit(X_train, y_train)

  joblib.dump(model, 'model.joblib')
  print('Modelo entrenado exitosamente y guardado en model.joblib')


if __name__ == '__main__':
  train_model()
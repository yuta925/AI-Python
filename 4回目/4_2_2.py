# ワーク：2.2.クロス集計処理

# NumPy、Pandasの読み込み
import numpy as np
import pandas as pd

# クロス集計に使用するデータの作成
sex = np.random.choice(['male', 'female'], size=20)
sufficiency = np.random.choice([1, 2, 3, 4, 5], size=20)
age = np.random.choice([20, 30, 40, 50], size=20)

# データフレーム作成
df = pd.DataFrame({'sex': sex, 'sufficiency': sufficiency, 'age': age})
print(f'df：\n{df}\n')

# 満足度結果を年齢、性別別でクロス集計
df_crs = pd.crosstab(index=[df['sufficiency'], df['age']], columns=df['sex'])
print(f'クロス集計：\n{df_crs}\n')

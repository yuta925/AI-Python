import pandas as pd
import numpy as np
np.random.seed(0)
df1 = pd.DataFrame({'XY':np.random.choice(['X','Y'],6),
                    'value':np.random.choice([1,2,np.nan],6)})
print(f'初期データ：\n{df1}\n')

# 重複データの確認
df2 = df1.duplicated()
print(f'重複確認：\n{df2}\n')

# df1の重複データを削除
df3 = df1.drop_duplicates(["XY","value"])
print(f'重複削除：\n{df3}\n')

# NaNを含む行を削除
df4 = df3.dropna()
print(f'NaNデータ削除：\n{df4}\n')

#クロス集計処理
df5 = pd.crosstab(index=df4["XY"], columns=df4["value"])
print(f'クロス集計：\n{df5}\n')
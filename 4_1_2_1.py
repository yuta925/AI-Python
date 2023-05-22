# ワーク：1.2.データの連結

# NumPy、Pandasの読み込み
import numpy as np
import pandas as pd

# numpyでの連結
# 2×2の配列を作成
array1 = np.arange(4).reshape(2, 2)
print(f'array1：\n{array1}\n')

# 縦方向（axis=0）に連結
print(f'縦方向の連結：\n{np.concatenate([array1,array1],axis=0)}\n')
# 横方向（axis=1）に連結
print(f'横方向の連結：\n{np.concatenate([array1,array1],axis=1)}\n')


# pandasでの連結
# 2つのSeriesを作成
series1 = pd.Series([0, 1, 2], index=["A", "B", "X"])
series2 = pd.Series([3, 4], index=["X", "Y"])

# 2つを縦方向（axis=0）に連結
print(f'縦方向の連結：\n{pd.concat([series1,series2],axis=0)}\n')
# 2を横方向（axis=1）に連結
print(f'横方向の連結：\n{pd.concat([series1,series2],axis=1)}\n')


# 2つのDataFrameを作成
df1 = pd.DataFrame(np.random.randn(2, 2), columns=['X', 'Y'])
df2 = pd.DataFrame(np.random.randn(3, 2), columns=['Y', 'Q'])

# 2つのDataFrameを連結
print(f'DataFrameの連結：\n{pd.concat([df1,df2],ignore_index=True)}\n')

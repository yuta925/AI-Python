# ワーク：1.1.Pythonによるデータの結合
# 内部結合/部分外部結合/外部結合

# NumPy、Pandasの読み込み
import numpy as np
import pandas as pd

# DataFrame を2つ作成
df1 = pd.DataFrame({'key':['X', 'Z', 'Y', 'Z', 'X', 'X'], 'data1': np.arange(6)})
df2 = pd.DataFrame({'key':['Q', 'Y', 'Z'], 'data2':[1,2,3]})
print(f'df1：\n{df1}\ndf2：\n{df2}\n')

# DataFrame 2つを内部結合
print(f'内部結合：\n{pd.merge(df1, df2)}\n')

# 右外部結合
print(f'右外部結合：\n{pd.merge(df1, df2 ,on="key", how="right")}\n')

# 完全外部結合
print(f'完全外部結合：\n{pd.merge(df1, df2 ,on="key", how="outer")}\n')

# 複数キー×複数キーでの結合
# keyに複数の値を持つDataFrameを作成
df3 = pd.DataFrame({'key': ['X','X','X','Y','Z','Z'], 'data3': range(6)})
df4 = pd.DataFrame({'key': ['Y','Y','X','X','Z'], 'data4': range(5)})
print(f'df3：\n{df3}\ndf4：\n{df4}\n')

# DataFrame 2つを内部結合
print(f'複数キー×複数キー：\n{pd.merge(df3, df4)}\n')

# indexでの結合
# indexをキーに持つDataFrameを作成
df5 = pd.DataFrame({'key': ['X','Y','Z','X','Y'], 'data5': range(5)})
df6 = pd.DataFrame ({'data6': [10, 20]}, index=['X', 'Y'])
print(f'df5：\n{df5}\ndf6：\n{df6}\n')

# 左(df5)はkey列をキーに、右(df6)はindexをキーにmergeを実行する
df7 = pd.merge(df5, df6, left_on='key',right_index=True)
print(f'キーを指定してmerge：\n{df7}')
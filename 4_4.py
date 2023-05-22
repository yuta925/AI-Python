# ワーク：2.4.欠損値・外れ値の処理

# Pandasの読み込み
import numpy as np
import pandas as pd

# 外れ値を含む処理
# circle.csvを読み込む
df = pd.read_csv("circle.csv")
print(f'circle：\n{df}\n')

# NaNを含む行を削除する
df1 = df.dropna()
print(f'NaNデータ削除：\n{df1}\n')

# NaNを特定の値に置換する
df2 = df.fillna({"Circle": "Not Belonging"})
print(f'NaNデータ置換：\n{df2}\n')


# 四分位数による外れ値の判定
array_data = np.array([1, 2, 3, 4, 9, 10, 13, 20, 23, 34, 38, 39, 40])
print(f'配列：{array_data}')

q1 = np.percentile(array_data, 25)
print(f'第一四分位：{q1}')

q2 = np.percentile(array_data, 50)
print(f'第二四分位：{q2}')

q3 = np.percentile(array_data, 75)
print(f'第三四分位：{q3}\n')

iqr = q3 - q1
print(f'四分位範囲：{iqr}\n')

# 下限
lower_bound = q1 - (iqr * 1.5)
# 上限
upper_bound = q3 + (iqr * 1.5)

print(f'{lower_bound}以下の値、{upper_bound}以上の値は外れ値')

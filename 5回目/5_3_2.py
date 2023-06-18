# ワーク：3.2.Seabornの操作②(折れ線グラフの作成)

# 警告文の非表示
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
import warnings
warnings.simplefilter('ignore')

# Seaborn、pyplot、NumPy、Pandasの読み込み

# 365個 x 4セットのランダムなデータを生成
rs = np.random.RandomState(365)
values = rs.randn(365, 4).cumsum(axis=0)
print(f'4セットそれぞれの上位10件表示：\n{values[0:10]}\n')

# 365個のデータを1年365日のデータとみなし、4つのデータセットそれぞれの7日間の移動平均を求める。
dates = pd.date_range('1 1 2021', periods=365, freq='D')
data1 = pd.DataFrame(values, dates, columns=['A', 'B', 'C', 'D'])
data2 = data1.rolling(7).mean()
print(f'移動平均：\n{data2}\n')

# 折れ線グラフを生成する。
sns.lineplot(data=data2, palette='dark')
plt.show()
plt.clf()

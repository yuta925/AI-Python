# ワーク：3.1.Seabornの操作②(棒グラフの作成)

# 警告文の非表示
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
import warnings
warnings.simplefilter('ignore')

# Seaborn、pyplot、NumPyの読み込み

# x軸のデータの作成
x = np.array(list('ABCDEFGHIJ'))
print(f'x：{x}')

# y軸のデータの作成
y = np.arange(1, 11)
print(f'y：{y}\n')

# 棒グラフの生成
sns.barplot(x, y)
plt.show()
plt.clf()

# 棒グラフの色パターンの変更
sns.barplot(x, y, palette='pastel')
plt.show()
plt.clf()


# データの平均値と信頼区間を可視化した棒グラフの作成
# 曜日ごとのチップの金額に関するデータを利用
tips = sns.load_dataset('tips')
print(f'チップの金額データ：\n{tips[0:10]}\n')

# 曜日と時間帯によるチップの平均額を棒グラフで表示
sns.barplot(x='day', y='tip', data=tips, hue='time')
plt.show()
plt.clf()

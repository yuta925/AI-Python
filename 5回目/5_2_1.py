# ワーク：2.1.Seabornの操作①(ヒストグラムの作成)

# Seaborn、Pyplotの読み込み
from matplotlib import pyplot as plt
import seaborn as sns
import numpy as np


# 警告文を非表示
import warnings
warnings.simplefilter('ignore')


# ランダムデータの作成
random_data = np.random.normal(size=1000)

# 先頭の10個を表示する
print(f'先頭10個：\n{random_data[0:10]}\n')

# ヒストグラムの生成
sns.distplot(random_data, kde=False, bins=100)
plt.show()
plt.clf()

# ヒストグラムにカーネル密度推定を重ね合わせて表示する
sns.distplot(random_data, kde=True, bins=100)
plt.show()
plt.clf()

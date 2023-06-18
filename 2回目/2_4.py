# ワーク：Matplotlibの操作方法

# Matplotlibパッケージの読み込み
import numpy as np
from matplotlib import pyplot as plt
import numpy.random as random
import matplotlib.pyplot as plt
import matplotlib as mpl

# 折れ線グラフの作成
# データの作成
x = [1, 2, 3, 4, 5, 6]
y = [100, 250, 200, 300, 310, 200]

plt.plot(x,  y)

plt.grid(True)
plt.show()
plt.close()


# 散布図の作成
# パッケージの読み込み

# シードを固定して、乱数を生成
random.seed(0)
x = random.rand(100)
y = random.rand(100)

# 散布図を描画
plt.scatter(x, y)
plt.grid(True)
plt.show()
plt.close()


# ヒストグラムの作成
# パッケージの読み込み

# 正規乱数を1000個生成
x = np.random.normal(size=1000)

# ヒストグラムを描画
plt.hist(x, bins=10)
plt.grid(True)
plt.show()
plt.close()

# ワーク：NumPyの操作方法②

# 乱数の発生のためのモジュール読み込み
import numpy as np
import numpy.random as random

# 乱数の生成
# seedを設定することで乱数を固定化
random.seed(0)

# 正規分布(平均0,分散1)の乱数5個作成
norm_random_data = random.randn(5)
print(f'乱数：{norm_random_data}\n')


# 行列生成
# 1次元配列の作成
# np.arange(最初の項,終点の項,公差)
multi_array_data1 = np.arange(9)
print(f'1次元配列：\n{multi_array_data1}\n')

# 3×3行列の作成
multi_array_data2 = np.arange(9).reshape(3, 3)
print(f'3×3行列：\n{multi_array_data2}\n')

# 1行目、全ての列を指定
print(f'1行目：{multi_array_data2[0,:]}')
# 全ての行、1列目を指定
print(f'1列目：{multi_array_data2[:,0]}\n')

# 2つの行列の掛算
# 行列の作成
a = np.array([1, 3, 5, 7]).reshape(2, 2)
b = np.array([2, 8, 0, 10]).reshape(2, 2)
print(f'行列 a：\n{a}')
print(f'行列 b：\n{b}\n')

# 2×2行列aと2×2行列bの掛け算の結果
print(f'行列a × 行列b：\n{np.dot(a,b)}')
# 2=(1*2)+(3*0)
# 38=(1*8)+(3*10)
# 10=(5*2)+(7*0)
# 110=(5*8)+(7*10)

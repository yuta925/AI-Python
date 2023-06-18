# 解説：NumPyの操作方法①

# 【問題】
# 以下の3つの演習を行い、プログラムの空欄を埋めて完成させてください。
# 1次元の要素数3の配列をdata1として作成する
# 配列data1の要素をそれぞれ3乗し、data2として作成する
# 配列data1の要素にそれぞれ2を足し、data3として作成する
# 配列data3の次元数と要素数を確認する

import numpy as np

# 1次元の要素数3の配列を1つ作る
data1 = np.array([1, 2, 3])
print(f'1次元,要素数3の配列：{data1}\n')

# 配列の要素をそれぞれ3乗する
data2 = data1 ** 3
print(f'data1の要素の3乗：{data2}\n')

# 配列の要素にそれぞれ2を足す
data3 = data1 + 2
print(f'data1の要素に2を足し算：{data3}\n')

# 次元数と要素数の確認
print(f'次元数:{data3.ndim}')
print(f'要素数:{data3.size}\n')

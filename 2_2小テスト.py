import numpy as np

# 配列の作成
array1 = np.arange(1, 10, 1)
array2 = np.arange(11, 20, 1)
print(f'array1：{array1}')
print(f'array2：{array2}\n')

# ３×３行列に変換
array1_33 = array1.reshape(3, 3)
array2_33 = array2.reshape(3, 3)
print(f'array1を用いた3×3行列：\n{array1_33}')
print(f'array2を用いた3×3行列：\n{array2_33}\n')

# ２つの行列の積の計算
multi_matrix = np.dot(array1_33, array2_33)
print(f'array1とarray2の積：\n{multi_matrix}')

# ワーク：NumPyの操作方法①

# NumPyパッケージの読み込み
import numpy as np

# 配列の作成
np.array([0, 1])
sample_numpy_data = np.array([[9, 2, 4], [1, 2, 4], [3, 4, 5]])
print(f'配列の作成：\n{sample_numpy_data}\n')


# 次元数と要素数の確認
print(f'次元数:{sample_numpy_data.ndim}')
print(f'要素数:{sample_numpy_data.size}\n')


# 四則演算と定数倍
# 掛け算
print(f'掛け算: {np.array([1,2,3]) * np.array([9,8,7])}')

# 割り算
print(f'割り算:{np.array([9,8,7]) / np.array([3,2,1])}\n')

# 配列の定数倍
print(f'定数倍:{np.array([1,2,3]) * 2}')

# 配列の累乗
print(f'累乗:{np.array([1,2,3]) ** 3}\n')


# 0の初期化データ
# (5,10)は5行10列の行列データを作成
# dtypeを指定しない場合はfloat型で作成される
zero_data = np.zeros((5, 10))

print(f'0でfloat型：\n{zero_data}\n')

# dtypeを指定しint型の配列を作成
zero_data_int = np.zeros((2, 3), dtype=int)

print(f'0でint型：\n{zero_data_int}\n')


# データの並び替え
sample_numpy_data2 = np.array([0, 6, 3, 1, 5])
print(f'sample_numpy_data2：\n{sample_numpy_data2}\n')

sample_numpy_data2.sort()

print(f'昇順に並べ替え：\n{sample_numpy_data2}\n')

# スライスとは、配列の要素に部分的にアクセスする機能
# 配列を含む変数[始点: 終点: 増分]
print(f'要素を1つ飛ばしで取得：\n{sample_numpy_data2[0:4:2]}\n')

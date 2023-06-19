# ワーク：1.2.SVMを利用した空の写真の天気判定②

# 使用するモジュールの読み込み
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import cv2

from sklearn import svm, metrics
from sklearn.model_selection import train_test_split

# 定数定義
directory ='./tenants/data/'
tsv_file_name = 'svm.tsv'

# 特徴量のTSVファイルの読み込み
table = np.loadtxt(directory + tsv_file_name)
print(f'画像の特徴量データ：{table.shape}\n')

#tableの中身を10行出力
print (f'画像の特徴量先頭10行：\n{table[:10]}\n')

# 説明変数の設定
X = table[:, 2:4]
print (f'説明変数(G,B)先頭10行：\n{X[:10]}\n')

# 目的変数を設定し、データ型をintに変換する　(1:  晴れ, 2: 曇り)
Y = table[:, 0]
print(f'変換前：{Y.dtype}')
Y = Y.astype(np.int8)
print(f'変換後：{Y.dtype}\n')

# 学習データとテストデータに分割
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, random_state = 0, test_size=0.1)

print(f'学習データ数：{Y_train.size}')
print(f'テストデータ数：{Y_test.size}\n')

# SVMの作成・学習
clf = svm.SVC(gamma='scale')
clf.fit(X_train, Y_train)

# テストデータの予測値と実測値を表示
predict = clf.predict(X_test)
print(f'予測値　：{predict}')
print(f'テスト値：{Y_test}\n')

# 正解率の確認
acc_score = metrics.accuracy_score(Y_test, predict)
print(f'正解率:{acc_score}\n')

# モデルの可視化
# データのプロット
X_scatter1 = table[table[:,0]==1,2:4]
X_scatter2 = table[table[:,0]==2,2:4]

plt.scatter(X_scatter1[:, 0], X_scatter1[:, 1], c='blue', zorder=10,label='sunny')
plt.scatter(X_scatter2[:, 0], X_scatter2[:, 1], c='red', zorder=10,label='cloudy')

# 表示設定
plt.legend(loc="lower right", fontsize=10)
plt.xlabel("G")
plt.ylabel("B")
plt.axis('tight')

plt.show()

#X, Y軸の格子点を作成
X_min = X[:, 0].min() - 1
X_max = X[:, 0].max() + 1
Y_min = X[:, 1].min() - 1
Y_max = X[:, 1].max() + 1

XX, YY = np.mgrid[X_min:X_max:200j, Y_min:Y_max:200j]

# 格子点に対して予測
Z = clf.predict(np.c_[XX.ravel(), YY.ravel()])
print(f'変換前：{Z.shape}')
Z = Z.reshape(XX.shape)
print(f'変換後：{Z.shape}')
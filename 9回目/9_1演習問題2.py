# 解説：1.2.SVMを利用した空の写真の天気判定②
"""
【問題】
空欄を埋める形で、SVMのモデルをロジスティック回帰に変更してプログラムを作成してください。
本演習問題では、以下の部分のコードを修正します。
・目的変数を設定する部分を埋める
・予測値、テスト値、正解率を求めるpred_result関数で、引数を指定する部分と正解率を算出する部分を埋める
・ロジスティック回帰モデルを作成する部分を埋める
・モデルを可視化するview_model関数を呼び出す
"""

# 使用するモジュールの読み込み
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import cv2

from sklearn import svm, metrics
from sklearn.model_selection import train_test_split

from sklearn.linear_model import LogisticRegression

# 定数定義
directory ='./tenants/data/'
tsv_file_name = 'svm.tsv'

# 特徴量のTSVファイルの読み込み
table = np.loadtxt(directory + tsv_file_name)

# 説明変数の設定
X = table[:, 2:4]

# 目的変数を設定し、データ型をintに変換する　(1:  晴れ, 2: 曇り)
Y = table[:, 0]
Y = Y.astype(np.int8)

# 学習データと検証用データに分割
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, random_state = 0, test_size=0.1)

print(f'学習データ数：{Y_train.size}')
print(f'テストデータ数：{Y_test.size}\n')

def pred_result(predict,Y_test):
    print(f'予測値　：{predict}')
    print(f'テスト値：{Y_test}\n')
    # 正解率の確認
    acc_score = metrics.accuracy_score(Y_test, predict)
    print(f'正解率:{acc_score}\n')

def data_plot(table):
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

def view_model(X,model):
    # 下限と上限の設定
    X_min = X[:, 0].min() - 1
    X_max = X[:, 0].max() + 1
    Y_min = X[:, 1].min() - 1
    Y_max = X[:, 1].max() + 1

    XX, YY = np.mgrid[X_min:X_max:200j, Y_min:Y_max:200j]

    # 格子点に対して予測
    Z = model.predict(np.c_[XX.ravel(), YY.ravel()])
    Z = Z.reshape(XX.shape)

    # ロジスティック回帰の可視化
    plt.pcolormesh(XX, YY, Z, cmap=plt.cm.coolwarm,shading='auto')
    plt.contourf(XX, YY, Z, cmap=plt.cm.coolwarm, alpha=0.8)

    plt.show()
    plt.clf()

# ロジスティック回帰の作成・学習
model = LogisticRegression()

# モデルの学習
model.fit(X_train, Y_train)

# 予測の実施
predict = model.predict(X_test)

# 予測結果の確認
pred_result(predict,Y_test)

# データのプロット
data_plot(table)

# モデルの可視化
view_model(X,model)
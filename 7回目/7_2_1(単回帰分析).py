#＃ ワーク：2.2.線形回帰のPythonによる実装(単回帰分析)
#
# UCバークレー大学が機械学習の習得用に公開しているデータ
# 「Wine Quality Data Set」：https://archive.ics.uci.edu/ml/datasets/wine+quality

# ライブラリの読み込み
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn.model_selection import train_test_split

# CSV形式のファイル読み込み
wine = pd.read_csv("winequality-red.csv", sep=";")
print(f'赤ワインデータセット：\n{wine.head(10)}\n')
print('データのカラム名とデータ型')
print(f'{wine.info()}\n')


# 目的変数と説明変数の設定
simple_Y = wine['alcohol'].values   # 目的変数にalcohol(アルコール度数)を指定
simple_X = wine.loc[:, ['density']].values   # 説明変数にdensity(濃度)を指定
print(f'目的変数：\n{simple_Y}\n')
print(f'説明変数：\n{simple_X}\n')

# 学習データとテストデータに分割
simple_X_train, simple_X_test, simple_Y_train, simple_Y_test = train_test_split(simple_X, simple_Y, random_state=0)

print(f'学習データ数：{simple_Y_train.size}')
print(f'テストデータ数：{simple_Y_test.size}\n')

# 単回帰モデルの作成
simple_clf = linear_model.LinearRegression()

# モデルの学習
simple_clf.fit(simple_X_train, simple_Y_train)

# 回帰係数と切片の確認
print(f'回帰係数：{simple_clf.coef_}')
print(f'切片：{simple_clf.intercept_}\n')

print(f'単回帰式：\nalcohol = density × {simple_clf.coef_} + {simple_clf.intercept_}\n ')

# 決定係数の確認
train_R2 = simple_clf.score(simple_X_train, simple_Y_train)
print(f'学習データの決定係数：{train_R2}')

test_R2 = simple_clf.score(simple_X_test, simple_Y_test)
print(f'テストデータの決定係数：{test_R2}')

# 単回帰分析結果の可視化
plt.scatter(simple_X_train, simple_Y_train)   # 説明変数と目的変数を散布図で可視化
plt.plot(simple_X_train, simple_clf.predict(simple_X_train), color='r')   # 回帰直線を可視化
plt.show()
plt.clf()
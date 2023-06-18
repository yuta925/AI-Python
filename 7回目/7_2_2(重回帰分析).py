## ワーク：2.3.線形回帰のPythonによる実装(重回帰分析)
#
# UCバークレー大学が機械学習の習得用に公開しているデータ
# 「Wine Quality Data Set」：https://archive.ics.uci.edu/ml/datasets/wine+quality

# ライブラリの読み込み
import pandas as pd
import numpy as np
from sklearn import linear_model
from sklearn.model_selection import train_test_split

# CSV形式のファイル読み込み
wine = pd.read_csv("./tenants/data/winequality-red.csv", sep=";")
print(f'赤ワインデータセット：\n{wine.head(10)}\n')
print(f'特徴量確認：\n{wine.columns}\n')

# 説明変数と目的変数の設定
wine_explanatory_variables1 = wine[['fixed acidity', 'volatile acidity', 'citric acid', 'residual sugar']]
print(f'wine_explanatory_variables1の型：{type(wine_explanatory_variables1)}')
multiple1_X = wine_explanatory_variables1.values
print(f'multiple1_Xの型：{type(wine_explanatory_variables1.values)}\n')

multiple1_Y = wine['quality'].values

# 学習データとテストデータに分割
multiple1_X_train, multiple1_X_test, multiple1_Y_train, multiple1_Y_test = train_test_split(multiple1_X, multiple1_Y, random_state=0, test_size=0.25)

print(f'学習データ数：{multiple1_Y_train.size}')
print(f'テストデータ数：{multiple1_Y_test.size}\n')

# 重回帰モデルの作成
multiple1_clf = linear_model.LinearRegression()

# モデルの学習
multiple1_clf.fit(multiple1_X_train, multiple1_Y_train)

# 回帰係数と誤差の確認
coef = pd.DataFrame({'Name':wine_explanatory_variables1.columns,
                    'Coefficients':multiple1_clf.coef_})
print(f'回帰係数：\n{coef}\n')

intercept = multiple1_clf.intercept_
print(f'切片：{intercept}\n')

formula = f'quality\n='
for i in range(len(coef)):
    formula = f'{formula} {coef.Name[i]} × {(round(coef.Coefficients[i],5))}\n+'
formula = f'{formula} {round(intercept,5)}'
print(f'重回帰式：\n{formula}\n')

# 決定係数の確認
train_R2 = multiple1_clf.score(multiple1_X_train, multiple1_Y_train)
print(f'学習データの決定係数：{train_R2}')

test_R2 = multiple1_clf.score(multiple1_X_test, multiple1_Y_test)
print(f'テストデータの決定係数：{test_R2}')
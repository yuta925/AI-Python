#ワーク：1.2.ロジスティック回帰のPythonによる実装①

# UCバークレー大学が機械学習の習得用に公開しているデータ
#「Adult Data Set」：https://archive.ics.uci.edu/ml/datasets/adult

# ライブラリの読み込み
import pandas as pd
import numpy as np
from sklearn import linear_model
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# CSV形式のファイル読み込み
adult = pd.read_csv('adult.csv')
print(f'成人の国勢調査データセット：\n{adult.head(10)}\n')
print(f'カラム名確認：\n{adult.columns}\n')

# フラグの追加
adult["fin_flg"] = adult["flg-50K"].map(lambda x: 1 if x ==' >50K' else 0)
print(f'成人の国勢調査データセット：\n{adult.head(10)}\n')

print(f'{adult.groupby("flg-50K").size()}\n')
print(f'{adult.groupby("fin_flg").size()}\n')

# 説明変数と目的変数の設定
X = adult[['age', 'education-num', 'capital-gain', 'capital-loss', 'hours-per-week']]
Y = adult['fin_flg']

# 学習データとテストデータの分割
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, random_state=0, test_size=0.2)

print(f'学習データ数：{Y_train.size}')
print(f'テストデータ数：{Y_test.size}\n')

# モデルの作成
clf = linear_model.LogisticRegression(solver='liblinear')

# モデルの学習
clf.fit(X_train, Y_train)

#予測精度の確認
pred_test = clf.predict(X_test)
np.set_printoptions(edgeitems=15)
print(f'予測値　：{pred_test}')
print(f'テスト値：{Y_test.values}\n')

acc_score = accuracy_score(Y_test, pred_test)
print(f'正解率:{acc_score}')

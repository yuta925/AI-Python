 # 解説：1.2.ロジスティック回帰のPythonによる実装①
"""
【問題】
空欄を埋める形で、以下2つの説明変数を追加し、正解率を算出してください。
また、正解率に変化があることを確認してください。
・hours-per-week_age_ratio：年齢に対する労働時間(hours-per-week / age)
・education-num_age_diff：年齢と最終学歴の数値の差分(age - education-num)
"""
 ############# ワークと同様のコード################
 # ライブラリの読み込み
import pandas as pd
import numpy as np
from sklearn import linear_model
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

 # CSV形式のファイル読み込み
adult = pd.read_csv('./tenants/data/adult.csv')

 # フラグの追加
adult["fin_flg"] = adult["flg-50K"].map(lambda x: 1 if x ==' >50K' else 0)

 # 説明変数と目的変数の設定
X = adult[['age', 'education-num', 'capital-gain', 'capital-loss', 'hours-per-week']]
Y = adult['fin_flg']
print(f'追加前の説明変数：\n{X.columns}\n')

 # 学習データと検証用データの分割
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, random_state=0, test_size=0.2)

 # モデルの作成
clf1 = linear_model.LogisticRegression(solver='liblinear')

 # モデルの学習
clf1.fit(X_train, Y_train)

 #予測精度の確認
pred_test1 = clf1.predict(X_test)
acc_score1 = accuracy_score(Y_test, pred_test1)
print(f'追加前の正解率:{acc_score1}\n')
 #################################################

 #説明変数の追加
 #年齢に対する労働時間(hours-per-week/age)を作成
X_train['hours-per-week_age_ratio'] = X_train['hours-per-week']/X_train['age']
X_test['hours-per-week_age_ratio'] = X_test['hours-per-week']/X_test['age']

 #年齢と最終学歴の数値の差分(age - education-num)を作成
X_train['education-num_age_diff'] = X_train['age'] - X_train['education-num']
X_test['education-num_age_diff'] = X_test['age'] - X_test['education-num']

print(f'追加後の説明変数：\n{X_train.columns}\n')

 # ロジスティック回帰モデルの作成(引数のsolverはliblinearを使用)
clf2 = linear_model.LogisticRegression(solver='liblinear')

 # モデルの学習
clf2.fit(X_train, Y_train)

 #予測精度の確認
pred_test2 = clf2.predict(X_test)
acc_score2 = accuracy_score(pred_test2, Y_test)
print(f'追加後の正解率:{acc_score2}')
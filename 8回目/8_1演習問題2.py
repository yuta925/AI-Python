#解説：1.2.ロジスティック回帰のPythonによる実装②
#
# UCバークレー大学が機械学習の習得用に公開しているデータ
#「Adult Data Set」：https://archive.ics.uci.edu/ml/datasets/adult

"""
【問題】
空欄を埋める形で、ロジスティック回帰のプログラムが動くように、コードを修正してください。
本演習問題では、以下の部分のコードを修正します。
・relationship(夫/父/子持ちなどの情報)データをダミー変数へ変換して、説明変数に追加する
・標準化を行う部分のコードをstd_scaleとして関数化する
・学習データとテストデータそれぞれの正解率をout_acc関数を用いて出力する
"""

# ライブラリの読み込み
import pandas as pd
import numpy as np
from sklearn import linear_model
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, precision_score, recall_score,f1_score

def ready ():
    adult = pd.read_csv('./tenants/data/adult.csv')
    adult["fin_flg"] = adult["flg-50K"].map(lambda x: 1 if x ==' >50K' else 0)

    # relationship(夫/父/子持ちなどの情報)データをダミー変数へ変換
    X_dummy = pd.get_dummies(adult['relationship'])

    X = adult[['age','education-num', 'capital-gain', 'capital-loss', 'hours-per-week']]
    X = pd.concat([X,X_dummy],axis=1)

    X_dummy_column_num = X_dummy.columns.size
    X_column_num = X.columns.size
    print(f'X_dummy_column_num：{X_dummy_column_num}\n')
    print(f'X_column_num：{X_column_num}\n')

    Y = adult['fin_flg']

    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, random_state=0, test_size=0.2)

    return X_train, X_test, Y_train, Y_test

def make_model (X, Y):
    clf = linear_model.LogisticRegression(solver='liblinear')
    clf.fit(X, Y)
    return clf

def out_acc (X, Y,clf):
    pred_test = clf.predict(X)
    acc_score = accuracy_score(Y,pred_test)
    return acc_score

def std_scale(X_train,X_test):
    sc = StandardScaler()
    sc.fit(X_train)

    X_train_std = sc.transform(X_train)
    X_test_std = sc.transform(X_test)

    check_df = pd.DataFrame({'平均値':np.round(X_train_std.mean(axis=0),5),
                            '標準偏差':X_train_std.std(axis=0)},
                            index=X_train.columns)
    print(f'平均値と標準偏差の確認：\n{check_df}\n')
    return X_train_std,X_test_std

#データの準備
X_train, X_test, Y_train, Y_test = ready()

#標準化
X_train_std,X_test_std =  std_scale(X_train,X_test)

#モデルの作成・学習
clf_std = make_model(X_train_std, Y_train)

#予測精度の確認
train_acc = out_acc(X_train_std, Y_train,clf_std)
print(f'学習データの正解率:{train_acc}\n')

test_acc = out_acc(X_test_std, Y_test,clf_std)
print(f'テストデータの正解率:{test_acc}\n')

# 混同行列の確認
pred_test_std = clf_std.predict(X_test_std)
cm = confusion_matrix(Y_test, pred_test_std)
print(f'混同行列:\n{cm}\n')

# その他評価指標の確認
precision = precision_score(Y_test,pred_test_std)
recall = recall_score(Y_test,pred_test_std)
f1 = f1_score(Y_test,pred_test_std)
print(f'precision(適合率)：{precision}')
print(f'recall(再現率)：{recall}')
print(f'f1(F値)：{f1}')
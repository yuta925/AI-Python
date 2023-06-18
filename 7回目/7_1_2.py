#ワーク：1.2.ロジスティック回帰のPythonによる実装②

# UCバークレー大学が機械学習の習得用に公開しているデータ
#「Adult Data Set」：https://archive.ics.uci.edu/ml/datasets/adult

# ライブラリの読み込み
import pandas as pd
import numpy as np
from sklearn import linear_model
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

def ready ():
    adult = pd.read_csv('./tenants/data/adult.csv')
    adult["fin_flg"] = adult["flg-50K"].map(lambda x: 1 if x ==' >50K' else 0)

    # Occupation(職業)データの確認
    print(f'職業：\n{adult["occupation"]}\n')

    # ダミー変数への変換
    X_dummy = pd.get_dummies(adult['occupation'])
    print(f'X_dummy：\n{X_dummy}\n')

    X = adult[['age','education-num', 'capital-gain', 'capital-loss', 'hours-per-week']]
    X = pd.concat([X,X_dummy],axis=1)
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

#データの準備
X_train, X_test, Y_train, Y_test = ready()
print(f'説明変数の確認：\n{X_train}\n')

# 標準化のためのライブラリ
from sklearn.preprocessing import StandardScaler

# 標準化を実施
sc = StandardScaler()
sc.fit(X_train)

# 学習データとテストデータそれぞれの説明変数に対して標準化
X_train_std = sc.transform(X_train)
X_test_std = sc.transform(X_test)
print(f'標準化した学習データの説明変数：\n{np.round(X_train_std,5)}\n')

check_df = pd.DataFrame({'平均値':np.round(X_train_std.mean(axis=0),5),
                        '標準偏差':X_train_std.std(axis=0)},
                        index=X_train.columns)
print(f'平均値と標準偏差の確認：\n{check_df}\n')


# 標準化を実施したデータでモデルの作成・学習
clf_std = make_model(X_train_std, Y_train)

#予測精度の確認
acc = out_acc(X_test_std, Y_test,clf_std)
print(f'正解率:{acc}\n')

# ライブラリの読み込み
from sklearn.metrics import confusion_matrix, precision_score, recall_score,f1_score

# 混同行列の確認
pred_test_std = clf_std.predict(X_test_std)
cm = confusion_matrix(Y_test, pred_test_std)
print(f'混同行列:\n{cm}\n')
tn, fp, fn, tp = cm.flatten()
print(f'5万ドル以上と予測して正解だった数(tp)：{tp}')
print(f'5万ドル未満と予測して不正解だった数(fn)：{fn}')
print(f'5万ドル以上と予測して不正解だった数(fp)：{fp}')
print(f'5万ドル未満と予測して正解だった数(tn)：{tn}\n')

# その他評価指標の確認
precision = precision_score(Y_test,pred_test_std)
recall = recall_score(Y_test,pred_test_std)
f1 = f1_score(Y_test,pred_test_std)
print(f'precision(適合率)：{precision}')
print(f'recall(再現率)：{recall}')
print(f'f1(F値)：{f1}')
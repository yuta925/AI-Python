import pandas as pd
import numpy as np
from sklearn import linear_model
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score,f1_score

def ready ():
    adult = pd.read_csv('./tenants/data/adult.csv')
    adult["fin_flg"] = adult["flg-50K"].map(lambda x: 1 if x ==' >50K' else 0)
    X_dummy = pd.get_dummies(adult['relationship'])
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
    
def std_scale(X_train,X_test):
    sc = StandardScaler()
    sc.fit(X_train)
    X_train_std = sc.transform(X_train)
    X_test_std = sc.transform(X_test)
    return X_train_std,X_test_std
    
#データの準備
X_train, X_test, Y_train, Y_test = ready()

#標準化
X_train_std,X_test_std =  std_scale(X_train,X_test)

#モデルの作成・学習
clf_std = make_model(X_train_std, Y_train)

#予測精度の確認
test_acc = out_acc(X_test_std, Y_test,clf_std)
print(f'テストデータの正解率:{round(test_acc,5)}\n')

# f値の算出
pred_test_std = clf_std.predict(X_test_std)
f1 = f1_score(Y_test,pred_test_std)
print(f'f1(F値)：{round(f1,5)}')
import numpy as np
from sklearn import svm, metrics
from sklearn.model_selection import train_test_split

table = np.loadtxt('./tenants/data/svm.tsv')

# 説明変数と目的変数の設定
X = table[:, 1:4]
Y = table[:, 0]
Y = Y.astype(np.int8)

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, random_state = 2, test_size=0.1)

def pred_result(predict,Y_test):
    acc_score = metrics.accuracy_score(Y_test, predict)
    print(f'正解率:{round(acc_score,5)}') 

# SVMの作成
model = svm.SVC(gamma='scale')

# モデルの学習
model.fit(X_train, Y_train)

# 予測の実施
predict = model.predict(X_test)

# 予測結果の確認
pred_result(predict,Y_test)
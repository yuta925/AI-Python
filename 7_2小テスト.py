import pandas as pd
import numpy as np
from sklearn import linear_model
from sklearn.model_selection import train_test_split

# CSV形式のファイル読み込み
wine = pd.read_csv("./tenants/data/winequality-red.csv", sep=";") 

# 重回帰式
def multiple_formula(wine_explanatory_variables1, multiple1_clf):
    coef = pd.DataFrame({'Name':wine_explanatory_variables1.columns, 
                        'Coefficients':multiple1_clf.coef_})
    intercept = multiple1_clf.intercept_
    formula = f'quality\n='
    for i in range(len(coef)):
        formula = f'{formula} {coef.Name[i]} × {(round(coef.Coefficients[i],5))}\n+'
    formula = f'{formula} {round(intercept,5)}'
    print(f'重回帰式：\n{formula}\n')
    return

# 説明変数と目的変数の設定
wine_explanatory_variables1 = wine[['fixed acidity', 'volatile acidity','alcohol']]
multiple1_X = wine_explanatory_variables1.values
multiple1_Y = wine['quality'].values

# 学習データとテストデータに分割
multiple1_X_train, multiple1_X_test, multiple1_Y_train, multiple1_Y_test = train_test_split(multiple1_X, multiple1_Y, random_state=0, test_size=0.20)

# 重回帰モデルの作成
multiple1_clf = linear_model.LinearRegression()

# モデルの学習
multiple1_clf.fit(multiple1_X_train, multiple1_Y_train)

# 重回帰式の表示
multiple_formula(wine_explanatory_variables1, multiple1_clf)

# 決定係数の確認
test_R2 = multiple1_clf.score(multiple1_X_test,multiple1_Y_test)
print(f'テストデータの決定係数：{round(test_R2,5)}')
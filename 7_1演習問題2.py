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
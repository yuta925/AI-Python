# 解説：2.1.Pandasの操作方法①

# 【問題】
# 以下の2つの演習を行い、プログラムの空欄を埋めて
# 完成させてください。
# 1. series1を作成し、コンソールに表示させる
# 2. 1で作ったSeriesの値とindexをコンソールに表示させる

import pandas as pd

#series1の作成
series1 = pd.Series(['Tokyo','Chiba','Akita','Toyama','Kagawa'],index=['A','B','C','D','E'])
print(f'series1：\n{series1}\n')

# series1の値の確認
seriesVal = series1.values
print(f'データの値:\n{seriesVal}\n')

# series1のindexの確認
seriesInd = series1.index
print(f'index：\n{seriesInd}\n')
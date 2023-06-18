# ワーク：2.1.Pandasの操作方法①

# pandasの読み込み
import pandas as pd

# SeriesとDataFrameの関数の読み込み
from pandas import Series, DataFrame

# Seriesの作成
series_data = pd.Series([10, 11, 12, 13, 14, 15])
print(f'series_data：\n{series_data}\n')

# seriesの要素の確認
print(f'２番目の要素：{series_data[1]}')
# Seriesの値の確認
print(f'データの値の確認：{series_data.values}')
# Seriesのインデックスの確認
print(f'インデックスの確認：{series_data.index}\n')

# Seriesのインデックスの定義
series_index_data1 = pd.Series([0, 1, 2, 3, 4, 5], index=[
                               'a', 'b', 'c', 'd', 'e', 'g'])
print(f'series_index_data1：\n{series_index_data1}\n')

series_index_data2 = series_index_data1.reset_index(drop=True)
print(f'series_index_data2：\n{series_index_data2}\n')

series_index_data3 = series_index_data1.reset_index()
print(f'series_index_data3：\n{series_index_data3}\n')

# ワーク：3.2.テキストデータの読み込み

# pandasの読み込み
import pandas as pd

# テキストデータを読み込み、DataFrameに変換
df1 = pd.read_csv('sample_text.csv', header=None)
# 絶対パスで開くファイルを指定

print(f'df1：\n{df1}')

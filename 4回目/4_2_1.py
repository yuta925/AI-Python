# ワーク：2.1.ピポットテーブルの作成

# pandasの読み込み
import pandas as pd

# データをcsvからDataFrameに読み込み
df = pd.read_csv('pivotdata.csv')
print(f'df：\n{df}\n')

# ピボットで、行→列→値に定義
df_piv = df.pivot("date", "variable", "value")
print(f'dfピボット：\n{df_piv}\n')

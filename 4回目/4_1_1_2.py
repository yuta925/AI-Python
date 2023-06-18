# ワーク：1.1.Groupbyメソッドを用いたデータの結合

# Pandasの読み込み
import pandas as pd

# 男女/年齢/居住都市のテストデータを作成
df1 = pd.DataFrame({"SEX": ["M", "M", "F", "M", "F", "F", "M"],
                    "AGE": [20, 18, 23, 28, 32, 15, 41],
                    "CITY": ["OSAKA", "FUKUOKA", "OSAKA", "TOKYO", "OSAKA", "FUKUOKA", "KYOTO"]})
print(f'df1：\n{df1}\n')

# 性別でグループ化し、年齢の平均を求める
df2 = df1.groupby('SEX').mean()
print(f'df2：\n{df2}\n')

# 要素を複数指定して、グループ化を階層化
df3 = df1.groupby(["SEX", "CITY"]).mean()
print(f'df3：\n{df3}\n')

# 演習問題：2.2.Pythonによるピボットテーブルの作成とクロス集計処理

# 【問題】
# DataFrame1を作成する
# 行に性別、列に出身地、値に趣味にかける金額が入る
# ピボットテーブルを作成する
# 趣味を性別、出身地別でクロス集計する

import pandas as pd

# DataFrameに使用するデータを作成
data1 = {"性別": ['女性', '女性', '男性', '女性', '男性', '男性', '女性'],
         "出身地": ['Tokyo', 'Chiba', 'Chiba', 'Kanagawa', 'Saitama', 'Tokyo', 'Saitama'],
         "趣味にかける金額": [10000, 12000, 4000, 8000, 9000, 12000, 5000],
         "趣味": ['ゲーム', 'ゲーム', 'ヨガ', 'ゲーム', 'ヨガ', 'ヨガ', 'ヨガ']}


# DataFrame1を作成
df1 = pd.DataFrame(data1, index=["A", "B", "C", "D", "E", "F", "G"])
print(f'df1：\n{df1}\n')


# ピボットテーブルを作成
df1_piv = df1.pivot("性別", "出身地", "趣味にかける金額")
print(f'ピボットテーブル：\n{df1_piv}\n')

# クロス集計処理
df2 = pd.crosstab(index=df1["性別"], columns=df1["出身地"])
print(f'クロス集計：\n{df2}\n')

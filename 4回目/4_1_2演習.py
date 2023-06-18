# 演習問題：1.2.データの結合と連結

# 【問題】
# DataFrame1、DataFrame2を作成する
# DataFrame1,2を内部結合したDataFrame3を作成する
# DataFrame1,2を連結し、indexを新たに0から振り直した
# DataFrame4を作成する

import pandas as pd

# DataFrame1,2を作成
df1 = pd.DataFrame({'名前': ['A', 'B', 'C', 'D'],
                    '身長': [160, 150, 170, 165],
                    '性別': ['男性', '女性', '男性', '女性']})
df2 = pd.DataFrame({'名前': ['A', 'B', 'D', 'E'],
                    '体重': [50, 45, 55, 60]})

# DataFrameを内部結合
df3 = pd.merge(df1, df2)
print(f'内部結合：\n{df3}\n')

# 2つのDataFrameを連結
df4 = pd.concat([df1, df2], ignore_index=True)
print(f'連結：\n{df4}\n')

# 演習問題：2.3.重複データの処理

# 【問題】
# Dataframe1の重複データを確認する
# Dataframe1の重複データを削除する

import pandas as pd

# 重複したデータを含むDataFrameを作成
df1 = pd.DataFrame({'科目': ['英語', '英語', '算数', '算数', '英語'],
                    '点数': [90, 85, 75, 80, 90]})
print(f'df1:\n{df1}\n')

# 重複データの確認
df2 = df1.duplicated()
print(f'重複確認：\n{df2}\n')

# df1の重複データを削除
df3 = df1.drop_duplicates(["科目", "点数"])
print(f'重複削除：\n{df3}\n')

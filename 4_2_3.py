# ワーク：2.3.重複データの処理

# Pandasの読み込み
import pandas as pd

# 重複したデータを含むDataFrameを作成
df = pd.DataFrame({"key1": ["A", "A", "B", "B", "B"],
                   "key2": [2, 2, 2, 3, 3]})
print(f'df：\n{df}\n')

# 重複データの確認
print(f'重複確認：\n{df.duplicated()}\n')

# 作成したdfの重複データを削除
print(f'重複データ削除：\n{df.drop_duplicates(["key1","key2"])}\n')

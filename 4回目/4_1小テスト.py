import numpy as np
import pandas as pd

series = pd.Series(['1/1', '1/2', '1/3', '1/4', '1/5', '1/6','1/7',
                '1/8','1/9','1/10','1/11','1/12','1/13','1/14'],name='日付')
df1 = pd.DataFrame({'日付':['1/1', '1/2', '1/3', '1/4', '1/6','1/7'],
                    '天気':['晴れ', '曇り', '晴れ', '曇り', '晴れ','曇り']})
df2 = pd.DataFrame({'日付':['1/8', '1/14', '1/9', '1/12', '1/11'],
                    '天気':['雨', '晴れ', '晴れ', '雨', '晴れ']})

# 2つのDataFrameを縦方向に連結
merge_df1 = pd.concat([df1, df2],axis=0)
print(f'連結：\n{merge_df1}\n')

# seriesに対し、日付をkeyにしてmerge_df1を左外部結合
merge_df2 = pd.merge( series,merge_df1, on="日付", how="left")
print(f'日付をkeyに左外部結合：\n{merge_df2}\n')

# 天気でグループ化し、数を集計
count_df = merge_df2.groupby(["天気"]).count()
print(f'count_df：\n{count_df}\n')
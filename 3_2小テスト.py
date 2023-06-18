import pandas as pd
# DataFrameの作成
data = {'NAME': ['Makoto', 'Shinji', 'Naomi', 'Takashi', 'Homare'],
        'SEX': ['M', 'M', 'F', 'M', 'F'],
        'MONEY': [3000, 4400, 1500, 1300, 3700]}

df1 = pd.DataFrame(data)
print(f'df1：\n{df1}\n')

# index名をアルファベット(a,b,c,d,e)に変換
df2 = pd.DataFrame(data, index=['a', 'b', 'c', 'd', 'e'])
print(f'df2：\n{df2}\n')

# MONEY列が2000以上の行を抽出
df3 = df1[df1["MONEY"] >= 2000]
print(f'df3：\n{df3}\n')

# NAME列がShinjiとTakashiの行を抽出する
df4 = df1[df1["NAME"].isin(["Shinji", "Takashi"])]
print(f'df4：\n{df4}\n')

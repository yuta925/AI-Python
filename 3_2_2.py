# ワーク：2.2.Pandasの操作方法②

# pandasの読み込み
import pandas as pd

# 作成
# DataFrameの作成
df1 = pd.DataFrame([[100, 1990, 'Tokyo', 'Hiroshi'],
                    [101, 1989, 'Osaka', 'Masahiro'],
                    [102, 1992, 'Kyoto', 'Hideo']])
print(f'df1：\n{df1}\n')

# DataFrameの列名、indexの定義
df1.columns = ['ID', 'birth_year', 'city', 'name']
df1.index = ['a', 'b', 'c']
print(f'df1：\n{df1}\n')

# 辞書型データの作成
# 辞書型：{キーA:[値1,2,3], キーB:[値4,5,6]…}
dictdata = {'ID': [100, 101, 102],
            'birth_year': [1990, 1989, 1992],
            'city': ['Tokyo', 'Osaka', 'Kyoto'],
            'name': ['Hiroshi', 'Masahiro', 'Hideo']}
print(f'dictdata：\n{dictdata}\n')

# 辞書型データを使用したDataFrameの作成
df2 = pd.DataFrame(dictdata)
print(f'df2：\n{df2}\n')

# DataFrame（df1）を転置
df3 = df1.T
print(f'df3：\n{df3}\n')

# 列指定
# 生まれ年の1列を指定
print(f'1列指定：\n{df1.birth_year}\n')

# 名前と生まれ年の2列を指定
print(f'2列指定：\n{df1[["name","birth_year"]]}\n')


# データの削除
# 行の削除
print(f'1行削除：\n{df1.drop("a",axis=0)}\n')

# 列の削除（2列の場合）
print(f'2列削除：\n{df1.drop(["ID", "birth_year"], axis=1)}\n')


# データ抽出
# 条件でのデータ抽出
print(f'条件での抽出：\n{df1[df1["name"] == "Hiroshi"]}\n')

# 複数の値を許容するデータ抽出
print(f'複数条件での抽出：\n{df1[df1["city"].isin(["Tokyo","Osaka"])]}\n')


# 並べ替え
# 値は0,1,2、indexはC,A,BのSeriesを作成
series1 = pd.Series(range(3), index=['C', 'A', 'B'])
print(f'series1：\n{series1}\n')

# indexで並べ替え（昇順）
print(f'indexで並べ替え（昇順）：\n{series1.sort_index(ascending=True)}\n')

# 値で並べ替えも（降順）
print(f'値で並べ替え（降順）：\n{series1.sort_values(ascending=False)}\n')

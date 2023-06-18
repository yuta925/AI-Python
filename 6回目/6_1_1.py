# 演習問題：1.1.タイタニック号沈没事故のデータ解析(課題1)

# ## 事前準備

# 使用するモジュールの読み込み
import seaborn as sns

# タイタニック号沈没事故のデータの読み込み
titanic_df = sns.load_dataset('titanic')

# データのカラム名とデータ型の表示
print('データのカラム名とデータ型')
print(f'{titanic_df.info()}\n')

# ## 【課題1】データの概要
# 以下のデータを表示してください。
#  1. データの先頭10行
#  2. 生存者、男性、女性、子供の人数

# データの先頭10行の表示
titanic10 = titanic_df.head(10)
print(f'先頭10行：\n{titanic10}\n')

# 生存者、男性、女性、子供の人数

# 生存者の人数
surv_num = titanic_df['survived'].value_counts()
print(f'生存者人数：\n{surv_num}\n')

# 男性/女性の人数
sex_num = titanic_df['sex'].value_counts()
print(f'男性/女性の人数：\n{sex_num}\n')

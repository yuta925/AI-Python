# Excelデータの読み込み
import pandas as pd

excel_dir = './tenants/data/mondai1.xlsx'
df1 = pd.read_excel(excel_dir, header=0)
print(f'Excelデータ：\n{df1}\n')

# df1の価格で昇順に並び替えて表示
sort_df1 = df1.sort_values(by='Price')
print(f'df1の価格で昇順：\n{sort_df1}\n')

# csvデータの読み込み
csv_dir = './tenants/data/mondai1.csv'
df2 = pd.read_csv(csv_dir, header=None)
print(f'csvデータ：\n{df2}\n')

# df2の2行(Teaのデータ)削除
delete_df2 = df2.drop(2)
print(f'Teaの行削除：\n{delete_df2}\n')

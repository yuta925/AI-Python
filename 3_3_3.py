# ワーク：3.4.Excelデータの読み込み

# pandasの読み込み
import pandas as pd

# Excelデータの読み込み
df = pd.read_excel('sample_excel.xlsx', sheet_name='Sheet1')
print(f'Excelデータ：\n{df}\n')

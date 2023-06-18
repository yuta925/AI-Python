# ワーク：3.3.HTMLデータの読み込み

# pandasの読み込み
import pandas as pd

url = "https://www.data.jma.go.jp/gmd/risk/obsdl/top/help4.html#data_hyouki.html"
# 出典：気象庁ホームページ（https://www.data.jma.go.jp/gmd/risk/obsdl/top/help4.html#data_hyouki.html）

# HTMLから表を読み込み、DataFrameリストで取得
df_list = pd.read_html(url)
# リストの最初のアイテムを取り出す
df = df_list[0]
# 最初の5行を確認
print(f'HTMLの表データ：\n{df.head(5)}\n')


# HTMLから天気記号の対応表を読み込みリストで取得
df_list = pd.read_html(url, match="天気記号")

# 読み込まれ表データの数の確認
print(f'取得した表データ数:{len(df_list)}\n')

# リストの最初のアイテムを取り出す
df_first = df_list[0]
# 最初の3行だけ確認
print(f'天気記号を含む表：\n{df_first.head(3)}\n')

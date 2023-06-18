# 解説：1.3.タイタニック号沈没事故のデータ解析(課題3)

# ## 事前準備

# 警告文の非表示
import warnings
warnings.simplefilter('ignore')

# 使用するモジュールの読み込み
import matplotlib.pyplot as plt
import seaborn as sns

# タイタニック号沈没事故のデータの読み込み
titanic_df = sns.load_dataset('titanic')

# ## 課題3) 生存者の傾向解析

# 生存者の傾向を解析するために、以下を実施する。
# 1. データ項目間の相関関係を理解するためのヒートマップの作成(数値も表示)
# 2. 生存者のデータ項目を他のデータ項目の相関係数の可視化(降順に表示)
# 3. 船室の等級ごとの死亡/生存人数の棒グラフの作成



# 1. データ項目間の相関関係を理解するためのヒートマップの作成
# ヒートマップ作成用のDataFrameの作成
titanic_heatmap_df = titanic_df.copy()


# DataFrameのmap() 関数を利用し、以下の変換を実施する。
#   列「sex」のmaleを0, femaleを1
#   列「who」のmanを0, womanを1, childを2
#   列「embarked」のSを0, Cを1, Qを2
titanic_heatmap_df['sex'] = titanic_heatmap_df['sex'].map({'male': 0, 'female': 1})
titanic_heatmap_df['who'] = titanic_heatmap_df['who'].map({'man': 0, 'woman': 1, 'child': 2})
titanic_heatmap_df['embarked'] = titanic_heatmap_df['embarked'].map({'S': 0, 'C': 1, 'Q': 2})




# ヒートマップ作成用のDataFrameの先頭20行を表示する。
print(f'先頭20行\n{titanic_heatmap_df.head(20)}\n')

# 相関係数の計算
titanic_survived_corr = titanic_heatmap_df.corr()

# ヒートマップを描画する領域を8×8で指定
plt.figure(figsize=(8, 8))

# ヒートマップを作成(ヒートマップ化するデータとしてtitanic_survived_corrを使用)
sns.heatmap(titanic_survived_corr, annot=True)
plt.show()
plt.clf()


# 2. 生存者のデータ項目を他のデータ項目の相関係数の可視化（降順に表示）
# 相関係数の計算
titanic_survived_corr = titanic_heatmap_df.corr()['survived'].sort_values(ascending=False)

# 相関係数の計算結果の出力
print(f'相関係数：\n{titanic_survived_corr}\n')

# 「survived」に対する相関係数のグラフ化
titanic_survived_corr.plot.bar()
plt.show()
plt.clf()


# 男女/子供別の死亡/生存人数の棒グラフの作成
# Seabornのcountplot() 関数を使用
sns.countplot(x='who', data=titanic_df, hue='survived')
plt.show()
plt.clf()

# 3. 船室の等級ごとの死亡/生存人数の棒グラフの作成
sns.countplot(x='pclass', data=titanic_df, hue='survived')
plt.show()
plt.clf()
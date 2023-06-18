# 解説：1.2.タイタニック号沈没事故のデータ解析(課題2)

# ## 事前準備

# 警告文の非表示
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
warnings.simplefilter('ignore')

# 使用するモジュールの読み込み

# タイタニック号沈没事故のデータの読み込み
titanic_df = sns.load_dataset('titanic')

# Seabornで棒グラフを描画する方法
# barplot : 横軸と縦軸の値を設定してグラフを描画する
# sns.barplot(x='x軸', y ='y軸', data=グラフ化するデータの名称)
# countplot : データの要素を個数を数えて描画する
# sns.countplot(x='x軸', data=グラフ化するデータの名称)

# ## 課題2) データの可視化

# 以下のデータを可視化するためにグラフを作成しましょう。
# 1. 男性/女性の人数 (棒グラフ)の作成
# 2. 乗船した港ごとの人数 (棒グラフ)
# 3. 船室の等級ごとの人数 (棒グラフ)
# 4. 船室の等級ごとの男女別人数 (棒グラフ)
# 5. 船室の等級ごとの乗船した港別人数 (棒グラフ)
# 6. 年齢別の人数 (ヒストグラム)

# 1. 男性/女性の人数 (棒グラフ)
sns.countplot(x='sex', data=titanic_df)
plt.show()
plt.clf()

# 2. 乗船した港ごとの人数 (棒グラフ)
sns.countplot(x='embark_town', data=titanic_df)   # カラム名「embarked」を指定してもよい
plt.show()
plt.clf()

# 3. 船室の等級ごとの人数 (棒グラフ)
sns.countplot(x='pclass', data=titanic_df)   # カラム名「class」を指定してもよい
plt.show()
plt.clf()

# 4. 船室の等級ごとの男女別人数 (棒グラフ)
sns.countplot(x='pclass', data=titanic_df, hue='sex')
plt.show()
plt.clf()

# 5. 船室の等級ごとの乗船した港別人数 (棒グラフ)
sns.countplot(x='pclass', data=titanic_df, hue='embark_town')
plt.show()
plt.clf()

# 6. 年齢別の人数 (ヒストグラム)
sns.distplot(titanic_df['age'], kde=False, bins=30)
plt.show()
plt.clf()
# sns.distplot(titanic_df['age'].dropna(), bins=50)

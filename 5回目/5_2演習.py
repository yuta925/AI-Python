# 演習問題：2.2.Seabornの操作①(ヒストグラム・散布図の作成)

# 【問題】
# 客の支払金額(total_bill)の、階級の数を30とした
# ヒストグラムを作成する ※カーネル密度推定は非表示とする
# 客が店員に渡したチップ(tip)と、客の支払い金額(total_bill)の
# 相関を表す散布図を作成する　※来店時間(time)ごとに色を変える


# 警告文の非表示
from matplotlib import pyplot as plt
import seaborn as sns
import warnings
warnings.simplefilter('ignore')

# Seaborn、pyplotの読み込み

# tipsデータの読み込み
tips = sns.load_dataset('tips')

# データの確認
print(f'tipsの先頭10行：\n{tips[0:10]}\n')

# ヒストグラムの作成
sns.distplot(tips['total_bill'], kde=False, bins=30)
plt.show()
plt.clf()

# 散布図の作成
sns.scatterplot('total_bill', 'tip', data=tips, hue='time')
plt.show()
plt.clf()

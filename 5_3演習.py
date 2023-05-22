# 解説：3.3.Seabornの操作①(棒グラフ・折れ線グラフ・ヒートマップの作成)

# 【問題】
# 1月の乗客数(passengers)を、年(year)ごとに示した棒グラフを作成する
# 1月の乗客数(passengers)を、年(year)ごとに示した折れ線グラフを作成する
# x軸を月(month)、y軸を年(year)としたヒートマップを作成する

# 警告文の非表示
from matplotlib import pyplot as plt
import seaborn as sns
import warnings
warnings.simplefilter('ignore')

# Seaborn、pyplotの読み込み

# flightsデータの使用と確認
flights = sns.load_dataset('flights')

# 棒グラフの作成
sns.barplot(x='year', y='passengers', data=flights[flights.month == 'Jan'])
plt.show()
plt.clf()

# 折れ線グラフの作成
sns.lineplot(x='year', y='passengers', data=flights[flights.month == 'Jan'])
plt.show()
plt.clf()

# ヒートマップの作成
flights = flights.pivot('year', 'month', 'passengers')
sns.heatmap(flights)
plt.show()
plt.clf()

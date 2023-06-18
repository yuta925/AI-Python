from matplotlib import pyplot as plt
import seaborn as sns
import warnings
warnings.simplefilter('ignore')

flights = sns.load_dataset('flights')

# （元から#が付いているものは、採点を行う際にもコメントアウトしてください。）
# 棒グラフの作成
sns.barplot(x='month', y='passengers', data=flights[flights.year == 1953])
plt.show()
plt.clf()

# 棒グラフで最も乗客数が少ない月
min_passengers = 'Nov'
print(f'最も乗客数が少ない月：{min_passengers}\n')

# 折れ線グラフの作成
sns.lineplot(x='month', y='passengers', data=flights[flights.year == 1958])
plt.show()
plt.clf()

# 折線グラフで最も乗客数が多い月
max_passengers = 'Aug'
print(f'最も乗客数が多い月：{max_passengers}')

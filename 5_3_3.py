# ワーク：3.3.Seabornの操作②(ヒートマップの作成)

# 警告文の非表示
from matplotlib import pyplot as plt
import seaborn as sns
import warnings
warnings.simplefilter('ignore')

# Seaborn、pyplotの読み込み

# 年/月ごとの飛行機乗客数のデータを利用
flights = sns.load_dataset('flights')
print(f'flightsデータの確認：\n{flights}\n')

# Pivot形式に変換し、ヒートマップを生成
flights = flights.pivot('month', 'year', 'passengers')
print(f'飛行機乗客数データの確認：\n{flights}\n')

sns.heatmap(flights)
plt.show()
plt.clf()

# 数字を重ね合わせて表示
sns.heatmap(flights, annot=True, fmt='d')
plt.show()
plt.clf()

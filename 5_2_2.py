# ワーク：2.2.Seabornの操作①(散布図の作成)

# 警告文の非表示
from matplotlib import pyplot as plt
import seaborn as sns
import warnings
warnings.simplefilter('ignore')

# Seaborn、pyplotの読み込み

# アヤメの花のデータ読み込み
iris = sns.load_dataset('iris')

# 先頭の10行を表示する
# sepal_length：がく片の長さ, sepal_width：がく片の幅
# petal_length：花びらの長さ, petal_width：花びらの幅
# species：品種
print(f'irisの先頭10行：\n{iris[0:10]}\n')

# 散布図の生成
sns.scatterplot('sepal_width', 'petal_length', data=iris)
plt.show()
plt.clf()

# 品種ごとに色を変えることも可能
sns.scatterplot('sepal_width', 'petal_length', data=iris, hue='species')
plt.show()
plt.clf()

# 散布図とヒストグラムの同時表示
sns.jointplot('sepal_width', 'petal_length', data=iris)
plt.show()
plt.clf()

# 散布図行列の生成
sns.pairplot(iris, hue='species')
plt.show()
plt.clf()

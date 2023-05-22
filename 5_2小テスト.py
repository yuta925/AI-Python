from matplotlib import pyplot as plt
import seaborn as sns
import warnings
warnings.simplefilter('ignore')

# Seaborn、pyplotの読み込み

# tipsデータの読み込み
tips = sns.load_dataset('tips')

tips['tip_per_total'] = tips['tip'] / tips['total_bill']
tip_per_total_10 = tips['tip_per_total'].head(10)
print(f'tip_per_totalの先頭10行：\n{tip_per_total_10}\n')

# 散布図の作成
# （元から#が付いているものは、採点を行う際にもコメントアウトしてください。）
sns.scatterplot('total_bill', 'tip_per_total', data=tips, hue='time')
# plt.show()
# plt.clf()

# tip_per_totalが、一番高く外れている点(小数第1位)
outliers = 0.7
print(f'散布図で読み取れる一番高いtip_per_total：{outliers}')

import matplotlib.pyplot as plt
import numpy as np

# 円周率
pi = np.pi
print(f'円周率π：{pi}\n')

x = np.arange(-pi, pi, 0.1)
print(f'x = \n{x[:10]}\n')

# sin関数
y = np.sin(x)

# sin関数を表示
# 元から#が付いているものは、実行結果を確認し、
# 採点を行う際にコメントアウトしてください。

plt.plot(x, y)
plt.grid(True)
plt.show()
plt.close()

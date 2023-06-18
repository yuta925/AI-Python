# ワーク：2.6.Pythonによる関数の定義

# 関数
def hello_world():
    print('Hello World!\n')


def hello_with_name(name):
    print(f'Hello,{name}!\n')


data = 'hello'


def capital():
    print(data.upper())


print('hello_world関数の実行')
hello_world()

print('hello_with_name関数の実行')
hello_with_name('Taroh')

print('captal関数の実行')
capital()

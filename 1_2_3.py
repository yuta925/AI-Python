# ワーク：2.3.Pythonによる条件分岐

# if文
# if文
a = 1
b = 3

if a < b:
    print('if文が実行される：')
    print(f'{a}よりも{b}の方が大きい\n')
if a > b:
    print('if文が実行されない：')
    print(f'{a}の方が{b}よりも方が大きい\n')

 # if ~ else文
a = 1
b = 3
if a > b:
    print('a > bが成立')
else:
    print('a > bが不成立')

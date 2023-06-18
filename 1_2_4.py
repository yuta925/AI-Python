# ワーク：2.5.Pythonによる繰り返し構文

# for文
print('開始を指定しない場合：')
for i in range(3):
    print(i)

print('開始を指定した場合')
for i in range(1, 4):
    print(i)
print()


# while文
count = 1
end = 10

print(f'while文で"count"が"end"より大きくなるまで実行')
while count < end:
    print(f'{count}回目：{count} < {end}')
    count = count + 1

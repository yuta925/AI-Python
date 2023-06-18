def calculation(i):
    b = 2
    if i >= b:
        print(f'{i} >= {b}')
        output = i - b
    else:
        print(f'{i} < {b}')
        output = b - i
    return output


for i in range(1, 4):
    print(f'{i}回目')
    result = calculation(i)
    print(f'結果：{result}')

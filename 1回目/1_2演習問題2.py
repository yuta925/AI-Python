# 解説：2.6.Pythonの基本構文

# 【問題1】
# 今月1日0時から経過した時間を計算し、
# 表示させるプログラムの空欄を埋めてください。

# aに日、bに時刻(1時間単位)を入力
a = 5
b = 14
print(f'{a}日の{b}時\n')
time = (a-1) * 24 + b
print(f'今月1日0時から経過した時間：{time}\n')

# 【問題2】
# 月~金曜日まで表示させる関数を作成する
# プログラムの空欄を埋めてください。

weekdays = ['月', '火', '水', '木', '金']
print(f'weekdaysの中身：{weekdays}\n')  # weekdaysのデータを確認
week_type = type(weekdays)  # weekdaysのデータ型を確認
print(f'weekdaysの型：{week_type}\n')


def week():
    for day in weekdays:
        print(f'{day}曜日\n')


week()

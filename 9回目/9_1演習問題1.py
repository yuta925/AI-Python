# 解説：1.2.SVMを利用した空の写真の天気判定①

"""
【問題】
空欄を埋める形で、画像データの処理を実行してください。
本演習問題では、以下の部分のコードを修正します。
・画像データの要素数と実際の曇り画像を表示する部分をshow_img関数として定義する
・画像のRGBの平均値を求めるaverage_color関数で、それぞれの平均を求める部分を埋める
・get_rgb関数内で画像データを数値データに変換し、show_img関数とaverage_color関数を呼び出す
"""

# 使用するモジュールの読み込み
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import cv2

#データのディレクトリを定義
directory ='./tenants/data/'

def show_img(input_img):
    #画像データの要素数
    img_structure = input_img.shape
    print(f'画像データの要素数：{img_structure}\n')

    #BGR→RGBに変換して表示
    input_img = cv2.cvtColor(input_img, cv2.COLOR_BGR2RGB)
    plt.imshow(input_img)
    plt.show()
    plt.clf()

# 画像中のRGB (Red/Green/Blue) を求めるための関数
def average_color(src):

    average_bgr = [0,0,0]
    # RGBの平均値の算出
    for i in range(3):
        extract_img = src[:,:,i]
        average_bgr[i] = np.average(extract_img)

    rgb_value = [average_bgr[2], average_bgr[1], average_bgr[0]]

    return rgb_value

# 画像データから特徴量を抽出する関数
def get_rgb(file, label):
    #画像の読み込み
    input_img = cv2.imread(file)
    show_img(input_img)

    #RGBの平均値を取得する
    rgb_value = average_color(input_img)
    #label, R, G, Bの要素を\t区切り(tsv)で表す
    tsv_line = f'{label}\t{rgb_value[0]}\t{rgb_value[1]}\t{rgb_value[2]}\n'

    return tsv_line

# 曇り画像のサンプルデータ読み込み
file = f'{directory}/sample_cloud.jpg'

#サンプルデータのRGB取得
tsv_line = get_rgb(file, '002')
print(f'sample_cloud.jpgのラベルとRGB：\n{tsv_line}')
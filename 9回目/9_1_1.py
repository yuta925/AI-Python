# ワーク：1.2.SVMを利用した空の写真の天気判定①

# 使用するモジュールの読み込み
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import cv2

#データのディレクトリを定義
directory ='./tenants/data/'

# 晴れ画像のサンプルデータ読み込み
file = f'{directory}sample_bluesky.jpg'
img = cv2.imread(file)
print(f'画像データの要素数：{img.shape}\n')

# 画像データの表示
plt.imshow(img)
plt.show()
plt.clf()

#BGR→RGBに変換して表示
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(img)
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
    #RGBの平均値を取得する
    rgb_value = average_color(input_img)
    #label, R, G, Bの要素を\t区切り(tsv)で表す
    tsv_line = f'{label}\t{rgb_value[0]}\t{rgb_value[1]}\t{rgb_value[2]}\n'

    return tsv_line

#サンプルデータのRGB取得
tsv_line = get_rgb(file, '001')
print(f'sample_bluesky.jpgのラベルとRGB：\n{tsv_line}')
#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import glob
import numpy as np
import cv2
import matplotlib.pyplot as pyplot
import pickle

# 保存先や画像サイズの指定
out_dir=".png-etl1"#画像データのあるディレクトリ
im_size = 25 #画像サイズ
save_file = out_dir + "/katakana.pickle" #保存先
plt.figure(figsize=(9,17))#画像を大きく

# カタカナの画像が入っているディレクトリから画像を取得
kanadir = list(range177,220+1)
kanadir.append(166)#ヲ
kanadir.append(221)#ン
result=[]

for i,code in enumerate(kanadir):
	img_dir = out_dir + "/" + str(code)
	fs = glob.glob(img_dir + "/*")
	print("dir=",img_dir)

	# 画像を読み込んでグレースケールに変換しリサイズ
	for j,f in enumerate(fs):
		img = sv2.imread(f)
		img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
		img = sv2.resize(img_gray,(im_size,im_size))
		result.append([i,img])
		if j == 3:
			plt.subplot(11,5,i+1)
			plt.axis("off")
			plt.title(str(i))
			plt.imshow(img,cmap="gray")

# ラベルと画像のデータを保存*4
pickle.dump(result, open(save_file,"wd"))
plt.show()
print("ok")


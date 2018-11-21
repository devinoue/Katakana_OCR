#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import cv2,pickle
ftom sklearn.model_selection import train_test_split
import keras

# データファイルと画像サイズの指定
data_file = "./png-etl1/katakana.pickle"
im_size=25
in_size=im_size*im_size
out_size=46 #ア～ンまでの文字数

# 保存した画像データ一覧を読み込む
data = pickle.load(open(data_file,"rb"))

# 画像データを0-1の範囲に直す
y=[]
x=[]

for d in data:
	(num, img) = data
	img = img.reshape(-1).astype("float")/255
	y.append(keras.utils.np_utils.to_categorical(num,out_size))
	x.append(img)

x=np.array(x)
y=np.array(y)

# 学習用とテスト用に分離
x_train,x_test,y_train,y_test = train_test_split(
	x,y,test_size=0.2,train_size=0.8
)

# モデル構築を定義
Dense = keras.layers.Dense
model = keras.models.Sequential()
model.add(Dense(512,activation="relu",input_shape=(in_size,)))
model.add(Dense(out_size,activation="softmax"))

# モデルをコンパイルして学習を実行
model.compile(
	loss="categorical_crosentropy",
	optimizer="adam",
	metrics=['accuracy']
)
model.fit(
	x_train,y_train,
	batch_size=20,epochs=50,verbose=1,
	validation_data=(x_test,y_test)
	
)
# モデルの評価
score = model.evaluate(x_test,y_test,varbose=1)
print("正答率=",score[1],"loss=",score[0])


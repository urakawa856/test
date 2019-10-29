import numpy as np
import pandas as pd
import os

# dataのimport########################################################

import pickle

foldername = 't600sample'
filename1 = '{}.binaryfile'.format(foldername)


######################################################################
with open(filename1,'rb') as k:
	timedepend = pickle.load(k)
	vlas = pickle.load(k)
	resolutionT = pickle.load(k)
	resolutionX = pickle.load(k)
	distanceF = pickle.load(k)
	allFrame = pickle.load(k)

#RoIの設定##############################################################

RoI = []
x = [114,400] # RoIの横軸の範囲
y = [220,320] # RoIの縦軸の範囲

for i in range(allFrame):
	a = timedepend[i].iloc[y[0]:y[1],x[0]:x[1]]
	RoI.append(a)
print(RoI[0])

#deltaTauに整列する関数を使用###############################################
from visualizations import makeLambdaTau as mkLT

initialFrame = 0
fps = 30

lambdaTemp, scanframe, vlaspixel, pixel, scanframeMax = mkLT(vlas,distanceF,resolutionX,RoI,initialFrame,fps,allFrame)

print(len(lambdaTemp))
print(len(scanframe))
print(vlaspixel)
print(pixel)


# visualizationをおこなう#################################################
import matplotlib.pyplot as plt

from visualizations import visualization as vis

# 描画する温度範囲を設定##################################################
rangeT = [0.1,1]
movie, images = vis(scanframeMax, lambdaTemp, rangeT)
plt.show(movie)

movie.save('visualAnimation.gif')



# resultfileを作成しbinary形式で保存
filename2 = '{}_result.binaryfile'.format(foldername)
with open(filename2,'wb') as f:
	pickle.dump(images, f)


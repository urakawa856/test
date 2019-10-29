def visualization(allFrame, timedepend, rangeT):
	import matplotlib.pyplot as plt
	import matplotlib.animation as animation

	images = []
	fig = plt.figure()



	for i in range(allFrame): #range(a,b) = a=<x<bなので+1
		data = timedepend[i]
		#image = plt.imshow(data,interpolation='nearest',cmap = 'jet', vmin=rangeT[0], vmax=rangeT[1],animated=True)
		image = plt.pcolor(data,cmap = 'jet', vmin=rangeT[0], vmax=rangeT[1])


		#title = plt.text(0.5, 1.01, 'delta={:.2f}'.format(i*0.034),ha='center', va='bottom',transform=ax.transAxes, fontsize='large')

		#plt.tick_params(labelleft=False, labelright=False, left = False, right=False)
		#plt.title('time {} [s]'.format((i+1)*0.033))

		images.append([image])

	movie = animation.ArtistAnimation(fig,images,interval=50)
	plt.show()
	

	return images , movie



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
x = [255,400] # RoIの横軸の範囲
y = [220,320] # RoIの縦軸の範囲

for i in range(allFrame):
	a = timedepend[i].iloc[y[0]:y[1],x[0]:x[1]]
	RoI.append(a)
print(RoI[0])

#deltaTauに整列する関数を使用###############################################
from visualizations import makeLambdaTau as mkLT


# RoIに合わせてフレーム間隔を設定################################################
initialFrame = 800
allFrame = 1650 
fps = 30

lambdaTemp, scanframe, vlaspixel, pixel, scanframeMax = mkLT(vlas,distanceF,resolutionX,RoI,initialFrame,fps,allFrame)

print(lambdaTemp[30])

print(len(lambdaTemp))
print(len(scanframe))
print(vlaspixel)
print(pixel)
print(scanframeMax)

# 描画する温度範囲を設定##################################################
rangeT = [0.1,1]
import matplotlib.pyplot as plt

vis, mov = visualization(scanframeMax, lambdaTemp,rangeT)


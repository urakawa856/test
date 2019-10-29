def visualization(allFrame, timedepend, rangeT):
	import matplotlib.pyplot as plt
	import matplotlib.animation as animation

	images = []
	fig = plt.figure()


	for i in range(allFrame):
		data = timedepend[i]
		image = plt.imshow(data,interpolation='nearest',cmap = 'jet', vmin=rangeT[0], vmax=rangeT[1],animated=True)
		#plt.tick_params(labelleft=False, labelright=False, left = False, right=False)
		#plt.title('time {} [s]'.format((i+1)*0.033))

		images.append([image])

	movie = animation.ArtistAnimation(fig,images,interval=100)
	

	return movie, images 




# レーザー通過からの経過時間で整理した温度データを作成するユーザー定義関数を作成

def makeLambdaTau(vlas,distanceF,resolutionX,timedepend,initialFrame,fps,allFrame):
	import math
	import numpy as np
	import pandas as pd
	# vlasを1frameで移動するpixel数に変換
	vlasPixel = vlas / (fps*resolutionX*distanceF*10**-3)
	pixel = resolutionX*distanceF*10**-3 # 1pixelのサイズを算出

	# timedependにおける1frame目の列数を取得
	raw_pixel, col_pixel = timedepend[1].shape
	print(col_pixel)

	scanframe = []
	matrix = np.zeros([raw_pixel,col_pixel])
	ilambdaTemp = pd.DataFrame(matrix)
	lambdaTemp = []

	for l in range(allFrame):
		l=l+1
		lambdaTemp.append(ilambdaTemp)

	print(l)
	print(allFrame)
	print(lambdaTemp[0])
	print(timedepend[1])

	difTemp = []
	for i in range(len(timedepend)):
		temp = timedepend[i] - timedepend[0]
		difTemp.append(temp)



	#レーザーが通過したフレームをvlasPixelをもちいて算出し，レーザー通過フレームで整理したlambdaTempリストを作成
	for p in range(col_pixel):# 位置ピクセル
		a = math.ceil(p/vlasPixel) + initialFrame #各ピクセルでのレーザー通過時フレームの算出
		scanframe.append(a)


		for i in range(allFrame-scanframe[p]): #フレーム数，０から始めて，必要なステップ数を指定
			print(i)
			print(p)

			temp1 = lambdaTemp[i].values
			temp2 = difTemp[scanframe[p]+i].values #scanframe[p]+i で位置ピクセルpのレーザー通過フレームscanframe[p]から+iフレーム目の温度テーブルをnparray配列を取得
			print(scanframe[p])

			temp11 = temp1[:,p] # lambdaTempのiフレーム目の配列から，位置ピクセルpの要素（温度）を指定
			temp21 = temp2[:,p] # tdのscanframe[p]+iフレーム目の配列から，位置ピクセルpの要素（温度）を指定
			temp11 = temp21 #lambdaTempの1frame目のp列すべてにtimedependのp列すべてのピクセルのレーザー通過フレーム時の温度データを代入

			lambdaTemp[i].iloc[:,p] = temp11



	return lambdaTemp, scanframe, vlasPixel, pixel, allFrame-scanframe[p]

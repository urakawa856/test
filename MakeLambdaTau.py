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
	scanframe = []
	matrix = np.zeros([raw_pixel,col_pixel])
	ilambdaTemp = pd.DataFrame(matrix)
	lambdaTemp = []

	for l in range(allFrame):
		lambdaTemp.append(ilambdaTemp)



	#レーザーが通過したフレームをvlasPixelをもちいて算出し，レーザー通過フレームで整理したlambdaTempリストを作成
	for p in range(col_pixel):
		a = math.ceil(p/vlasPixel) + initialFrame #各ピクセルでのレーザー通過時フレームの算出
		scanframe.append(a)


		for i in range(allFrame-scanframe[p]): #０から始めて，必要なステップ数を指定
			lambdaTemp[i].iloc[:,p] =timedepend[scanframe[p]+i].iloc[:,p] #lambdaTempの1frame目のp列すべてにtimedependのp列すべてのピクセルのレーザー通過フレーム時の温度データを代入

	return lambdaTemp, scanframe, vlasPixel, pixel















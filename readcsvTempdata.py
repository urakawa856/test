# 実験結果および実験条件各種をバイナリファイルに保存する

import numpy as np
import pandas as pd
import os

# 参照するフォルダを指定（ここを変更する）
foldername = 't600sample'
rawTempfolder = './{}/'.format(foldername)






data=[]
# 0
timedepend=[]

# csvファイルの読み込み
rawTemp = os.listdir(rawTempfolder) 
allFrame = len(rawTemp)#　記録したデータの総フレーム数
for i in range(allFrame):
    infile = rawTempfolder + rawTemp[i]
    Temp = pd.read_csv(infile, header = None)
    
    a=[]
    a = Temp
    timedepend.append(a)
print(a)

print(len(timedepend))

print(timedepend[22])

# 実験条件の入力
vlas = 1 # laser velosity = 1.0 mm/s
resolutionT = 0.025 # Temperature resolution = 0.025 K
resolutionX = 0.68 # spatial resolution = 0.68 mrad
distanceF = 250 # focal distance = 250 mm
fps = 30 #

#pickleを用いたtimedependおよび各種実験条件の保存
import pickle

# バイナリファイルの名前を変更して各種変数を保存するファイルを作成
filename = '{}.binaryfile'.format(foldername)
with open(filename,'wb') as f:
	pickle.dump(timedepend,f)
	pickle.dump(vlas,f)
	pickle.dump(resolutionT,f)
	pickle.dump(resolutionX,f)
	pickle.dump(distanceF,f)
	pickle.dump(allFrame,f)


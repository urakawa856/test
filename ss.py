import matplotlib.pyplot as plt
import matplotlib.animation as animation

images = []
fig = plt.figure()

for i in range(allFrame):
	data = timedepend[i]
	image = plt.pcolor(data, cmap = 'jet')
	#plt.tick_params(labelleft='off', labelright='off', left = 'off', right='off')

	images.append([image])

movie = animation.ArtistAnimation(fig,images)
plt.show()
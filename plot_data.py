import numpy as np
import matplotlib.pyplot as plt
import glob

# get a list of files that match the pattern 'inflammation-*.csv'
filenames = glob.glob('inflammation-*.csv')
filenames = filenames[0:3]

# run it for each file
for filename in filenames:
	
	print filename

	# load the first data file
	data = np.loadtxt(fname=filename, delimiter=',')

	# create a matplotlib figure with a certain size
	fig = plt.figure(figsize=(10.0, 3.0))

	# create my figure axes
	axes1 = fig.add_subplot(1, 3, 1)
	axes2 = fig.add_subplot(1, 3, 2)
	axes3 = fig.add_subplot(1, 3, 3)

	# fill axes1
	axes1.set_ylabel('average')
	axes1.plot(data.mean(axis=0))

	# fill axes2
	axes2.set_ylabel('max')
	axes2.plot(data.max(axis=0))

	# fill axes3
	axes3.set_ylabel('min')
	axes3.plot(data.min(axis=0))

	# make the figure have a tight layout, no overlapping text
	fig.tight_layout()

	# save the figure to inflammation-xx.png
	figname = filename.replace('csv', 'png')
	plt.savefig(figname)
	


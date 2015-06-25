import numpy as np
import matplotlib.pyplot as plt

# load the first data file
data = np.loadtxt(fname='inflammation-01.csv', delimiter=',')

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

# show the figure
plt.show(fig)


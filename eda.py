import numpy as np
import peakutils
from peakutils.plot import plot as pplot
from matplotlib import pyplot
from scipy.ndimage import filters


## example code with randomly generated data
# centers = (30.5, 72.3)
# x = np.linspace(0, 120, 121)
# y = (peakutils.gaussian(x, 5, centers[0], 3) +
#     peakutils.gaussian(x, 7, centers[1], 10) +
#     np.random.rand(x.size))
# pyplot.figure(figsize=(10,6))
# pyplot.plot(x, y)
# pyplot.title("Data with noise")

# indexes = peakutils.indexes(y, thres=0.5, min_dist=30)
# print(indexes)
# print(x[indexes], y[indexes])
# interpolatedIndexes = peakutils.interpolate(x, y, ind=indexes)
# pyplot.figure(figsize=(10,6))
# pplot(x, y, indexes)
# print(interpolatedIndexes)
# pyplot.title('First estimate')

# pyplot.show()

#-------------------------------------------------
INTERVAL_LENTH = 1000
#interval at which q sensor is outputing data
# used to calculate time stamp

#processing and plotting the data without peak finding
csv = np.genfromtxt('puppies.txt', delimiter=',')
time = csv[:,0]
eda = csv[:,6]
x = np.linspace(1, len(eda), num=len(eda))
y = eda
print(y)
# normalize with log
# and blur with gaussian
y = filters.gaussian_filter(y, 30)
# y = np.log10(y)
pyplot.figure(figsize=(10,6))
pyplot.plot(x/INTERVAL_LENTH, y)

#plotting data with peaks
indexes = peakutils.indexes(y, thres=np.mean(y), min_dist=10)
#possible thresholds for indexes
#thres=0.4*max(y)
#thres=np.mean(y)
#can filter by mean, or max value percentage, 
#distance is set to 10 seconds
pyplot.figure(figsize=(10,6))
pplot(x, y, indexes)
pyplot.title('First estimate')

# #removing baseline
# base = peakutils.baseline(y, 2)
# y2 = y-base
# indexes2 = peakutils.indexes(y, thres=np.mean(y2), min_dist=10)
# pyplot.figure(figsize=(10,6))
# pplot(x, y2, indexes2)
# pyplot.title('Removing baseline')


pyplot.show()
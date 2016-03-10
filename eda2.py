import numpy as np
import sys
import peakutils
from peakutils.plot import plot as pplot
from matplotlib import pyplot
from scipy.ndimage import filters
import re
import csv
#two lines here and a few commented out at the bottom so we can fix the formatting and create a new file to log to. 
#f = open('features.csv', 'w')
#fwrite = csv.writer(f)


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
csv = np.genfromtxt('trial_data/tast.txt', delimiter=',')
time = csv[:,0]
eda = csv[:,6]
#cut out first and last interval if it's not a baseline read (assuming baseline reads time <= 6 minutes)
if len(eda) >= 3600: #change from 3600 if different time window; this is for 6 minutes.
    eda = eda[3601:len(eda)]
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

#calculating mean phasic peak amplitude, sum phasic peak amplitude, and phasic peak frequency EDA

def get_phasic_values(time_window, peak_vals):
    """Given a time interval (/10 = seconds) and a csv of peakutils calculated peak y-values, returns 
    a list containing the sum peak phasic amplitude eda, the mean peak phasic amplitude eda,
    and the phasic peak frequency for each time interval."""

    eda_vectors = []
    #when filled with data, eda_vectors has (mean PPA, sum PPA, frequency) 
    #(so its length = the total number of time windows)
 
    i=time_window #time_window should be 1800 for 3 minutes
    j=0
    while i < max(x[peak_vals]+time_window):
        while j < max(x[peak_vals]):
            slider = []
            #slider is a list of eda readings in time window in question
            for peak in peak_vals:
                if j <= x[peak] <= i:
                    #print str(x[peak]) + " is between " + str(j) + " and " + str(i)
                    slider.append(y[peak])
                    eda_xval = (i+j)/2.0
            eda_phasic_sum = sum(slider)
            eda_phasic_mean = sum(slider)/len(slider)
            eda_phasic_freq = len(slider)
            features = eda_xval, eda_phasic_sum, eda_phasic_mean, eda_phasic_freq
            eda_vectors.append(features)
            #print features
            j = i
            i += time_window    


    return eda_vectors

values = get_phasic_values(1800, indexes)

xvals = np.array([v[0] for v in values])
sums = np.array([v[1] for v in values])
means = np.array([v[2] for v in values])
freqs = np.array([v[3] for v in values])

#pyplot.figure(figsize=(10,6))
#pplot(x, y, indexes)
#pyplot.title('Means')

def plot_phasic(interval):
    """
    Plots the time intervals as vertical lines."""
    

    #visually segment the time intervals
    for i in range(0, len(xvals)):
        pyplot.axvline(x = xvals[i] - interval/2.0)

interval = 1800
#should be 1800 for 3-minute intervals

#to plot mean
pyplot.figure(figsize=(10,6))
plot_phasic(interval)
pplot(x, y, indexes)
pyplot.plot(xvals, means, 'go')
pyplot.title('Means')

#to plot sum
pyplot.figure(figsize=(10,6))
plot_phasic(interval)
pyplot.plot(xvals, sums, 'r-')
pyplot.plot(xvals, sums, 'ro')
pyplot.title('Sums')

#to plot freq
pyplot.figure()
plot_phasic(interval)
#pyplot.hist(freqs, bins=max(x[indexes])/interval)
pyplot.plot(xvals, freqs, 'y-')
pyplot.plot(xvals, freqs, 'yo')
pyplot.title('Frequencies')


#for now, just printing series of mean PPA, sum PPA, frequency 
print("SUM, MEAN, FREQUENCY EDA")
for read in values:
    print(read) 

#uncomment when csv writing is set up
#for rec in values:
    #fwrite.writerow([rec])

#f.close()

pyplot.show()


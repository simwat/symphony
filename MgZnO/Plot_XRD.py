#!/usr/bin/env python
# coding: utf-8

# In[14]:


# Takes a .csv exported from XRD data file and plots the peaks
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')
fig = plt.figure()
ax = fig.add_subplot(111)
#import os 

#rootdir = '/home/jupyter/.local/share/jupyter'

FilePath = input('Please enter the file path and file name of the XRD data: ')

f = open(FilePath)

# identify how many lines of header (known lines of comment)
Start = False
header = 0
while Start == False:
    line = f.readline()
    header += 1
    if 'Angle,Intensity' in line:
        Start = True
        
Angle, Intensity = np.genfromtxt(FilePath, delimiter=",", unpack = True, skip_header=header)
ax.plot(Angle, Intensity)
plt.title(FilePath)
plt.xlabel('Angle (degrees)')
plt.ylabel('Intensity')
plt.show()
fig.savefig('H1092.png')
print('Done plotting and saved')


# In[ ]:





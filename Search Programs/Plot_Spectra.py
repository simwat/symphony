#!/usr/bin/env python
# coding: utf-8

# In[8]:


# SAMPLE H1101b
import numpy as np
import matplotlib.pyplot as plt
#import plotly.graph_objects as go

#E = hc/lambda in eV calculations
h = 6.62606891*10**(-34) # m^2kg/s
c = 299792458 # m/s
eV = 1.602176634*10**(-19) # J
Conversion = h*c/eV

FileNames = input('Please enter the filepath followed by the filename you would like to plot: ')
#fig = go.Figure()
Wavelength, Count = np.genfromtxt(FileNames, delimiter="\t", unpack = True, skip_header=4)
EnergyEV = [0]*len(Wavelength)
    
Wavelength = Wavelength*10**(-9)*1.000289
EnergyEV = Conversion/Wavelength*1000
    
# Add traces
plt.plot(EnergyEV, Count)

#fig['layout']['xaxis'].update(title='Energy (meV)', dtick=5, autorange=True)
#fig['layout']['yaxis'].update(title='Counts/sec', autorange=True)
plt.title(FileNames)
plt.xlabel('meV')
plt.ylabel('Counts/sec')
plt.show()


# In[ ]:





# In[ ]:





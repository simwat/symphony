#!/usr/bin/env python
# coding: utf-8

# In[10]:


# This program searches up data files containing specific sample names, within a local directory

import os
rootdir = 'c:/Users/Pat/Documents/PL-folder/Data' # pls change to your own directory

# input 
input1 = input('Please enter what you are looking for: ') 
  
# output 
print(input1) 


for subdir, dirs, files in os.walk(rootdir): # for every folder and file in the root directory
    for file in files: # for every file
        f = open(os.path.join(subdir, file)) # open the file
        try: # the program will run this section unless there is an error
            line = f.readline() # reads first line of the data file (the header)
            if input1 in line or input1 in os.path.join(subdir, file): # checks if keyword is in the first line or filename
                if '.pxp' in os.path.join(subdir, file):
                    print(os.path.join(subdir, file)) # prints only path of selected file for Igor files
                    print('')
                else:
                    print(os.path.join(subdir, file)) # prints path of selected file
                    print(line) # prints first line of header
                    print(f.readline()) # prints the next line of the header
                    
        except UnicodeDecodeError: # if there is an error about reading the file, do this
            #print('Error File', os.path.join(subdir, file))
            continue # go on to the next iteration
            
print('')
print('******************')
print('Finished Search :)')
        


# In[ ]:





# In[ ]:






# coding: utf-8

# ## analysing tabular data

# In[6]:

import numpy


# In[7]:

numpy.loadtxt


# In[8]:

numpy.loadtxt(fname='data/weather-01.csv' delimiter = ',')


# In[9]:

numpy.loadtxt(fname='data/weather-01.csv'delimiter=',')


# In[10]:

numpy.loadtxt(fname='data/weather-01.csv',delimiter=',')


# # variables

# In[11]:

weight_kg=55


# In[12]:

print (weight_kg)


# In[13]:

print('weight in pounds:',weight_kg*2.2)


# In[14]:

numpy.loadtxt(fname='data/weather-01.csv',delimiter=',')


# In[15]:

numpy.loadtxt(fname='data/weather-01.csv',delimiter=',')


# In[16]:

numpy.loadtxt(fname='data/weather-01.csv',delimiter=',')


# In[17]:

get_ipython().magic('whos')


# In[18]:

data=numpy.loadtxt(fname='data/weather-01.csv',delimiter=',')


# In[19]:

get_ipython().magic('whos')


# In[20]:

get_ipython().magic('whos')


# In[21]:

print(data.dtype)


# In[22]:

print(data.shape)


# # this is 60 by 40
# 

# In[23]:

print ("first value in data:",data [0,0])


# In[24]:

print ('A middle value:',data[30,20])


# # lets get the first 10 columns for the firsst 4 rows
# 

# print(data[0:4, 0:10])
# # start at index 0 and go up to but not including index 4

# In[25]:

print (data[0:4, 0:10])


# #we dont need to start slicng at 0

# In[26]:

print (data[5:10,7:15])


# #we dont even need to inc upper and lower limits

# In[27]:

smallchunk=data[:3,36:]
print(smallchunk)


# #arithmetic on arrays

# In[28]:

doublesmallchunk=smallchunk*2.0


# In[29]:

print(doublesmallchunk)


# In[30]:

triplesmallchunk=smallchunk+doublesmallchunk


# In[31]:

print(triplesmallchunk)


# In[32]:

print(numpy.mean(data))


# In[33]:

print (numpy.max(data))


# In[34]:

print (numpy.min(data))


# #get a set of data for the first station
# #this is shorthand for "all the columns"

# In[35]:

station_0=data[0,:]


# In[36]:

print(numpy.max(station_0))


# #we dont need to create @temporary@ array slices
# #we can refer to what we call array axes

# In[37]:

print(numpy.mean(data, axis=0))


# In[38]:

print(numpy.mean(data, axis=1))


# #axis = 0 gets mean down eaach column
# #axis=1 gets the mean across each row so the mean temp
# #for each station for all periods
# #see above

# #do some simple vissualisations

# In[39]:

import matplotlib.pyplot


# In[40]:

get_ipython().magic('matplotlib inline')


# In[41]:

image=matplotlib.pyplot.imshow(data)


# #lets look at the average tempp over time

# In[42]:

avg_temperature=numpy.mean(data,axis=0)


# In[43]:

avg_plot=matplotlib.pyplot.plot(avg_temperature)


# In[44]:

import numpy


# In[45]:

import matplotlib.pyplot


# In[46]:

get_ipython().magic('matplotlib inline')


# In[47]:

data=numpy.loadtxt(fname='data/weather-01.csv',delimiter=',')


# #create a wide figure to hold sub plots

# In[48]:

fig=matplotlib.pyplot.figure (figsize=(10.0,3.0))


# #create placeholders for plots

# In[ ]:




# In[49]:

fig=matplotlib.pyplot.figure (figsize=(10.0,3.0))
subplot1=fig.add_subplot (1,3,1)
subplot2=fig.add_subplot (1,3,2)
subplot3=fig.add_subplot (1,3,3)

subplot1.set_ylabel('average')
subplot1.plot(numpy.mean(data, axis=0))

subplot2.set_ylabel('minimum')
subplot2.plot(numpy.min(data, axis=0))

subplot3.set_ylabel('maximum')
subplot3.plot(numpy.max(data, axis=0))


# # this is fine for small numbers of datasets, what if wwe have hundreds or thousands?  we need more automaation

# #loops

# In[50]:

word='notebook'
print (word[4])


# #see aabove note diff between squaare and normaal brackets

# In[51]:

for char in word:
    # colon before word or indentation v imporetaant
    #indent is 4 spaces
    


# In[ ]:

for char in word:
    print (char)


# #reading filenames
# # get a list of all the filenames from disk

# In[52]:

import glob


# #global..something~

# In[53]:

print(glob.glob('data/weather*.csv'))


# #putting it all together

# In[54]:

filenames=sorted(glob.glob('data/weather*.csv'))
filenames=filenames[0:3]

for f in filenames:
    print (f)
    data=numpy.loadtxt(fname=f, delimiter=',')
    
#next bits need indenting


    fig=matplotlib.pyplot.figure (figsize=(10.0,3.0))
    subplot1=fig.add_subplot (1,3,1)
    subplot2=fig.add_subplot (1,3,2)
    subplot3=fig.add_subplot (1,3,3)

    subplot1.set_ylabel('average')
    subplot1.plot(numpy.mean(data, axis=0))

    subplot2.set_ylabel('minimum')
    subplot2.plot(numpy.min(data, axis=0))

    subplot3.set_ylabel('maximum')
    subplot3.plot(numpy.max(data, axis=0))
    
    fig.tight_layout()
    matplotlib.pyplot.show


# In[ ]:




# In[55]:

num=37
if num>100:
    print('greater')
else:
    print('not greater')
    print ('done')


# In[56]:

num=107
if num>100:
    print('greater')
else:
    print('not greater')
    print ('done')


# # didnt print "done" due to break in indentation sequence

# In[57]:

num=-3

if num>0:
    print (num, "is positive")
elif num ==0:
    print (num, "is zero")
else:
    print (num, "is negative")


# # elif eqauls else if, always good to finish a chain with an else

# In[58]:

filenames=sorted(glob.glob('data/weather*.csv'))


# In[59]:

filenames=sorted(glob.glob('data/weather*.csv'))
filenames=filenames[0:3]

for f in filenames:
    print (f)
    data=numpy.loadtxt(fname=f, delimiter=',') == 0 
    if numpy.max (data, axis=0)[0] ==0 and numpy.max (data, axis=0)[20] ==20:
        print ('suspicious looking maxima')
    elif numpy.sum(numpy.min(data, axis=0)) ==0:
        print ('minimum adds to zero')
    else:
        print ('data looks ok')
    
   
    
#next bits need indenting


    fig=matplotlib.pyplot.figure (figsize=(10.0,3.0))
    subplot1=fig.add_subplot (1,3,1)
    subplot2=fig.add_subplot (1,3,2)
    subplot3=fig.add_subplot (1,3,3)

    subplot1.set_ylabel('average')
    subplot1.plot(numpy.mean(data, axis=0))

    subplot2.set_ylabel('minimum')
    subplot2.plot(numpy.min(data, axis=0))

    subplot3.set_ylabel('maximum')
    subplot3.plot(numpy.max(data, axis=0))
    
    fig.tight_layout()
    matplotlib.pyplot.show


# #something went wrong with the above

# In[60]:

def fahr_to_kelvin(temp):
    return((temp-32)*(5/9)+ 273.15)


# In[61]:

print ('freezing point of water:', fahr_to_kelvin(32))


# In[62]:

print ('boiling point of water:', fahr_to_kelvin(212))


# #using functions

# In[63]:

def analyse (filename):
    data=numpy.loadtxt(fname=filename,)......


# #unfinsinshed

# In[64]:

def detect_problems (filename):
    data=numpy.loadtxt(fname=filename, delimiter=',')
    
    if numpy.max (data, axis=0)[0] ==0 and numpy.max (data, axis=0)[20] ==20:
        print ('suspicious looking maxima')
    elif numpy.sum(numpy.min(data, axis=0)) ==0:
        print ('minimum adds to zero')
    else:
        print ('data looks ok')
    
    


# In[65]:

for f in filenames [0:5]:
    print (f)
    analyse (f)
    detect_problems (f)
    


# In[ ]:

def analyse (filename):
    data=numpy.loadtxt(fname=filename,delimiter=',')
    
    fig=matplotlib.pyplot.figure (figsize=(10.0,3.0))
    subplot1=fig.add_subplot (1,3,1)
    subplot2=fig.add_subplot (1,3,2)
    subplot3=fig.add_subplot (1,3,3)

    subplot1.set_ylabel('average')
    subplot1.plot(numpy.mean(data, axis=0))

    subplot2.set_ylabel('minimum')
    subplot2.plot(numpy.min(data, axis=0))

    subplot3.set_ylabel('maximum')
    subplot3.plot(numpy.max(data, axis=0))
    
    fig.tight_layout()
    matplotlib.pyplot.show
    
    


# In[ ]:

for f in filenames [0:5]:
    print (f)
    analyse (f)
    detect_problems (f)
    


# In[ ]:




# In[ ]:




# In[ ]:




# In[66]:

help(numpy.loadtxt)


# In[67]:

help(detect_problems)


# In[69]:


"""some of our temperature files haave problems, check for these

this function reads a file and reports on odd looking maxima and minimia that add to zero
the function does not return any data
"""

def detect_problems (filename):
    data=numpy.loadtxt(fname=filename, delimiter=',')
    
    if numpy.max (data, axis=0)[0] ==0 and numpy.max (data, axis=0)[20] ==20:
        print ('suspicious looking maxima')
    elif numpy.sum(numpy.min(data, axis=0)) ==0:
        print ('minimum adds to zero')
    else:
        print ('data looks ok')
    


# In[70]:

def analyse (filename):
    data=numpy.loadtxt(fname=filename,delimiter=',')
    
    """ this function analyses a dataset and outputs plots for maax min and ave
    """
    
    fig=matplotlib.pyplot.figure (figsize=(10.0,3.0))
    subplot1=fig.add_subplot (1,3,1)
    subplot2=fig.add_subplot (1,3,2)
    subplot3=fig.add_subplot (1,3,3)

    subplot1.set_ylabel('average')
    subplot1.plot(numpy.mean(data, axis=0))

    subplot2.set_ylabel('minimum')
    subplot2.plot(numpy.min(data, axis=0))

    subplot3.set_ylabel('maximum')
    subplot3.plot(numpy.max(data, axis=0))
    
    fig.tight_layout()
    matplotlib.pyplot.show


# In[ ]:




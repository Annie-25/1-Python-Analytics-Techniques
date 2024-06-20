#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


df=pd.read_csv('Assessment 1 - Atliqo dataset.csv')
df.head(120)


# # Data Description

# In[3]:


shape=df.shape
print(shape)


# In[4]:


size=df.size
print(size)


# # Data Cleaning

# In[5]:


print(df.isnull())


# In[6]:


print(df.isnull().sum())


# # Data Visualization Techniques

# In[7]:


import matplotlib.pyplot as plt


# ## Revenue

# ### Revenue before and after 5G

# In[8]:


x=df['Month']
# Jan-April(Before 5G)
#Jun-Sept(After 5G)
y=(61, 43, 37, 37, 31, 28, 24, 21, 22, 12, 15, 8, 6, 5, 4, 61, 54, 39, 47, 56, 34, 29, 21, 16, 25, 12, 12, 6, 9, 4, 57, 49, 67, 42, 31, 28, 31, 29, 17, 15, 11, 17, 8, 6, 3, 65, 51, 49, 42, 33, 28, 46, 24, 15, 13, 12, 9, 10, 6, 4, 62, 42, 37, 38, 31, 28, 25, 21, 23, 12, 15, 8, 6, 6, 4, 60, 51, 38, 46, 54, 33, 28, 19, 15, 25, 11, 12, 6, 9, 4, 58, 49, 69, 44, 30, 28, 32, 29, 18, 16, 11, 18, 8, 6, 4, 65, 48, 48, 42, 32, 27, 46, 23, 15, 13, 12, 9, 10, 6, 4)

plt.title('Revenue before and after 5G')
plt.xlabel('Month')
plt.ylabel('Revenue/crores')

plt.plot(x,y,color='Blue')


# ### City with highest revenue 

# In[12]:


x=df['City']
y=[61, 43, 37, 37, 31, 28, 24, 21, 22, 12, 15, 8, 6, 5, 4, 61, 54, 39, 47, 56, 34, 29, 21, 16, 25, 12, 12, 6, 9, 4, 57, 49, 67, 42, 31, 28, 31, 29, 17, 15, 11, 17, 8, 6, 3, 65, 51, 49, 42, 33, 28, 46, 24, 15, 13, 12, 9, 10, 6, 4, 
62, 42, 37, 38, 31, 28, 25, 21, 23, 12, 15, 8, 6, 6, 4, 60, 51, 38, 46, 54, 33, 28, 19, 15, 25, 11, 12, 6, 9, 4, 58, 49, 69, 44, 30, 28, 32, 29, 18, 16, 11, 18, 8, 6, 4, 65, 48, 48, 42, 32, 27, 46, 23, 15, 13, 12, 9, 10, 6, 4]

plt.scatter(x,y,label='City with Highest Revenue Before and After 5G')
plt.xlabel('City')
plt.ylabel('Revenue / crores')
plt.legend()


# ## Average Revenue Per User (ARPU)

# ### ARPU Before and After 5G

# In[11]:


y= 192, 175, 175, 175, 203, 183, 200, 165, 189, 198, 188, 212, 185, 181, 191, 169, 189, 175, 189, 206, 193, 190, 171, 199, 210, 208, 170, 162, 187, 168, 213, 171, 187, 166, 211, 211, 201, 206, 186, 212, 197, 206, 202, 181, 197, 213, 191, 198, 169, 192, 199, 209, 163, 206, 193, 177, 212, 181, 185, 181, 193, 198, 199, 242, 198, 224, 199, 205, 251, 219, 252, 236, 199, 197, 255, 243, 240, 169, 186, 196, 164, 173, 175, 182, 162, 212, 218, 250, 231, 236, 248, 202, 195, 183, 209, 231, 161, 224, 175, 248, 212, 235, 191, 192, 237, 240, 218, 209, 225, 188, 250, 164, 255, 229, 249, 250, 177, 163, 238, 173
x=df['Gen']

plt.barh(x,y,label='ARPU Before and After Sales',color='yellowgreen')
plt.xlabel('ARPU')
plt.ylabel('Gen')


# ## Active Users

# ### Active users before and after 5G

# In[13]:


x_values=df['Month']
# Jan-April(Before 5G)
#Jun-Sept(After 5G)
y_values=df['Active users in lakhs']

plt.bar(x_values,y_values,label='Number 0f Active Users Before and After 5G',color='b')

plt.ylabel('Active users')
plt.xlabel('Month')


# ### City with highest number of active users

# In[14]:


x=df['City']
y=df['Active users in lakhs']

plt.barh(x,y,label='City with Highest Number of Active Users',color='yellowgreen')
plt.ylabel('City')
plt.xlabel('Active users / Lakhs')


# ## Unsubscribers (Churn Rate)

# ### Number of unsubscribers per city

# In[15]:


a=df["City"].value_counts().head(10)
print(a)
plt.figure(figsize=(8,8))
cols_values = ['orange','cyan','grey','indigo','green']
plt.pie(a,labels=df["City"].value_counts().head(10).index,autopct="%0.0f%%",shadow=True,explode=[0.2,0.1,0,0,0,],startangle=90,colors=cols_values);
plt.show()


# ### Number of Unsubscribers Before and After 5G

# In[16]:


x=df['Gen']
y=df['Unsubscribed users in lakhs']


plt.xlabel('Gen')
plt.ylabel('Unsubscribers / Lakhs')

plt.bar(x,y,label='Unsubscribers Before and After 5G',color='b')


plt.plot(x,y,color='Blue')


# ## Geographical Visualization

# In[60]:


import geopandas as gpd
import pandas as pd
from shapely.geometry import Polygon,Point
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import seaborn as sns

sns.set_style('whitegrid')


# In[21]:


import shapefile as shp


# In[22]:


fp = r'E:\India map'
map_df = gpd.read_file(fp) 
map_df_copy = gpd.read_file(fp)
map_df.head()


# In[23]:


map_df.plot()


# In[24]:


data=pd.read_csv('India Cities.csv')


# In[25]:


data_1=data.join(map_df)


# In[26]:


Atliqo=pd.read_csv('AtliQo_data.csv')


# In[31]:


new_data=data_1.join(Atliqo)
new_data.head()


# In[32]:


geometry = [Point(xy) for xy in zip(new_data.lat,new_data.lng)]
fig,ax = plt.subplots(figsize =(50,50),)

ax.axis('off')
ax.set_title('Map of India showing India States', fontdict={'fontsize': '30', 'fontweight' : '20'})

map_df.boundary.plot(ax = ax)

geo_df = gpd.GeoDataFrame(geometry = [])

g = geo_df.plot(ax = ax,label = 'States',cmap='hsv',legend=True)
                
for i in range(len(new_data)):
    plt.text(new_data.lng[i],new_data.lat[i],"{}".format(new_data.city[i]),size=20)
    
plt.show()


# In[45]:


data_2=pd.read_csv('Atliqo_cities.csv')
data_2.head()


# In[42]:


New_data=new_data.merge(data_2)
New_data.head()


# In[62]:


geometry = [Point(xy) for xy in zip(New_data.lng,New_data.lat)]
fig,ax = plt.subplots(figsize = (9,9))
ax.axis('off')
ax.set_title('Map of India showing where Atliqo is Present', fontdict={'fontsize': '20', 'fontweight' : '10'})

map_df.boundary.plot(ax = ax)

geo_df = gpd.GeoDataFrame(geometry = geometry)

g = geo_df.plot(ax = ax, markersize = 50, color = 'red',marker = '*',label = 'Cities')
                
for i in range(len(New_data)):
    plt.text(New_data.lng[i],New_data.lat[i],"{}".format(New_data.city[i]),size=10)
    
plt.show()


# In[ ]:





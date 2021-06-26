#!/usr/bin/env python
# coding: utf-8

# # 1) Movies with 3 highest and 3 lowest budget.

# In[1]:


import pandas as pd


# In[2]:


df = pd.read_csv('tmdb-movies.csv')


# In[3]:


df


# In[4]:


df.info()


# In[5]:


df["budget"]


# In[6]:


df.loc[:,["budget","original_title"]]


# In[7]:


df.loc[:,["budget","original_title"]].nlargest(10,"budget")


# #### Movie with third highest budget is-Pirates of the Caribbean: At World's End

# In[8]:


df.loc[:,["budget","original_title"]].nsmallest(10,"budget")


# In[9]:


filt=(df["budget"]==0)


# In[10]:


df.loc[filt,["budget"]]


# In[11]:


df.loc[filt,["budget"]] = df["budget"].mean()


# In[12]:


df.loc[:,["budget","original_title"]].nsmallest(10,"budget")


# ### Movie with third lowest budget is- Angus, Thongs and Perfect Snogging

# # 2) Movies with most and least earned revenue

# In[13]:


df


# In[15]:


df["revenue"]


# In[16]:


df.loc[:,["revenue","original_title"]]


# In[17]:


df.loc[:,["revenue","original_title"]].nlargest(10,"revenue")


# ### Movie with most earned revenue is- Avatar

# In[18]:


df.loc[:,["revenue","original_title"]].nsmallest(10,"revenue")


# In[20]:


filt = (df["revenue"]==0)


# In[21]:


df.loc[filt,["revenue"]]


# In[22]:


df.loc[filt,["revenue"]] = df["revenue"].mean()


# In[23]:


df.loc[:,["revenue","original_title"]].nsmallest(10,"revenue")


# ### Movie with least earned revenue is-Shattered Glass

# # 3) Average runtime of movies in the year 2006

# In[24]:


df


# In[26]:


df.loc[:,["runtime","original_title"]]


# In[27]:


df.loc[:,["runtime"]].mean()


# In[28]:


filt = (df["release_year"]==2006)


# In[29]:


df.loc[filt,["release_year"]]


# In[30]:


df.loc[filt,["runtime"]].mean()


# ### Average runtime of movies in the year 2006 is- 101.68 mins

# # 4) Most common Genre for Vin Diesel & Emma Watson movies

# In[3]:


import pandas as pd


# In[4]:


df = pd.read_csv('tmdb-movies.csv')


# In[5]:


df


# In[7]:


df.loc[:,["genres","cast"]]


# In[8]:


df.isna().sum()


# In[9]:


df.fillna("abc",inplace = True)


# In[10]:


filt = (df["cast"])


# In[11]:


filt = df["cast"].str.contains("Vin Diesel")


# In[12]:


df.loc[filt,["genres"]]


# In[13]:


data = df.loc[filt,"genres"]


# In[14]:


data.tolist()


# In[15]:


filt = (df["cast"].str.contains("Vin Diesel"))

vin_df = df.loc[filt,"genres"].apply(lambda x:x.split("|"))
genres_ = set()
total_list = []

for gen in vin_df.tolist():
    for i in gen:
        total_list.append(i)
        genres_.add(i)
genres_


most_common = dict.fromkeys(genres_)
for gen in genres_:
    most_common[gen] = total_list.count(gen)
    

most_common = dict(sorted(most_common.items(),key=lambda x:x[1],reverse=True))


# In[16]:


most_common


# ###  Most common Genre for Vin Diesel is- Action 

# In[17]:


df


# In[18]:


df.loc[:,["genres","cast"]]


# In[19]:


df.isna().sum()


# In[20]:


filt = (df ["cast"])


# In[21]:


filt = df["cast"].str.contains("Emma Watson")


# In[22]:


df.loc[(filt),["genres"]]


# In[23]:


data = df.loc[filt,"genres"]


# In[24]:


data.tolist()


# In[25]:


filt = (df["cast"].str.contains("Emma Watson"))

emma_df = df.loc[filt,"genres"].apply(lambda x:x.split("|"))
genres_ = set()
total_list = []

for gen in emma_df.tolist():
    for i in gen:
        total_list.append(i)
        genres_.add(i)
genres_


most_common = dict.fromkeys(genres_)
for gen in genres_:
    most_common[gen] = total_list.count(gen)
    

most_common = dict(sorted(most_common.items(),key=lambda x:x[1],reverse=True))


# In[26]:


most_common


# ###  Most common Genre for Emma Watson is- Family 

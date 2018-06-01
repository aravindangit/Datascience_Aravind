
# coding: utf-8

# In[1]:


import pandas as pd
train = pd.read_csv('Train File.csv')
test = pd.read_csv('Test File.csv')


# In[2]:


train.dtypes


# In[3]:


train.describe()


# In[9]:


categorical_variable = train.dtypes.loc[train.dtypes=='object'].index


# In[11]:


print(categorical_variable)


# In[14]:


train[categorical_variable].apply(lambda x: len(x.unique()))


# In[16]:


train['Race'].value_counts()


# In[17]:


train['Race'].value_counts()/train.shape[0]


# In[20]:


train.shape[0]


# In[21]:


train['Native.Country'].value_counts()


# In[22]:


train['Native.Country'].value_counts()/train.shape[0]


# In[23]:


train.head()


# In[30]:


train.loc[[train['Marital.Status'] =='Divorced'].value_counts()]


# In[31]:


train['Marital.Status'].value_counts()/train.shape[0]


# In[34]:


ct = pd.crosstab(train['Sex'],train['Income.Group'],margins=True)
print (ct)


# In[35]:


get_ipython().run_line_magic('matplotlib', 'inline')
ct.iloc[:-1,:-1].plot(kind='bar',stacked='True',color=['red','blue'],grid='False')


# In[39]:


ct.iloc[:-1,:-1]


# In[42]:


def PercConvert(ser):
    return ser/float(ser[-1])
ct2 = ct.apply(PercConvert, axis=1)
ct2.iloc[:-1,:-1].plot(kind='bar',stacked='True',color=['red','blue'],grid='False')


# In[44]:


train.plot('Age','Hours.Per.Week',kind='scatter')


# In[45]:


train.boxplot(column='Hours.Per.Week',by='Sex')


#!/usr/bin/env python
# coding: utf-8

# In[43]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[44]:


match_data = pd.read_csv("E:/Python aniket/IPL Dataset and Code/IPL Dataset and Code/IPL Matches 2008-2020.csv")
ball_data = pd.read_csv("E:/Python aniket/IPL Dataset and Code/IPL Dataset and Code/IPL Ball-by-Ball 2008-2020.csv")


# In[45]:


match_data.head()


# In[46]:


ball_data.head()


# In[47]:


match_data.isnull().sum()


# In[48]:


ball_data.isnull().sum()


# In[49]:


ball_data.shape


# In[50]:


ball_data.columns


# In[51]:


match_data.shape


# 

# In[52]:


match_data.columns


# In[53]:


match_data['Season'] = pd.DatetimeIndex(match_data['date']).year
match_data.head()


# In[54]:


match_per_season = match_data.groupby(['Season'])['id'].count().reset_index().rename(columns={'id':'matches'})
match_per_season


# In[55]:


sns.countplot(match_data['Season'])
plt.xticks(rotation=90, fontsize=10)
plt.yticks(fontsize=10)
plt.xlabel('Season', fontsize=10)
plt.ylabel('Count' , fontsize=10)
plt.title('Total matches played in each season', fontsize=10 , fontweight='bold')


# In[56]:


season_data=match_data[['id','Season']].merge(ball_data, left_on = 'id', right_on = 'id', how = 'left').drop('id', axis = 1)
season_data.head()


# In[57]:


season=season_data.groupby(['Season'])['total_runs'].sum().reset_index()
p=season.set_index('Season')
ax = plt.axes()
ax.set(facecolor = "white")
sns.lineplot(data=p,palette="magma") 
plt.title('Total runs in each season',fontsize=12,fontweight="bold")
plt.show()


# In[58]:


toss=match_data['toss_winner'].value_counts()
ax = plt.axes()
ax.set(facecolor = 'white')
sns.set(rc={'figure.figsize':(20,15)},style = 'darkgrid')
ax.set_title('No.of tosses won by each team', fontsize=15,fontweight='bold')
sns.barplot(y=toss.index, x=toss, orient='h', palette='icefire', saturation=1)
plt.xlabel('# of tosses won')
plt.ylabel('Teams')
plt.show()


# In[59]:


ax = plt.axes()
ax.set(facecolor = 'gray')
sns.countplot( x= 'Season', hue='toss_decision', data=match_data, palette= 'magma',saturation=1)
plt.xticks(rotation=90, fontsize=10)
plt.yticks(fontsize=15)
plt.xlabel('\n Season', fontsize=15)
plt.ylabel('Count', fontsize=15)
plt.title('Toss decision across seasons', fontsize=12,fontweight='bold')
plt.show


# In[60]:


match_data['result'].value_counts()


# In[61]:


match_data.winner[match_data.result!='winner'].mode()


# In[62]:


toss = match_data['toss_winner']== match_data['winner']
plt.figure(figsize=(10,5))
sns.countplot(toss)
plt.show()


# In[63]:


plt.figure(figsize=(12,4))
sns.countplot(match_data.toss_decision[match_data.toss_winner == match_data.winner])
plt.show()


# In[64]:


player = (ball_data['batsman']=='MS Dhoni')
df_dhoni=ball_data[player]
df_dhoni.head()


# In[65]:


df_dhoni['dismissal_kind'].value_counts().plot.pie(autopct='%1.1f%%',shadow=True,rotatelabels=True)
plt.title('Dismissal kind', fontweight='bold',fontsize=15)
plt.show()


# In[67]:


runs = ball_data.groupby(['batsman'])['batsman_runs'].sum().reset_index()
runs.columns = ['Batsman', 'runs']
y = runs.sort_values(by='runs', ascending = False).head(10).reset_index().drop('index', axis=1)
y


# In[68]:


ax = plt.axes()
ax.set(facecolor = "grey")
sns.barplot(x=y['Batsman'],y=y['runs'],palette='rocket',saturation=1)
plt.xticks(rotation=90,fontsize=10)
plt.yticks(fontsize=10)
plt.xlabel('\n Player',fontsize=15)
plt.ylabel('Total Runs',fontsize=15)
plt.title('Top 10 run scorers in IPL',fontsize=15,fontweight="bold")


# In[72]:


ax = plt.axes()
ax.set(facecolor = "gray")
match_data.player_of_match.value_counts()[:10].plot(kind='bar')
plt.xlabel('Players')
plt.ylabel("Count")
plt.title("Highest MOM award winners",fontsize=15,fontweight="bold")


# In[ ]:





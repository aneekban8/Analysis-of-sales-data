# -*- coding: utf-8 -*-
"""
Created on Wed Jul  5 10:35:49 2023

@author: ANEEK BANDYOPADHYAY
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import datetime
from warnings import filterwarnings
#import re
filterwarnings('ignore')
pd.set_option('display.max_column', None)
data=pd.read_excel('D:/Upwork/MakeUP_IVY/Makeup_IVY 4 Python.xlsm',sheet_name='Sheet1')
data["Date"]=pd.to_datetime(data["Date"]).dt.strftime("%d-%m-%Y")
data["Year"]=pd.DatetimeIndex(data['Date']).year
d_2004=data[data.Year==2004]
#fig,ax=plt.subplots(figsize=(15,15))
k=d_2004.groupby(['Name','Product'])
d_2004_total=k['Total']
d1=(d_2004_total.agg('sum').round(0).unstack())
#d1=d1.reset_index()
#d1.plot(x="Name",kind='bar', stacked=False,title='Sales by each person')
dict1=d1.to_dict('list')
persons=list(d1.index)
bar_width=0.16
x_pos=np.arange(len(persons))
fig,ax=plt.subplots()
for i, (pr_od,sls) in enumerate(dict1.items()):
    # Calculate the x-axis position for the current group of bars
    pos=x_pos+(i*bar_width)
    #Create a set of bars for the current group
    rects=ax.bar(pos,sls,width=bar_width,label=pr_od)
    #ax.bar_label(rects,padding=3,fontsize=6,rotation=-90)
ax.set_xticks(x_pos+((len(dict1)-1)/2)*bar_width)
ax.set_xticklabels(persons, fontsize=8)
ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
ax.set_xlabel('Sales Persons')
ax.set_ylabel('Dollars')
ax.set_title('Grouped Bar Plot')

# Show the plot
plt.show()   

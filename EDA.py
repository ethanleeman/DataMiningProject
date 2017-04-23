# -*- coding: utf-8 -*-
"""
Quora competition


"""

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import gensim
from gensim import models
import plotly.offline as py
#py.init_notebook_mode(connected=True)
import plotly.graph_objs as go
import plotly.tools as tls

#import os
#print(os.listdir('../input'))

#put your path to training set below
df = pd.read_csv("../input/train.csv").fillna("")

df['q1_n_words'] = df['question1'].apply(lambda row: len(row.split(" ")))
df['q2_n_words'] = df['question2'].apply(lambda row: len(row.split(" ")))

df_short=df.loc[(df['q1_n_words'] <3) | (df['q2_n_words'] <3)]
#df_diff=df.loc[np.abs((df['q1_n_words'] - df['q2_n_words']) >10)]
nz=np.count_nonzero(df_short['is_duplicate'])


df_new=df.loc[(df['q1_n_words'] >1) & (df['q2_n_words'] >1)]

str_head=[]
str_head_count=np.zeros(7195)
for i in df_new['id']:
    if df_new['question1'][i].partition(' ')[0] in str_head:
        str_head_count[str_head.index(df_new['question1'][i].partition(' ')[0])]+=1
    else:
        str_head.append(df_new['question1'][i].partition(' ')[0])
        str_head_count[len(str_head)]=1
        
    if df_new['question2'][i].partition(' ')[0] in str_head:
        str_head_count[str_head.index(df_new['question2'][i].partition(' ')[0])]+=1
    else:
        str_head.append(df_new['question2'][i].partition(' ')[0])
        str_head_count[len(str_head)]=1

idx=(-str_head_count).argsort()[:20]   
print "Most frequent question headings:\n"
for ii in idx:
    print str_head[ii], str_head_count[ii]



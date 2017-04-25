# -*- coding: utf-8 -*-
"""
This data cleaning program expands abbreviation and convert all "," to "."
It also removes stop words and duplicated words.

"""

import numpy as np
import pandas as pd
#import seaborn as sns
#import matplotlib.pyplot as plt
#import gensim
#from gensim import models
#import plotly.offline as py
#py.init_notebook_mode(connected=True)
#import plotly.graph_objs as go
#import plotly.tools as tls
import nltk
from nltk.corpus import stopwords
#from nltk.stem import SnowballStemmer
#from IPython.display import display
#import os
#print(os.listdir('../input'))

#remove all punctuation
punctuation='[)("\'?&]'
#put in entries in abbriviation dictionary
abbr_dict={

    "what's":"what is",
    "whats":"what is",
    "what're":"what are",
    "who's":"who is",
    "who're":"who are",
    "where's":"where is",
    "where're":"where are",
    "when's":"when is",
    "when're":"when are",
    "how's":"how is",
    "how're":"how are",
    
    "what about":"how about",

    "i'm":"i am",
    "we're":"we are",
    "you're":"you are",
    "they're":"they are",
    "it's":"it is",
    "he's":"he is",
    "she's":"she is",
    "that's":"that is",
    "there's":"there is",
    "there're":"there is",

    "i've":"i have",
    "we've":"we have",
    "you've":"you have",
    "they've":"they have",
    "who've":"who have",
    "would've":"would have",
    "not've":"not have",

    "i'll":"i will",
    "we'll":"we will",
    "you'll":"you will",
    "he'll":"he will",
    "she'll":"she will",
    "it'll":"it will",
    "they'll":"they will",

    "isn't":"be not",
    "wasn't":"be not",
    "aren't":"be not",
    "weren't":"be not",
    "can't":"can not",
    "couldn't":"can not",
    "don't":"do not",
    "didn't":"do not",
    "shouldn't":"should not",
    "wouldn't":"will not",
    "doesn't":"do not",
    "haven't":"have not",
    "hasn't":"have not",
    "hadn't":"have not",
    "won't":"will not",
    
#    "is":"be",
#    "are":"be",
#    "am":"be",
#    "was":"be",
#    "were":"be",
    "does":"do",
#    "did":"do",
#    "has":"have",

    
# remove spacing between sentences
    ",":".",
    ":":".",
    ";":".",
    "!":".",
    "@":"at",
    

    
}

punct_dict={
    punctuation:'',
    '\s+':' ',  # replace multi space with one single space
}


def process_data(data):
    data.question1=data.question1.str.lower() # conver to lower case
    data.question2=data.question2.str.lower()
    data.question1=data.question1.astype(str)
    data.question2=data.question2.astype(str)
    data.replace(abbr_dict,regex=True,inplace=True)
    data.replace(punct_dict,regex=True,inplace=True)
    return data


    
#put your path to training set below
print "Importing data..."
df = pd.read_csv("../input/train.csv").fillna("")

#count the number of all question pairs
maxlen=len(df)

# Expand abbreviations
print "Expanding abbrev..."
df = process_data(df)



print "Removing stopwords and duplicated words..."

def unique_list(l):
    ulist = []
    [ulist.append(x) for x in l if x not in ulist]
    return ulist
    

#Put the words that you don't want to delete below, unicode
useful_words = [u'what',u'why',u'who',u'whom',u'how',u'when',u'when',u'not'u'which',u'no']
#stop words are those in stopwords.words('english') minus useful_words
stop_words = [x for x in stopwords.words('english') if x not in useful_words]




for i in range(maxlen):
    #Q1
    q1=df['question1'][i]
    #remove stop words
    q1_remove=[word for word in q1.split(" ") if word.decode('utf-8') not in stop_words]
    #remove duplicated words
    q1=' '.join(unique_list(q1_remove))
    df.set_value(i,'question1',q1)
    #Q2
    q2=df['question2'][i]
    q2_remove=[word for word in q2.split(" ") if word.decode('utf-8') not in stop_words]
    q2=' '.join(unique_list(q2_remove))
    df.set_value(i,'question2',q2)

df.to_csv('train_remove_abbrev_stop_duplicate_words.csv')

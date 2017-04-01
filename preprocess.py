import pandas as pd
import matplotlib.pyplot as plt
import gensim


##One of them has a null value? okay.
def forcestring(x):
    if type(x) is str:
        return x
    return ""

## gensim removes stopwords, takes the stem of the rest, makes bag of words
def preproc(df):
    df['question1'] = df['question1'].apply(forcestring)
    df['question2'] = df['question2'].apply(forcestring)
    df['q1proc'] = df['question1'].apply(gensim.parsing.preprocessing.preprocess_string)
    df['q2proc'] = df['question2'].apply(gensim.parsing.preprocessing.preprocess_string)

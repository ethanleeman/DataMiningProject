import pandas as pd
import matplotlib.pyplot as plt

pdtrain = pd.DataFrame.from_csv('../Data/RawData/train.csv')
#pdtrain.info()
#print pdtrain.dtypes
#print pdtrain.describe()
#print pdtrain.head()
#print pdtrain.tail()
#print pdtrain['is_duplicate']

q1split = pdtrain['question1'].str.split(' ')
q2split = pdtrain['question2'].str.split(' ')

def first(x):
    if type(x) is list:
        return x[0]
    return ''

##### Plots how well the first word matching works on the training data
#sFirstWordMatch = (q1split.apply(first)==q2split.apply(first)).apply(int)
#sFirstWordMatch.plot.hist()
#plt.show()

####Plot length of the string for the first questions in trianing
#s1length = pdtrain['question1'].str.len()
#s1length.plot.hist()
#plt.show()

pdtest = pd.DataFrame.from_csv('../Data/RawData/test.csv')
pdtest['q1split'] = pdtest['question1'].str.split(' ')
pdtest['q2split'] = pdtest['question2'].str.split(' ')
pdtest['is_duplicate'] = (pdtest['q1split'].apply(first) == pdtest['q2split'].apply(first)).apply(int)
dfAnswer = pdtest['is_duplicate']
dfAnswer.to_csv('../Data/ProcessedData/answer.csv', header = True)

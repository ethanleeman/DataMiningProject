## Making features
import pandas as pd
import gensim

## This makes the Jaccard similarity between the 2 preprocessed bag-of-words
def Jac(x):
    if (len(x['q1proc']) > 0 and len(x['q2proc']) > 0):
        return gensim.matutils.jaccard(x['q1proc'],x['q2proc'])
    return 1.0

def JacFeat(df):
    df['jaccard'] = df.apply(Jac, axis=1)




#def first(x):
#    if type(x) is list:
#        return x[0]
#    return ''

##### Plots how well the first word matching works on the training data
#sFirstWordMatch = (q1split.apply(first)==q2split.apply(first)).apply(int)
#sFirstWordMatch.plot.hist()
#plt.show()

####Plot length of the string for the first questions in trianing
#s1length = pdtrain['question1'].str.len()
#s1length.plot.hist()
#plt.show()

# pdtest = pd.DataFrame.from_csv('../Data/RawData/test.csv')
# pdtest['q1split'] = pdtest['question1'].str.split(' ')
# pdtest['q2split'] = pdtest['question2'].str.split(' ')
# pdtest['is_duplicate'] = (pdtest['q1split'].apply(first) == pdtest['q2split'].apply(first)).apply(int)
# dfAnswer = pdtest['is_duplicate']
# dfAnswer.to_csv('../Data/ProcessedData/answer.csv', header = True)



## Make more features, put them in here
def makeFeatures(df):
    JacFeat(df)

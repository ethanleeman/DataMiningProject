import pandas as pd
import matplotlib.pyplot as plt
import gensim
import preprocess
import model
import featureEng

##### Section A             ####
##### Takes a bit of time...####
dftrain = pd.DataFrame.from_csv('../Data/RawData/train.csv')
dftest = pd.DataFrame.from_csv('../Data/RawData/test.csv')

preprocess.preproc(dftrain)
preprocess.preproc(dftest)


##### Section B, comment Section A out              ####
##### After you do A once, just load it again       ####
#dftrain = pd.DataFrame.from_csv('../Data/ProcessedData/train.csv')
#dftest = pd.DataFrame.from_csv('../Data/ProcessedData/test.csv')


featureEng.makeFeatures(dftrain)
featureEng.makeFeatures(dftest)

model.model(dftrain, dftest)

#### Some methods to check out the data
#dftrain.info()
#print dftrain.dtypes
#print dftrain.describe()
#print dftrain.head()
#print dftrain.tail()
#print dftrain['is_duplicate']


## Save your stuff to reload it in Section B
dftrain.to_csv('../Data/ProcessedData/train.csv', header = True)
dftest.to_csv('../Data/ProcessedData/test.csv', header = True)

## Save an answer for submission
dfAnswer = dftest['is_duplicate']
dfAnswer.to_csv('../Data/ProcessedData/answer.csv', header = True)

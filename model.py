## Anything that takes in features and outputs a guess
import pandas as pd
from sklearn import tree

#dftrain = pd.DataFrame.from_csv('../Data/ProcessedData/train.csv')
#dftest = pd.DataFrame.from_csv('../Data/ProcessedData/test.csv')

## just a regular decision tree
def DecTreeModel(dftrain, dftest, columnlist):
    clf = tree.DecisionTreeClassifier()

    X = dftrain[columnlist]
    y = dftrain['is_duplicate']

    clf.fit(X,y)

    return clf.predict(dftest[columnlist])

## runs our final model, currently a decision tree
## with just one feature, jaccard score
def model(dftrain, dftest):
    dftest['is_duplicate'] = DecTreeModel(dftrain, dftest, ['jaccard'])

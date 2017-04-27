## Anything that takes in features and outputs a guess
import pandas as pd
#import xgboost as xgb
from sklearn.model_selection import train_test_split
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

##
#def xgboost(dftrain, dftest, columnlist):
#    params = {}
#    params['objective'] = 'binary:logistic'
#    params['eval_metric'] = 'logloss'
#    params['eta'] = 0.02
#    params['max_depth'] = 4

#    dftrain1, dfval = train_test_split(X, test_size=0.33, random_state=42)

#    d_train = xgb.DMatrix(dftrain1, label = y_train)
#    d_valid = xgb.Dmatrix(x_valid, label = y_valid)
#    watchlist = [(d_train, 'train'), (d_valid, 'valid')]
#    bst = xgb.train(params, d_train, 400, watchlist, early_stopping_rounds=50, verbose_eval=10)
#    d_test = xgb.DMatrix(x_test)
#    return bst.predict(dftest)


## runs our final model, currently a decision tree
## with just one feature, jaccard score
def model(dftrain, dftest):
    dftest['is_duplicate'] = DecTreeModel(dftrain, dftest, ['jaccard'])
   # dftest['is_duplicate'] = xgboost(dftrain, dftest, ['jaccard'])

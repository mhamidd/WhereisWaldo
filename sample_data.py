import pandas as pd
import random
import csv
train_data = pd.read_csv('tweet_reg_train.csv')
rows = random.sample(train_data.index, 50000)
train_short = train_data.ix[rows]
train_short.columns = ['User', 'Tweet', 'Region', 'Fold']
#delete fold column
del train_short['Fold']
train_short.to_csv('short_train.csv', header=True)

test_data = pd.read_csv('tweet_reg_test.csv')
rows = random.sample(test_data.index, 10000)
test_short = test_data.ix[rows]
test_short.columns = ['User', 'Tweet', 'Region', 'Fold']
del test_short['Fold']
test_short.to_csv('short_test.csv', header=True)
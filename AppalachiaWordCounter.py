import numpy as np
import pandas as pd
from scipy import sparse
from sklearn.base import BaseEstimator

class AppalachiaWordCounter(BaseEstimator):
	#open North words list
	def __init__(self):
		with open("appalachia_words.csv") as f:
			appalachia_words = [l.strip() for l in f.readlines()]
		self.appalachia_words_ = appalachia_words

	def transform(self, documents):
		list = []
		for c in documents:
			sum_list = []
			
			for w in self.appalachia_words_:
			     #print w, " occurs ", str(c).lower().count(w), "times in ", str(c)
			     numOccur = [np.sum(str(c).lower().count(w))]
			     if (numOccur == None):
			         numOccur = []
			     
			     print sum_list.append(numOccur)
			list.append([np.sum(sum_list)])
			
		print "Here's the List: ", list
		return list
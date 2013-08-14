#script to get number of words in tweet
#get number of regional words in tweet
#save list of number regional words/tweet
import numpy as np
from scipy import sparse
from sklearn.base import BaseEstimator
 
class NEWordCounter(BaseEstimator): #not actually sure why the class takes the estimator as its arg
#open New England words list, save each word as newline
	def __init__(self):
		with open("ne_words.csv") as f:
			ne_words = [l.strip() for l in f.readlines()]
		self.ne_words_ = ne_words
		
	def transform(self, documents):
#split doc by words, get length
		n_words = [len(c) for c in documents]
#number of New England words:
		ne_words = [np.sum([c.lower().count(w) for w in self.ne_words_])for c in documents]
		return np.array([ne_words])        

class MAWordCounter(BaseEstimator):
	#open Mid Atlantic words list
	def __init__(self):
		with open("mid_atlantic_words.csv") as f:
			ma_words = [l.strip() for l in f.readlines()]
		self.ma_words_ = ma_words       

	def transform(self, documents):
	#get total words
		n_words = [len(c) for c in documents]
	# number of Mid Atlantic words:
		ma_words = [np.sum([c.lower().count(w) for w in self.ma_words_])for c in documents]

		return np.array([ma_words]) 

class SouthWordCounter(BaseEstimator):
	#open South words list
	def __init__(self):
		with open("south_words.csv") as f:
			south_words = [l.strip() for l in f.readlines()]
		self.south_words_ = south_words

	def transform(self, documents):
	#get total words
		n_words = [len(c) for c in documents]
	# number of Southern words:
		south_words = [np.sum([c.lower().count(w) for w in self.north_words_])for c in documents]

		return np.array([south_words]) 

class NorthWordCounter(BaseEstimator):
	#open North words list
	def __init__(self):
		with open("north_words.csv") as f:
			north_words = [l.strip() for l in f.readlines()]
		self.north_words_ = north_words   

	def transform(self, documents):
	#get total words
		n_words = [len(c.split()) for c in documents]
	# number of Northern words:
		north_words = [np.sum([c.lower().count(w) for w in self.north_words_])for c in documents]

		return np.array([north_words]) 

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
				print sum_list.append([np.sum(c.lower().count(w))])
			list.append([np.sum(sum_list)])

class MidlandWordCounter(BaseEstimator):
	#open North words list
	def __init__(self):
		with open("midland_words.csv") as f:
			midland_words = [l.strip() for l in f.readlines()]
		self.midland_words_ = midland_words

	def get_feature_names(self):
		return np.array(['n_words', 'midland_words', 'midland_ratio'])

	def fit(self, documents, y=None):
		return self                

	def transform(self, documents):
	#get total words
		n_words = [len(c.split()) for c in documents]
	# number of Northern words:
		midland_words = [np.sum([c.lower().count(w) for w in self.midland_words_])for c in documents]
	#ratio of Southern words to total words
		reg_ratio = np.array(midland_words) / np.array(n_words, dtype=np.float)

		return np.array([n_words, midland_words, midland_ratio]) 				

class SouthWestWordCounter(BaseEstimator):
	#open Southwestern words list
	def __init__(self):
		with open("southwest_words.csv") as f:
			southwest_words = [l.strip() for l in f.readlines()]
		self.southwest_words_ = southwest_words

	def get_feature_names(self):
		return np.array(['n_words', 'southwest_words', 'southwest_ratio'])

	def fit(self, documents, y=None):
		return self                

	def transform(self, documents):
	#get total words
		n_words = [len(c.split()) for c in documents]
	# number of Southwestern words:
		southwest_words = [np.sum([c.lower().count(w) for w in self.southwest_words_])for c in documents]
	#ratio of Southwestern words to total words
		reg_ratio = np.array(southwest_words) / np.array(n_words, dtype=np.float)

		return np.array([n_words, southwest_words, southwest_ratio]) 

class NorthWestCounter(BaseEstimator):
	#open Northwestern words list
	def __init__(self):
		with open("northwest_words.csv") as f:
			northwest_words = [l.strip() for l in f.readlines()]
		self.northwest_words_ = northwest_words

	def get_feature_names(self):
		return np.array(['n_words', 'northwest_words', 'northwest_ratio'])

	def fit(self, documents, y=None):
		return self                

	def transform(self, documents):
	#get total words
		n_words = [len(c.split()) for c in documents]
	# number of Northwestern words:
		northwest_words = [np.sum([c.lower().count(w) for w in self.northwest_words_])for c in documents]
	#ratio of Northwestern words to total words
		reg_ratio = np.array(northwest_words) / np.array(n_words, dtype=np.float)

		return np.array([n_words, northwest_words, northwest_ratio]) 

class PacWestWordCounter(BaseEstimator):
	#open PacificWest words list
	def __init__(self):
		with open("pacific_words.csv") as f:
			pacific_words = [l.strip() for l in f.readlines()]
		self.pacific_words_ = pacific_words

	def get_feature_names(self):
		return np.array(['n_words', 'pacific_words', 'pacific_ratio'])

	def fit(self, documents, y=None):
		return self                

	def transform(self, documents):
	#get total words
		n_words = [len(c.split()) for c in documents]
	# number of pacific words:
		pacific_words = [np.sum([c.lower().count(w) for w in self.northwest_words_])for c in documents]
	#ratio of pacific words to total words
		reg_ratio = np.array(pacific_words) / np.array(n_words, dtype=np.float)

		return np.array([n_words, pacific_words, pacific_ratio]) 

class DelmarvaWordCounter(BaseEstimator):
	#open delmarva words list
	def __init__(self):
		with open("delmarva_words.csv") as f:
			delmarva_words = [l.strip() for l in f.readlines()]
		self.delmarva_words_ = delmarva_words

	def get_feature_names(self):
		return np.array(['n_words', 'delmarva_words', 'delmarva_ratio'])

	def fit(self, documents, y=None):
		return self                

	def transform(self, documents):
	#get total words
		n_words = [len(c.split()) for c in documents]
	# number of delmarva words:
		delmarva_words = [np.sum([c.lower().count(w) for w in self.delmarva_words_])for c in documents]
	#ratio of delmarva words to total words
		reg_ratio = np.array(delmarva_words) / np.array(n_words, dtype=np.float)

		return np.array([n_words, delmarva_words, delmarva_ratio]) 


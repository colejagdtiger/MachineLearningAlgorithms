import numpy as np


class KMeans(object):

	def __init__(self, k, high, low):
		"""
		implementation of k-means algorithm
		k = number of clusters
		high = largest possible cluster initial value
		low = smallest possible cluster initial value
		"""
		self.cluster_centroids = np.random.rand(k, dtype='float64') * high - low

	def fitTrainingSet(training_set):
		"""
		fits clusters to training set, training set is expected to be
		a numpy array of dimension n+1 where a given training sample
		is of dimension n
		"""
		

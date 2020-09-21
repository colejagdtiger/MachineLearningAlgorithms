
class KMeans(object):

	def __init__(self, k):
		"""
		implementation of k-means algorithm
		k = number of clusters
		"""
		self.k = k

	def fitTrainingSet(training_set):
		"""
		fits clusters to training set, training set is expected to be
		a numpy array of dimension n+1 where a given training sample
		is of dimension n
		"""
		
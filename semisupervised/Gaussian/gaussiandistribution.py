"""
	Gaussian distribution, used for anomaly detection

	algo still needs testing to ensure that it works as intended
"""
import numpy as np


class Gaussian(object):

	def __init__(self, feature_num, epsilion=0.05):
	"""
		feature_num = number of features of data feed to classifier
		epsilion = 'probability value', if data point is found to
		lie on a lower probability location than this value, an
		data anomaly will be flagged for that point
	"""
	self.mean_para = np.array(feature_num)
	self.vari_para = np.array(feature_num)


	def fitModel(self, data_set):
	"""
       data_set = numpy array, dimensions [data_set_size, feature_number]
       contains data to fit algorithm on
	"""
		data_size = len(data_set)
		self.mean_para = np.sum(data_set, axis=0) / data_size
		mse = (data_set - self.mean_para)**2
		self.vari_para = np.sum(mse, axis=0) / data_size

	def evalData(self, data_set):
	"""
       data_set = numpy array, dimensions [data_set_size, feature_number]
       contains data to fit algorithm on
	"""
	   


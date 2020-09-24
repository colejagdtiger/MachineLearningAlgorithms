import numpy

class Bias(numpy.ndarray):

	def __init__(self, size):
		super().__init__(size)
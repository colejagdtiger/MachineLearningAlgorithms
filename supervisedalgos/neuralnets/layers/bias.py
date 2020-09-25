import numpy as np

class Bias(np.ndarray):

	def __init__(self, size):
		super().__init__(size)
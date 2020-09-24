import numpy as np

class ClusterCentroid(np.ndarray):

    def __init__(self, dim, high=1, low=-1):
        Super().__init__(dim)
        self.reach = 0
import torch
from torch.autograd import Variable
import numpy as np


class Nmf(object):
    """
    Compute non-negative matrix factorization of a non-negative matrix A into W and H.

    The columns of W represent the basis vectors and H the coefficients.

    Args
    ----
    - A: numpy array of shape (m,n)
    - rank: rank of W matrix

    Returns
    -------
    - W: non-negative matrix of shape (m,k)
    - H: non-negative matrix of shape (k,n)
    """

    def __init__(self, A, rank, eta, beta,  W=None, H=None, max_iter=100):
        self.A = Variable(torch.FloatTensor(A), requires_grad=True)
        self.rank = rank
        self.eta = eta
        self.beta = beta
        self.max_iter = max_iter

        self.W = Variable(torch.rand(), requires_grad=True)
        self.H = Variable(torch.rand(), requires_grad=True)

        if np.any(A < 0):
            print('Error: A must be non-negative')

    def factorize(self):


        return self.W, self.H

    def loss(self):
        return

    def penalize(self):
        return

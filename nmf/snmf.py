import torch
from torch.autograd import Variable
import numpy as np


class Snmf(object):
    """
    Compute sparse non-negative matrix factorization of a non-negative matrix A into W and H.

    The columns of W represent the basis vectors and H the coefficients.

    Args
    ----
    - A: numpy array of shape (m,n)
    - rank: rank of W matrix
    - eta: controls size of elements of W
    - beta:  control trade-off between accuracy of approximation and sparseness of H

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

        self.W = Variable(torch.rand(), requires_grad=False)
        self.H = Variable(torch.rand(), requires_grad=False)

        if np.any(A < 0):
            print('Error: A must be non-negative')

    def factorize(self):
        """
        Compute matrix factorization
        :return: fitted matrix factorization model
        """

        # Create optimizers
        opt_w = torch.optim.Adam()
        opt_h = torch.optim.Adam()

        for i in range(self.max_iter):
            self.min_h()
            self.min_w()

            # Report loss
            if i % 10 == 0:
                self.report()

        return self.W, self.H

    def min_h(self):
        """
        Minimize nonnegativity constrained least squares problem for H
        :return:
        """

    def min_w(self):
        """
        Minimize nonnegativity constrained least squares problem for W
        :return:
        """

    def loss(self):
        """
        Calculate loss for current matrix factorization
        :return: loss as defined by Kim and Park
        """

    def report(self):
        """
        Print loss for current iteration
        """
        print((self.A - self.W.mm(self.H.t())).norm(2).item())

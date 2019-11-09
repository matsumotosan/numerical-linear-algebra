import numpy as np
import torch
from torch.autograd import Variable
from sklearn.preprocessing import normalize


class Cnmf():
    def __init__(self, A, rank, alpha, beta, lr, rtol=1e-5, max_iter=100):
        self.A = Variable(torch.FloatTensor(A), requires_grad=False)
        self.rank, self.alpha, self.beta, self.lr, self.rtol, self.max_iter = rank, alpha, beta, lr, rtol, max_iter
        self.m, self.n = self.A.shape
        self.W = Variable(torch.FloatTensor(normalize(np.random.rand(self.m, self.rank))), requires_grad=True)
        self.H = Variable(torch.FloatTensor(normalize(np.random.rand(self.rank, self.n))), requires_grad=True)
        self.opt = torch.optim.Adam([self.W, self.H], lr=self.lr)

    def factorize(self):
        for i in range(self.max_iter):
            self.opt.zero_grad()

            # calculate loss
            l = self.loss()

            # calculate gradient through back propagation
            l.backward()

            # optimize W and H
            self.opt.step()

            # test convergence
            # if converged():
            #     return
        return self.W.data, self.H.data

    def loss(self):
        return (torch.norm(self.A - torch.mm(self.W, self.H)).pow(2) +
                self.alpha * torch.norm(self.W).pow(2) +
                self.beta * torch.norm(self.H).pow(2)) / 2 + self.penalize() * 1e6

    def penalize(self):
        return self.penalty(self.W).mean() + self.penalty(self.H).mean()

    def penalty(self, m):
        return torch.pow((m < 0).type(torch.FloatTensor) * torch.clamp(m, max=0.), 2)

    def converged(self):
        return torch.allclose(self.A, torch.mm(self.W, self.H), rtol=self.rtol)

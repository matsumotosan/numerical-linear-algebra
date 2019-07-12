from numpy import sum, exp, sqrt, abs, sin, cos, prod, zeros_like
from math import pi

"""
Library of functions commonly used to test optimization algorithms.
Original work by Derek Bingham in MATLAB and R translated in Python.
https://www.sfu.ca/~ssurjano/optimization.html
"""


def ackley(x, a=20, b=0.2, c=2*pi, n=2):

    s1 = sum(x ** 2, axis=-1)
    s2 = sum(cos(c * x), axis=-1)

    return -a * exp(-b * sqrt(s1 / n)) - exp(s2 / n) + a + exp(1)


def bukin(x):

    return 100 * sqrt(abs(x[:,:,1] - 0.01 * x[:,:,0] ** 2)) + 0.01 * abs(x[:,:,0] + 10)


def cross_in_tray(x):

    return -0.0001 * (abs(sin(x[:,:,0]) * sin(x[:,:,1]) * exp(100 - sqrt(sum(x ** 2, axis=-1)) / pi)) + 1) ** 0.1


def dropwave(x):

    return -(1+cos(12 * sqrt(sum(x ** 2, axis=-1)))) / (0.5 * sum(x ** 2, axis=-1)+2)


def eggholder(x):

    return -(x[:,:,1] + 47) * sin(sqrt(abs(x[:,:,1] + x[:,:,0] / 2 + 47))) - x[:,:,0] * sin(sqrt(abs(x[:,:,0] - (x[:,:,1] + 47))))


def gramacylee(x):

    return sin(10 * pi * x) / (2 * x) + (x - 1) ** 4


# incomplete
def griewank(x):

    s = sum((x ** 2) / 4000, axis=-1)
    p = prod([cos(x[..., i] / sqrt(i)) for i in range(x.shape[-1])], axis=-1)

    return s - p + 1


def holdertable(x):

    s = abs(1 - sqrt(sum(x ** 2, axis=-1)) / pi)

    return -abs(sin(x[:,:,0]) * cos(x[:,:,1]) * exp(s))


# incomplete
def langermann():

    return


# incomplete
def levy():

    return


def levy13(x):

    return sin(3 * pi * x[:,:,0]) ** 2 + (x[:,:,0] - 1) ** 2 * (1 + sin(3 * pi * x[:,:,1]) ** 2) + (x[:,:,1] - 1) ** 2 * (1 + sin(2 * pi * x[:,:,1]) ** 2)


def rastrigin():

    return


def schaeffer2():

    return


def schaeffer4():

    return


def schewfel():

    return


def shubert():

    return


def rosenbrock(x):

    s = zeros_like(x[...,0])
    for i in range(x.shape[-1] - 1):
        s += 100 * (x[..., i + 1] - x[..., i] ** 2) ** 2 + (x[..., i] - 1) ** 2

    return s


def beale(x):

    s1 = (1.5 - x[:,:,0] + x[:,:,0] * x[:,:,1]) ** 2
    s2 = (2.25 - x[:,:,0] + x[:,:,0] * x[:,:,1] ** 2) ** 2
    s3 = (2.625 - x[:,:,0] + x[:,:,0] * x[:,:,1] ** 3) ** 2

    return s1 + s2 + s3

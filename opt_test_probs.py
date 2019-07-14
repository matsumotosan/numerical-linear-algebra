from numpy import sum, diff, multiply, exp, sqrt, abs, sin, cos, prod, zeros_like
from math import pi

"""
Library of functions commonly used to test optimization algorithms.
Original work by Derek Bingham in MATLAB and R translated in Python.
https://www.sfu.ca/~ssurjano/optimization.html
"""


# Many local minima
def ackley(x, a=20, b=0.2, c=2*pi, n=2):

    s1 = sum(x ** 2, axis=-1)
    s2 = sum(cos(c * x), axis=-1)

    return -a * exp(-b * sqrt(s1 / n)) - exp(s2 / n) + a + exp(1)


def bukin(x):

    return 100 * sqrt(abs(x[:,:,1] - 0.01 * x[:,:,0] ** 2)) + 0.01 * abs(x[:,:,0] + 10)


def cross_in_tray(x):

    return -0.0001 * (abs(sin(x[:,:,0]) * sin(x[:,:,1]) * exp(100 - sqrt(sum(x ** 2, axis=-1)) / pi)) + 1) ** 0.1


def dropwave(x):

    return -(1 + cos(12 * sqrt(sum(x ** 2, axis=-1)))) / (0.5 * sum(x ** 2, axis=-1)+2)


def eggholder(x):

    return -(x[:,:,1] + 47) * sin(sqrt(abs(x[:,:,1] + x[:,:,0] / 2 + 47))) - x[:,:,0] * sin(sqrt(abs(x[:,:,0] - (x[:,:,1] + 47))))


def gramacylee(x):

    return sin(10 * pi * x) / (2 * x) + (x - 1) ** 4


def griewank(x): # incomplete

    s = sum((x ** 2) / 4000, axis=-1)
    p = prod([cos(x[..., i] / sqrt(i)) for i in range(x.shape[-1])], axis=-1)

    return s - p + 1


def holdertable(x):

    s = abs(1 - sqrt(sum(x ** 2, axis=-1)) / pi)

    return -abs(sin(x[:,:,0]) * cos(x[:,:,1]) * exp(s))


def langermann(): # incomplete

    return


def levy(): # incomplete

    return


def levy13(x):

    return sin(3 * pi * x[:,:,0]) ** 2 + (x[:,:,0] - 1) ** 2 * (1 + sin(3 * pi * x[:,:,1]) ** 2) + (x[:,:,1] - 1) ** 2 * (1 + sin(2 * pi * x[:,:,1]) ** 2)


def rastrigin(x):

    return 10 * x.shape[-1] + sum(x ** 2 - 10 * cos(2 * pi * x), axis=-1)


def schaffer2(x):

    num = sin(diff(x ** 2, axis=-1)) ** 2 - 0.5
    den = (1 + 0.001 * (sum(x ** 2, axis=-1))) ** 2

    return 0.5 + num / den


def schaffer4(x):

    num = cos(sin(abs(diff(x, axis=-1)))) - 0.5
    den = (1 + 0.001 * sum(x ** 2, axis=-1)) ** 2

    return 0.5 + num / den


def schwefel(x): # not sure if correct

    return 418.9829 * x.ndim - sum(multiply(x, sin(sqrt(abs(x)))), axis=-1)


def shubert(x):

    # s1 = s2 = zeros_like(x[:,:,0])
    s1 = [multiply(i, cos((i + 1) * x[:,:,0] + i)) for i in range(1, 6)]
    s2 = [multiply(i, cos((i + 1) * x[:,:,1] + i)) for i in range(1, 6)]

    return multiply(sum(s1, axis=0), sum(s2, axis=0))


# Bowl-shaped

def bohachevsky(x, no=1):

    if no == 1:
        return x[:,:,0] ** 2 + 2 * x[:,:,1] ** 2 - 0.3 * cos(3 * pi * x[:,:,0]) - 0.4 * cos(4 * pi * x[:,:,1]) + 0.7
    elif no == 2:
        return x[:,:,0] ** 2 + 2 * x[:,:,1] ** 2 - 0.3 * cos(3 * pi * x[:,:,0]) * cos(4 * pi * x[:,:,1]) + 0.3
    elif no == 3:
        return x[:,:,0] ** 2 + 2 * x[:,:,1] ** 2 - 0.3 * cos(3 * pi * x[:,:,0] + 4 * pi * x[:,:,1]) + 0.3
    else:
        return None


def perm(x):

    return


def rot_hypellip(x): # incomplete

    # z = zeros_like(x[:,:,0])
    # for i in range(x.ndim):
    #     z +=
    #
    return


def sphere(x):

    return sum(x ** 2, axis=-1)


def sumdiffpow(x): # incorrect

    return sum([abs(x[:,:,i]) ** (i + 2) for i in range(x.ndim - 1)], axis=-1)


def sumsq(x):

    return


def trid(x):

    return


## Plate-shaped
def booth(x):

    return (x[:,:,0] + 2 * x[:,:,1] - 7) ** 2 + (2 * x[:,:,0] + x[:,:,1] - 5) ** 2


def matyas(x):

    return 0.26 * sum(x ** 2, axis=-1) - 0.48 * prod(x, axis=-1)


def mccormick(x):

    return sin(sum(x, axis=-1)) + diff(x, axis=0) ** 2 - 1.5 * x[:,:,0] + 2.5 * x[:,:,1] + 1


def powersum(x):

    return


def zakharov(x):

    return


# Valley-shaped
def camel_3(x):

    return 2 * x[:,:,0] ** 2 - 1.05 * x[:,:,0] ** 4 + (x[:,:,0] ** 6) / 6 + prod(x, axis=-1) + x[:,:,1] ** 2


def camel_6(x):

    s1 = (4 - 2.1 * x[:,:,0] ** 2 + x[:,:,0] ** 4 / 3) * x[:,:,0] ** 2
    s2 = (-4 + 4 * x[:,:,1] ** 2) * x[:,:,1] ** 2

    return s1 + prod(x, axis=-1) + s2


def dixonprice(x):

    s = zeros_like(x[:,:,0])
    for i in range(1, x.ndim - 1):
        s += (i + 1) * (2 * x[:,:,i] ** 2 - x[:,:,i - 1]) ** 2

    return (x[:,:,0] - 1) ** 2 + s


def rosenbrock(x):

    s = zeros_like(x[...,0])
    for i in range(x.shape[-1] - 1):
        s += 100 * (x[..., i + 1] - x[..., i] ** 2) ** 2 + (x[..., i] - 1) ** 2

    return s


## Steep ridges/drops
def dejong(x):

    return


def easom(x):

    return


def michalewicz(x):

    return


# Other
def beale(x):

    s1 = (1.5 - x[:,:,0] + x[:,:,0] * x[:,:,1]) ** 2
    s2 = (2.25 - x[:,:,0] + x[:,:,0] * x[:,:,1] ** 2) ** 2
    s3 = (2.625 - x[:,:,0] + x[:,:,0] * x[:,:,1] ** 3) ** 2

    return s1 + s2 + s3


def branin(x):

    return


def colville(x):

    return


def forrester(x):

    return


def goldsteinprice(x):

    return


def hartmann3(x):

    return


def hartmann4(x):

    return


def hartmann6(x):

    return


def powell(x):

    return


def shekel(x):

    return


def stytang(x):

    return sum(x ** 4 - 16 * x ** 2 + 5 * x, axis=-1) / 2

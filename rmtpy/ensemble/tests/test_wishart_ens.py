import pytest

import numpy as np
from numpy.testing import (
    assert_almost_equal,
    assert_array_equal,
    assert_allclose,
)

from rmtpy.ensemble import WishartReal, WishartComplex, WishartQuaternion


##########################################
### Wishart Real Ensemble = WRE

def test_wishartReal_init():
    P = 3
    N = 5

    np.random.seed(1)
    wr = WishartReal(p=P, n=N)

    assert(wr.matrix.shape == (P,P))

    assert_almost_equal(wr.matrix, np.array([[5.1919012, -4.96197148, 5.1988152],
                                            [-4.96197148, 9.08485594, -7.11948641],
                                            [5.1988152, -7.11948641, 7.91882311]]),
                        decimal=4)


def test_wre_symmetric():
    P = 3
    N = 5
    wr = WishartReal(p=P, n=N)

    M = wr.matrix
    assert((M.transpose() == M).all() == True)


def test_wre_set_size():
    P1, N1 = 3, 5
    P2, N2 = 4, 6

    ens = WishartReal(p=P1, n=N1)
    assert(ens.p == P1)
    assert(ens.n == N1)
    assert(ens.matrix.shape == (P1,P1))

    ens.set_size(p=P2, n=N2, resample_mtx=False)
    assert(ens.p == P2)
    assert(ens.n == N2)
    assert(ens.matrix.shape == (P1,P1))

    ens.set_size(p=P2, n=N2, resample_mtx=True)
    assert(ens.p == P2)
    assert(ens.n == N2)
    assert(ens.matrix.shape == (P2,P2))


##########################################
### Wishart Complex Ensemble = WCE

def test_wishartComplex_init():
    P = 3
    N = 8

    np.random.seed(1)
    wc = WishartComplex(p=P, n=N)

    assert(wc.matrix.shape == (P,P))

    assert_almost_equal(wc.matrix, np.array([[10.95414504+1.18652432j, 6.49496169+2.33465966j, -0.41256652-0.97218795j],
                                            [6.49496169+2.33465966j, 3.04633885+0.74413531j, -3.62175065-2.09216231j],
                                            [-0.41256652-0.97218795j, -3.62175065-2.09216231j, -4.3742556 +4.41905659j]]),
                        decimal=4)


def test_wce_symmetric():
    P = 3
    N = 5
    wc = WishartComplex(p=P, n=N)

    M = wc.matrix
    assert((M.transpose() == M).all() == True)


def test_wce_set_size():
    P1, N1 = 5, 10
    P2, N2 = 7, 14

    ens = WishartComplex(p=P1, n=N1)
    assert(ens.p == P1)
    assert(ens.n == N1)
    assert(ens.matrix.shape == (P1,P1))

    ens.set_size(p=P2, n=N2, resample_mtx=False)
    assert(ens.p == P2)
    assert(ens.n == N2)
    assert(ens.matrix.shape == (P1,P1))

    ens.set_size(p=P2, n=N2, resample_mtx=True)
    assert(ens.p == P2)
    assert(ens.n == N2)
    assert(ens.matrix.shape == (P2,P2))



##########################################
### Wishart Quaternion Ensemble = WQE

def test_wishartQuatern_init():
    P = 2
    N = 5

    np.random.seed(1)
    wq = WishartQuaternion(p=2, n=5)

    assert(wq.matrix.shape == (2*P,2*P))

    assert_almost_equal(wq.matrix, np.array([[-6.01217359e-01+7.71388293j, -2.91531515e+00-6.39395501j, 8.10811919e-17+6.4759398j, 2.16853073e+00-0.3065013j],
                                             [-2.91531515e+00-6.39395501j, 3.83549752e+00+5.28492599j, -2.16853073e+00-0.3065013j, -1.30942157e-16-7.29353772j],
                                             [8.10811919e-17+6.4759398j, -2.16853073e+00-0.3065013j, -6.01217359e-01-7.71388293j, -2.91531515e+00+6.39395501j],
                                             [2.16853073e+00-0.3065013j, -1.30942157e-16-7.29353772j, -2.91531515e+00+6.39395501j, 3.83549752e+00-5.28492599j]]),
                        decimal=4)

                
def test_wqe_symmetric():
    P = 3
    N = 5
    wq = WishartQuaternion(p=P, n=N)

    M = wq.matrix
    assert((M.transpose() == M).all() == True)
                    

def test_wqe_set_size():
    P1, N1 = 2, 3
    P2, N2 = 4, 5

    ens = WishartQuaternion(p=P1, n=N1)
    assert(ens.p == P1)
    assert(ens.n == N1)
    assert(ens.matrix.shape == (2*P1,2*P1))

    ens.set_size(p=P2, n=N2, resample_mtx=False)
    assert(ens.p == P2)
    assert(ens.n == N2)
    assert(ens.matrix.shape == (2*P1,2*P1))

    ens.set_size(p=P2, n=N2, resample_mtx=True)
    assert(ens.p == P2)
    assert(ens.n == N2)
    assert(ens.matrix.shape == (2*P2,2*P2))

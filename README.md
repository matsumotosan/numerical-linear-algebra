# Numerical Linear Algebra
Jupyter notebooks on concepts from numerical/computational linear algebra.
Inspired by [Professor Rachel Thomas' class on computational linear algebra](https://www.youtube.com/playlist?list=PLtmWHNX-gukIc92m1K0P6bIOnZb-mg0hY).

## Topics covered
* Truncated SVD
* Non-negative matrix factorization (NMF) and sparse NMF
* Principal component analysis (PCA)
* Lp-spaces and p-norms (Lp-spaces incomplete)
* Preconditioners
  * Jacobi method
  * Cholesky factorization
  * LDL factorization
  * Successive over-relaxation (SOR)
  * Symmetric successive over-relaxation (SSOR)
  * Incomplete LU factorization
* Eigenvalue algorithms
  * Inverse iteration
  * Rayleigh quotient iteration

## Topics to be covered
* Preconditioners
* Eigenvalue algorithms
  * Divide-and-conquer eigenvalue algorithm (Cuppen) (in progress)
* Krylov subspaces
* Gauss-Legendre quadrature
* Conjugate gradient
* Power Method with shifts and deflation
* QR algorithm with Wilkinson shifts
* Golub-Kahan bidiagonalization with Householder reflectors
* GMRES (generalized minimal residual)
* Monte Carlo methods
* Lanczos algorithm
* *k*-means and *c*-means clustering

## Creating Conda environment
1. conda env create -f environment.yml
2. conda activate num-lin-alg

## Resources
[fast.ai Computational Linear Algebra course](https://www.fast.ai/2017/07/17/num-lin-alg/)
[Matrix Computations by Gene H. Golub and Charles F. Van Loan (4th Ed.)](https://www.amazon.com/Computations-Hopkins-Studies-Mathematical-Sciences/dp/1421407949)

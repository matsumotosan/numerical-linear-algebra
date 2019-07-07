# Numerical Linear Algebra
Jupyter notebooks on concepts from numerical/computational linear algebra.
Inspired by [Professor Rachel Thomas' class on computational linear algebra](https://www.youtube.com/playlist?list=PLtmWHNX-gukIc92m1K0P6bIOnZb-mg0hY).

## Topics
- [x] SVD and truncated SVD
- [x] Non-negative matrix factorization (NMF) and sparse NMF
- [x] Principal component analysis (PCA) and robust PCA
- [] QR factorization
  - [] QR algorithm with Wilkinson shifts
- [x] p-norms
- [] Lp-spaces
- [] Preconditioners
  - [x] Jacobi
  - [x] Gauss-Seidel
  - [x] Cholesky factorization
  - [x] Incomplete Cholesky with zero-fill (IC(0))
  - [] Incomplete Cholesky with threshold dropping (ICT)
  - [x] LDL factorization
  - [x] Successive over-relaxation (SOR)
  - [] Symmetric successive over-relaxation (SSOR)
  - [] Incomplete LU factorization (ILU)
  - [] Sparse approximate inverse (SPAI)
  - [] MR algorithm
- [] Eigenvalue algorithms
  - [] Power iteration
  - [] Inverse iteration
  - [] Rayleigh quotient iteration
  - [] Arnoldi iteration
  - [] Lanczos algorithm
  - [] Cuppen's divide-and-conquer eigenvalue algorithm
- [] Conjugate gradient method
- [] Krylov subspaces
- [] Gauss-Legendre quadrature
- [] Power Method with shifts and deflation
- [] Golub-Kahan bidiagonalization with Householder reflectors
- [] GMRES (generalized minimal residual)
- [] Monte Carlo methods
- [] Lanczos algorithm
- [] *k*-means and *c*-means clustering

## Possible future topics
  * [PyTorch optimization algorithms](https://pytorch.org/docs/stable/optim.html)

## Creating Conda environment
1. conda env create -f environment.yml
2. conda activate num-lin-alg

## Resources
[fast.ai Computational Linear Algebra course](https://www.fast.ai/2017/07/17/num-lin-alg/)
[Numerical Linear Algebra by Lloyd N. Trefethen and David Bau III](https://www.amazon.com/Numerical-Linear-Algebra-Lloyd-Trefethen/dp/0898713617)
[Matrix Computations by Gene H. Golub and Charles F. Van Loan (4th Ed.)](https://www.amazon.com/Computations-Hopkins-Studies-Mathematical-Sciences/dp/1421407949)

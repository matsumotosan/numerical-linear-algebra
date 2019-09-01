# Numerical Linear Algebra
Jupyter notebooks on concepts from numerical/computational linear algebra.
Inspired by [Professor Rachel Thomas' class on computational linear algebra](https://www.youtube.com/playlist?list=PLtmWHNX-gukIc92m1K0P6bIOnZb-mg0hY).

## Topics
- [x] SVD
  - [x] Truncated SVD
- [x] Non-negative matrix factorization (NMF)
  - [x] Sparse NMF
- [x] Principal component analysis (PCA)
  -[x] Robust PCA
- [ ] *k*-means clustering
- [ ] *c*-means clustering
- [ ] QR factorization
  - [ ] QR algorithm with Wilkinson shifts
- [x] p-norms
- [ ] Lp-spaces
- [ ] Regularization
- [ ] Preconditioners
  - [x] Jacobi
  - [x] Gauss-Seidel
  - [x] Cholesky factorization
  - [x] Incomplete Cholesky with zero-fill (IC(0))
  - [ ] Incomplete Cholesky with threshold dropping (ICT)
  - [x] LDL factorization
  - [x] Successive over-relaxation (SOR)
  - [ ] Symmetric successive over-relaxation (SSOR)
  - [ ] Incomplete LU factorization (ILU)
  - [ ] Sparse approximate inverse (SPAI)
  - [ ] MR algorithm
- [ ] Eigenvalue algorithms
  - [x] Power iteration
  - [ ] Power method with shifts and deflation
  - [x] Inverse iteration
  - [ ] Rayleigh quotient iteration
  - [ ] Arnoldi iteration
  - [ ] Lanczos algorithm
  - [ ] Cuppen's divide-and-conquer eigenvalue algorithm
- [x] Conjugate gradient method
- [ ] Krylov subspaces
- [ ] Generalized minimal residual method (GMRES)
- [ ] Gauss-Legendre quadrature
- [ ] Golub-Kahan bidiagonalization with Householder reflectors
- [ ] Monte Carlo methods
- [ ] Lanczos algorithm
- [ ] T-distributed stochastic neighbor embedding (t-SNE)
- [x] Optimization test problems
- [ ] Convex optimization

## Possible future topics
- [PyTorch optimization algorithms](https://pytorch.org/docs/stable/optim.html)
- Graduated optimization

## Creating Conda environment
```
conda env create -f environment.yml
conda activate linalg
```

## Resources
[fast.ai Computational Linear Algebra course](https://www.fast.ai/2017/07/17/num-lin-alg/)

[Numerical Linear Algebra by Lloyd N. Trefethen and David Bau III](https://www.amazon.com/Numerical-Linear-Algebra-Lloyd-Trefethen/dp/0898713617)

[Matrix Computations by Gene H. Golub and Charles F. Van Loan](https://www.amazon.com/Computations-Hopkins-Studies-Mathematical-Sciences/dp/1421407949)

[Iterative Methods for Sparse Linear Systems by Yousef Saad](https://www.amazon.com/Iterative-Methods-Sparse-Linear-Systems/dp/0898715342)

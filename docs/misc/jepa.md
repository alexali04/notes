# JEPA

## CCA

**Canonical Correlation Analysis** is dimensionality reduction - similar to PCA but it simulatenously reduces the dimensions of two random vectors (or datasets) $X, Y$. Instead of trying to maximize variance explained (PCA objective), it tries to maximize $\text{Corr}(X, Y)$. 

Let $X \in \mathbb{R}^{n \times d_x}, Y \in \mathbb{R}^{n \times d_y}$. Here, $n$ is the number of data-points. 

Let $k \leq \min(d_x, d_y, n)$ and $A, B$ be sketching matrices, $A \in \mathbb{R}^{d_x \times k}, B \in \mathbb{R}^{d_y \times k}$. $k$ is the target dimension.

Let $XA = z_x \in \mathbb{R}^{n \times k}, YB = z_y \in \mathbb{R}^{n \times k}$. 

CCA solves the following optimization problem:

$$
\max_{A, B} \text{Tr}(\frac{1}{n} z_x^T z_y)
$$

such that $\frac{1}{n} z_x^T z_k = \frac{1}{n} z_y^T z_y = I$. 

In other words, maximize the trace of the cross-correlation matrix between embeddings such that embeddings have unit variance and zero covariance. 

In PCA, there is a connection between maximizing variance and minimizing prediction error. Similarly, there's a relationship between cross-correlation trace and embedding prediction error.

$$
\frac{1}{n} \sum_{i = 1}^n ||z_x^{(i)} - z_y^{(i)}||^2 = \frac{1}{n} ||z_x - z_y||_F^2
$$

The Frobenius norm of a matrix essentially flattens a matrix into a long vector and finds its standard Euclidean norm. The above equality holds b/c we're takiing the MSE over all data-points between the sketched matrices - which is the same as if we were to flatten the two matrices and take their Frobenius norm. 

NOTE - why?

Then, we have:

$$
= \frac{1}{n} \left (    
\text{Tr}(z_x^T z_x) + \text{Tr}(z_y^T z_y) - 2 \text{Tr}(z_x^T z_y)
\right )
$$

Due to the above constraints, we know that each individual embedding matrix's covariance is $I$. So we have:

$$
= \frac{2k}{n} - \frac{2}{n} \text{Tr}(z_x^T z_y)
$$

Therefore, we can write CCA as:

$$
\min_{A, B} \frac{1}{n} \sum_{i = 1}^n ||z_x^{(i)} - z_y^{(i)}||^2
$$

with unit embedding covariances $\frac{1}{n} z_x^T z_x = \frac{1}{n} z_y^T z_y = I$. 

JEPA is similar to CCA but non-linear and without dimensional constraints (due to the non-linearity) which can result in representational collapse. Techniques like SIGReg are attempts to build in whitening constraints into the induced embeddings from a learned encoder.


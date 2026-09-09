# QR Decomposition

We introduce the tools used in QR-decomposition - outer-products, projectors, and the product of Householder reflectors. These tools are frequently used to compute QR decompositions so we can review this problem as well.

We specifically review choice chapters from the QR-decomposition section of Trefethen & Bau.

## Projectors

!!! info "Definition: Projector"
    A *projector* is a square matrix that satisfies

    $$
    P^2 = P
    $$

    $P$ is also called idempotent. This definition includes both orthogonal and non-orthogonal projectors. Non-orthogonal projectors may be called *oblique projectors*.

As suggested by its name, a projector takes a vector $v$ and projects it onto a certain subspace (kind of like the shadow casted by $v$ on $\text{span}(P)$). Once we have projected $v$ onto $\text{span}(P)$, a secondary projection ought to do nothing, which is why we require that $P^2 = P$. Mathematically,

Suppose $v = Px$. Then,

$$
Pv = P(Px) = P^2x = Px = v
$$

Naturally, $Pv - v \in \text{Ker}(P)$. This is precisely the component of $v$ which is discarded by the projection.

### Complementary Projector

If $P$ is a projector, then $I - P$ is also a projector.

$$
(I - P)^2 = I - 2P + P^2 = I - P
$$

$I - P$ projects on the null-space of $P$. We have that:

!!! tip "Theorem: Image(I - P) = Kernel(P)"

!!! quote "Proof"
    Suppose $v \in \text{Ker}(P), v \neq 0$. Then, $Pv = 0$ and $(I - P)v = v - Pv = v - 0 = v$ so $v \in \text{Image}(I - P)$. Therefore, $\text{Ker}(P) \subseteq \text{Image}(I - P)$.

    Suppose $v \in \text{Image}(I - P)$. Then, $(I - P)v = v - Pv$. However, we know that $P$ maps $v - Pv$ to $0$ so $\text{Image}(I - P) \subseteq \text{Ker}(P)$ (the two spaces are comparable because $P$ is square).

    Therefore, $\text{Image}(I - P) = \text{Ker}(P)$.

Without too much effort, we can show that $\text{Ker}(I - P) = \text{Image}(P)$ as well and that $\text{Image}(P) \bigcap \text{Ker}(P) = \{0\}$.

In short, a projector separates the vector space into two subspaces. Let $S_1, S_2$ be subspaces of $\mathbb{C}^m$ such that $S_1 \bigcap S_2 = \{0\}$ and $\mathbb{C}^m = S_1 \oplus S_2$ (each vector in $\mathbb{C}^m$ can be uniquely expressed as a sum of $s_1 \in S_1$ and $s_2 \in S_2$). The pair $(S_1, S_2)$ is called complementary subspaces. There is a projector $P$ such that $\text{Image}(P) = S_1, \text{Ker}(P) = S_2$. We say that $P$ is a projector onto $S_1$ along $S_2$.

An application: Given $x \in \mathbb{C}^m$, what's the component of $x$ in the direction of a particular eigenvector $v$ of a matrix $A$ (which holds a complete set of eigenvectors)? The answer is $Px$ where $P$ is a particular rank-one projector.

Note that if $P$ is a rank $k$ projector, $I - P$ is a rank $n - k$ projector where $n$ is the number of rows / columns in $P$.

### Orthogonal Projector

!!! info "Definition: Orthogonal Projector"
    An **orthogonal projector** is one which projects onto a subspace $S_1$ along $S_2$ where $S_1, S_2$ are orthogonal.

    Orthogonal projectors don't need to be orthogonal matrices.

!!! tip "Theorem: Orthogonal Projectors are Symmetric"

!!! quote "Proof"
    Let $P$ be an orthogonal projector. We have that

    $$
    \text{Image}(P) \perp \text{Ker}(P)
    $$

    and

    $$
    \text{Image}(P) \perp \text{Image}(I - P)
    $$

    Suppose $Px_1 \neq 0, (I - P)x_2 \neq 0$. Then by orthogonality,

    $$
    (P x_1)^T ((I - P) x_2) = 0
    $$

    $$
    x_1^T P^T (I - P) x_2 = 0
    $$

    $$
    x_1^T P^T x_2  - x_1^T P^T P x_2 = 0
    $$

    $$
    x_1^T P^T x_2 = x_1^T P^T P x_2 \implies P^T = P^T P
    $$

    $$
    (P^T)^T = P = P^T
    $$

    Therefore, orthogonality of the projected subspaces implies that the orthogonal projector must be symmetric.





A particularly important kind of orthogonal projector is the rank-one orthogonal projector,

$$
P_q = qq^T
$$

The complement is the rank $m - 1$ orthogonal projector which removes the component in the direction of $q$,

$$
P_{\perp q} = I - qq^T
$$

For idempotency, it is assumed that $q$ has norm $1$. However, normalizing is not hard.

## QR Factorization

The goal of QR factorization is to construct a sequence of orthonormal matrices $q_1, q_2, \dots$ that spans the successive column spaces of some matrix $A$. More precisely, for $A \in \mathbb{C}^{m \times n}, m \geq n$, we want:

$$
\text{Span}(q_1, \dots, q_j) = \text{Span}(a_1, \dots, a_j)
$$

for $j = 1, \dots, n$. This amounts to the condition that:

$$
\left[\begin{array}{c|c|c|c}
a_1 & a_2 & \cdots & a_n
\end{array}\right]
=
\left[\begin{array}{c|c|c|c}
q_1 & q_2 & \cdots & q_n
\end{array}\right]
\begin{bmatrix}
r_{11} & r_{12} & \cdots & r_{1n} \\
       & r_{22} &        & \vdots \\
       &        & \ddots &        \\
       &        &        & r_{nn}
\end{bmatrix}
$$

The coefficients in $R$ express that a column $a_j$ can be represented as a linear combination $\sum_{i = 1}^j r_{ij} q_i$ of the orthonormal columns of $Q$. More generally, we have $A = QR$ where $Q$ is a $m \times n$ matrix with orthonormal columns and $R$ is a $n \times n$ upper-triangular matrix. This factorization is called the *reduced $QR$ factorization of $A$*.

### Gram-Schmidt

One way to explicitly construct the $q$ vectors is to "invert" the sum $a_j = \sum_{i = 1}^j r_{ij} q_i$. Specifically,

$$
q_1 = \frac{a_1}{r_{11}}
$$

$$
q_2 = \frac{a_2 - r_{12} q_a}{r_{22}}
$$

$$
q_j = \frac{a_j - \sum_{i = 1}^{j - 1} r_{ij} q_j}{r_{jj}}
$$

This naturally produces a sequence of




## Appendix

Finally, we review outer-products.

### Outer Products

!!! tip "Theorem: "
    Matrix multiplication can be expressed as a sum of outer products.

!!! quote "Proof"
    Consider the generic $AB$ matrix multiplication.

    $$
    AB = \begin{bmatrix}
    a_{11} & \dots & a_{1N} \\
    \vdots & \ddots & \vdots \\
    a_{M1} & \dots & a_{MN} \\
    \end{bmatrix}
    \begin{bmatrix}
    b_{11} & \dots & b_{1P} \\
    \vdots & \ddots & \vdots \\
    b_{N1} & \dots & b_{NP} \\
    \end{bmatrix} = C
    $$

    $$
    c_{kl} = \sum_{i = 1}^N a_{ki} b_{il}
    $$

    The **outer-product** of two vectors is defined as:

    $$
    a_i \otimes b_j = ab^T = \begin{bmatrix}
    a_1 \\ \vdots \\ a_N
    \end{bmatrix} \otimes
    \begin{bmatrix}
    b_1 \\ \vdots \\ b_M
    \end{bmatrix} =
    \begin{bmatrix}
    a_1 b_1 & \dots & a_1 b_M \\
    \vdots & \ddots & \vdots \\
    a_N b_1 & \dots & a_N b_M \\
    \end{bmatrix}
    $$

    Let $C' = a_i \otimes b_j$. Then, $C'_{kl} = a_k b_l$.

    Generally, we can express:

    $$
    AB =
    \begin{bmatrix}
    a_1 | \dots | a_N
    \end{bmatrix}
    \begin{bmatrix}
    & b_1 & \\
    \hline
    & \vdots & \\
    \hline
    & b_N &
    \end{bmatrix}
    = C = \sum_{i = 1}^N a_i \otimes b_i^T
    $$

    In other words, a matrix-multiply can be expressed as a sum of rank-one outer-products. To see this, observe that:

    $$
    C_{kl} = [\sum_{i = 1}^N a_i \otimes b_i^T]_{kl}
    $$

    $$
    = \sum_{i = 1}^N (a_i \otimes b_i^T)_{kl}
    $$

    $$
    = \sum_{i = 1}^N a_{ki} b_{il}
    $$

    This is identical to the element-wise formula given by the regular process for matrix multiplication and holds for generic indices.
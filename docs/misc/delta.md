# Delta Net

We want to review the numerical linear algebra and linear attention background of delta-network style attention.

## Outer Products

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

## Projectors (Trefethen & Bau)

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

## Linear Attention

Standard attention (excluding scaling by $\sqrt{d_k}$) can be written as:

$$
\text{Attention}(Q, K, V) = \sigma(QK^T) V
$$

where $\sigma$ is the softmax function. Here, $Q, K, V \in \mathbb{R}^{T \times d_h}$ where $T$ is the context length and $d_h$ is the head-dimension. This scales like $O(T^2)$ as the attention score matrix is $QK^T \in \mathbb{R}^{T \times T}$.

*Vanilla Linear Attention* drops the softmax function and lets us reassociate the attention function such that:

$$
\text{VLA}(Q, K, V) = Q (K^T V)
$$

where $K^T V \in \mathbb{R}^{d_h \times d_h}$. Let $S = K^T V$. Ignoring the causal mask, we can write:

$$
S = \sum_{t = 1}^T k_t \otimes v_t = \sum_{t = 1}^T k_t v_t^T
$$

In other words, the state matrix $S$ can be expressed as a sum of rank-one outer-products. Generally, we have that $\text{rank}(S) \leq \min(T, d_h)$. As long as $T < d_h$, we could add new context (read: outer-products) to $S$ in principle with each new key-value outer-product possibly being orthogonal to all past outer-products.

Once we have $S$, we can essentially "query" it for the sum of the value vectors weighted by the attention score.

$$
S^T q = \sum_{t = 1}^T v_t (k_t^T q)
$$

## Delta Network

Under non-orthogonality or scenarios where $S$ is "stuffed" with too many outer-products, we can get the wrong coefficient for value vectors.

Suppose $q = k_1$ and $k_1$ is a unit-vector. Then,

$$
S^T q = S^T k_1 = \sum_{t} v_t (k_t^T k_1)
$$

This means for a single query directly equivalent to $k_1$, if there is any non-orthogonality between $k_1$ and other keys, instead of just getting $v_1$, we might also get other values (i.e if $k_1$ aligns with $k_2$, we would get a term $v_2 (k_2^T k_1)$ in $S^T q$).

In practice, random vectors in high-dimensional spaces tend to be nearly orthogonal so we might be okay. But can we scale to truly long-contexts? Can we fit a $1M$ context length in a $128 \times 128$ matrix?

Delta Network uses a soft-deletion strategy to over-write past key values with orthogonal updates.

!!! info "Definition: Delta Network Update"
    The typical delta rule in a one-layer neural network without a non-linearity is just:

    $$
    \Delta w_{ji} = \alpha (t_j - y_j) x_i
    $$

    In Delta-Networks, the generic update-rule without deletion can be written as:

    $$
    S_{t} = S_{t - 1} + \beta_t k_t (v_t - S_{t - 1}^T k_t)^T
    $$

Essentially, we are trying to "re-orthogonalize $S$" while adding a new value. The target $t_j$ is the clean value vector $v_t$ while the retrieved / noisy target value vector from $S$ is $S_{t - 1}^T k_t$ (as we outlined above). Expanding the update rule, we get:

$$
S_t = S_{t - 1} + \beta_t k_t v_t - \beta_t k_t k_t^T S_{t - 1}
$$

$$
= (I - \beta_t k_t k_t^T) S_{t - 1} + \beta_t k_t v_t^T
$$

As we saw before, $k_t \in \text{Ker}(I - \beta_t k_t k_t^T)$ since $(I - \beta_t k_t k_t^T)$ is the orthogonal projector. We apply this to the state matrix $S$, essentially removing the role of $k_t$ from the key-value map and over-write the deletion with the new key-value store, $k_t v_t^T$.


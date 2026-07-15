# Fundamental Subspaces

[TOC]

## Two Fundamental Subspaces

It's quite easy to identify two subspaces - the *kernel* or *null-space* and the image. These subspaces are both defined by a linear map.

Consider a linear map $L: X \to Y$. Then,

$$
\text{Ker}(L) = \{x \in X \mid L(x) = 0\}
$$

$$
\text{Im}(L) = \{L(x) : x \in X\} \subset Y
$$

The kernel is the subspace of vectors in the domain which are sent to $0$ and the image is the subspace of vectors in $Y$ which "came from" $X$. From this, we can recover Rank-Nullity, etc.

The image in particular is also called the span or *column-space* of $A$. But why is it called the column-space?

## Linear Maps, Column Space

Let $x_1, x_2, x \in X$ and $s \in \mathbb{F}$ where $\mathbb{F}$ is some field (like $\mathbb{C}, \mathbb{R}$). Then, $L: X \to Y$ is a linear map iff

$$
L(x_1 + x_2) = L(x_1) + L(x_2)
$$

$$
L(sx) = sL(x)
$$

This is still just an abstract map. Now suppose $X, Y$ are finite-dimensional. Fix a basis $\{e_1, \dots, e_n\}$ for $X$ and $\{f_1, \dots, f_m\}$ for $Y$. Then, any vector $x \in X$ can be represented as:

$$
x = \sum_{i = 1}^n s_i e_i = [e_1 \dots e_n] \begin{bmatrix}
s_1 \\ \vdots \\ s_n
\end{bmatrix}
$$

Then,

$$
L(x) = L([e_1 \dots e_n]
\begin{bmatrix}
s_1 \\ \vdots  \\ s_n
\end{bmatrix}
)
$$

$$
= L([e_1 \dots e_n]) \begin{bmatrix}
s_1 \\ \vdots \\ s_n
\end{bmatrix}
$$

When we apply $L$ to each basis vector $e_i$, the output vector can be represented as a linear combination of the output basis vectors. Specifically,

$$
L(e_j) = f_1 A_{1j} + \dots + f_m A_{mj} = \sum_i A_{ij} f_i
$$

This choice of which dimension to contract over is pure convention.

So we have:

$$
L(x) = [f_1 A_{11} + \dots + f_m A_{m1} & \dots & f_1 A_{n1} + \dots + f_m A_{mn}] \begin{bmatrix}
s_1 \\ \vdots \\ s_n
\end{bmatrix}
$$

$$
=
\begin{bmatrix}
f_1 & \dots & f_m
\end{bmatrix}
\begin{bmatrix}
A_{11} & \dots & A_{1n} \\ \vdots & \ddots & \vdots \\ A_{m1} & \dots & A_{mn}
\end{bmatrix}
\begin{bmatrix}
s_1 \\ \vdots \\ s_n
\end{bmatrix}
$$

$$
= F A s
$$

When we write a vector like $[1, 2, 3]^T$, we are really writing down $s$ as the coordinate representation within a specific basis. Additionally, in most cases, $F$ as a collection of basis vectors in $Y$ is just the identity matrix (typically if we are taking an orthonormal basis in $F$) so this really reduces to:

$$
L(v) = As
$$

Each column of a matrix merely encodes the action of the linear operator on a basis vector in the domain. Hence why it is appropriate to call this a "column-space". We also recover the typical formula of matrix-multiplication. Computationally, we are taking inner-products between the rows of $A$ and the vector $s$ but this is *equivalent* to scaling each column by the corresponding element of $s$. Write $A = [A_1 | \dots | A_n]$. If we ignore $F$ as the identity, then $L(s)$ (where $s$ is the coordinate vector) is:

$$
L(s) = L(\sum_i s_i e_i) = \sum_i s_i A_i
$$

## Orthogonal Complements

Given a subspace $E \subset V$, define the **orthogonal complement** of $E$ in $V$ as:

$$
E^{\perp} = \{v \in V: \forall e \in E, \langle e, v \rangle = 0\}
$$

This is the collection of vectors which are orthogonal to every vector in $E$. Hence why it is the complement.

(For convenience, we will now speak about linear maps and their matrix representation semi-interchangeably).

Now, recall the *adjoint* of a linear map $L^*$ is defined as:

$$
\langle L(x), y \rangle = \langle x, L^*(y) \rangle
$$

$$
(Ax)^T y = x^T A^T y
$$

!!! tip "Theorem: Orthogonality and Kernel"

    $$
    \text{Ker}(L^*) = \text{Img}(L)^{\perp}
    $$

    Here, $L$ and $L^*$ can be swapped and perpendicularity is symmetric.

!!! quote "Proof"

    Suppose $w \in \text{Ker}(L^*)$. Then,

    $$
    L^* (w) = 0 \iff \forall v \in V, \langle v, L^*w \rangle = 0
    $$

    $$
    \iff \forall v \in V, \langle L(v), w \rangle = 0
    $$

    $$
    \iff w \in \text{Img}(L)^{\perp}
    $$



Now view the matrix-vector product by taking inner-products between rows and $s$. Specifically,

$$
Ax = \begin{bmatrix}
A_{1, :}^T x \\
\vdots \\
A_{m, :}^T x
\end{bmatrix}
$$

Observe that this is $0$ iff $x$ is orthogonal to every row of $A$. But each row of $A$ is also a column of $A^T$.

Suppose $Ax = 0$. Then, $x \in \text{Ker}(A)$. But this also means $x$ is orthogonal to each column of $A^T$. Since $\text{Img}(A^T)$ is the space of all linear combinations and the inner-product is bilinear, it follows that $x$ is in the orthogonal complement of $\text{Img}(A^T)$.

So we get that:

$$
\text{Ker}(A) = \text{Img}(A^T)^{\perp}
$$

## Orthogonal Projections

Finally, we will prove that orthogonal projections minimize the distance to a subspace. First,

!!! info "Definition: Orthogonal Projection"

    An orthogonal projection is a projection where the kernel and image are orthogonal subspaces.

    $$
    P_E: E^{\perp} \oplus E \to E
    $$

    $$
    P_{E^{\perp}}: E^{\perp} \oplus E \to E^{\perp}
    $$

!!! tip "Theorem: Orthogonal Projection Minimizes Distance"

    For each $v \in E \oplus E^{\perp}$ and $w \in E$, the distance from $v$ to $e$ is minimized if $w = P_E(v)$ i.e.

    $$
    |v - w| \geq |v - P_E(v)|
    $$

    equality is clearly achieved when $w = P_E(v)$.

!!! quote "Proof"

    Let $v = v_1 + v_2, v_1 = P_E(v), v_2 = v - P_E(v) \in E^{\perp}$. For any $w \in E$,

    $$
    |v - w|^2 = |v_1 + v_2 - w|^2
    $$

    $$
    = \langle v_1 + v_2 - w, v_1 + v_2 - w \rangle
    $$

    $$
    = \langle v_1 - w, v_1 - w \rangle + \langle v_2, v_2 \rangle + \langle v_1 - w, v_2 \rangle + \langle v_2, v_1 - w \rangle
    $$

    $$
    = |v_1 - w|^2 + |v_2|^2
    $$

    $$
    = |v_1 - w|^2 + |v - v_1|^2 \geq |v - v_1|^2
    $$

    This is basically just Pythagoras. If we have some point above a subspace and we want to find some point which is closest to it, the distance can be computed by Pythagoras. The vertical drop is unavoidable but the horizontal drop is, hence why the smallest error is achieved when the target and error vectors are orthogonal to one another.

## Linear Regression

Consider the following modeling problem. We have a vector of targets $y$, a matrix $X$ where each row represents a single datapoint (and columns are features). We want to find $\beta$ such that $X \beta$ is "closest" to $y$.

There are several approaches to this involving matrix calculus but with those approaches, it's quite hard to remember the exact convention being used for gradients.

Instead, define the error vector

$$
e = y - X \beta
$$

Minimizing this error occurs when $e$ is in $\text{Img}(X)^{\perp}$. Therefore, $e \in \text{Ker}(X^T)$. So we have:

$$
X^T e = 0
$$

$$
X^T (y - X \beta) = 0
$$

$$
X^T X \beta = X^T y
$$

$$
\beta = (X^T X)^{-1} X^T y
$$

This is the simplest and most elegant way I know of to get the standard linear regression equation. More generally, the kernel and image of $L$ and $L^*$ have been frequently discussed as the "four fundamental subspaces" but I only just intuited the orthogonal complement (even though in retrospect, it was an incredibly natural idea?) and the connection between orthogonal rows and kernel of the transpose. I wanted to write this up as a nice motivator for the matrix-vector product "formula" which becomes retroactively defined by linearity + a basis.
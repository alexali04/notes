# Symmetry

## Isometries

The distance between points of $\R^{n}$ is the length $u - v$ of the vector $u - v$.

!!! info "Definition: Isometry"
    An *isometry* of $\R^{n}$ is a distance-preserving map $f: \R^n \to \R^{n}$ such that for all $u, \in \R^n$,

    $$
    |f(u) - f(v)| = |u - v|
    $$

An isometry will map a figure to a congruent figure.

!!! example "Example: Isometries"
    - Orthogonal linear operators are isometries. Since $\varphi$ is linear, it follows that $\varphi(u) - \varphi(v) = \varphi(u - v). Then,

    $$
    |\varphi(u - v)| = |u - v|
    $$

    hence orthogonal operators preserve distances.

    - Translation $t_a$ be a vector $a$, $t_a(x) = x + a$ is an isometry (as the vectors $a$ cancel out).

    - Composition of isometries is an isometry.

!!! tip "Theorem: Isometry Conditions"
    The following conditions on $\varphi: \R^n \to \R^n$ are equivalent.

    - $\varphi$ is an isometry that fixes the origin $\varphi(0) = 0$.
    - $\varphi(v) \cdot \varphi(w) = (v \dot w)$ for all $v, w$.
    - $\varphi$ is an orthogonal linear operator.






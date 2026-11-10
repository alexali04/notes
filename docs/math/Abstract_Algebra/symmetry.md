# Symmetry

[TOC]

## Isometries

The distance between points of $\R^{n}$ is the length $u - v$ of the vector $u - v$.

!!! info "Definition: Isometry"
    An *isometry* of $\R^{n}$ is a distance-preserving map $f: \R^n \to \R^{n}$ such that for all $u, \in \R^n$,

    $$
    |f(u) - f(v)| = |u - v|
    $$

An isometry will map a figure to a congruent figure.

!!! example "Example: Isometries"
    - Orthogonal linear operators are isometries. Since $\varphi$ is linear, it follows that $\varphi(u) - \varphi(v) = \varphi(u - v)$. Then,

        $$
        |\varphi(u - v)| = |u - v|
        $$

        hence orthogonal operators preserve distances.

    - Translation $t_a$ be a vector $a$, $t_a(x) = x + a$ is an isometry (as the vectors $a$ cancel out).

    - Composition of isometries is an isometry.

Recall the definition of an orthogonal matrix. $A$ is an orthogonal matrix provided that $A^T A = I \iff A^T = A^{-1} \iff Ax \cdot Ay = x \cdot y \iff \det(A) = \pm 1 \iff A$'s columns form an orthonormal basis of $R^n$.

Crucially, we will use the property of preserving dot-products, i.e. $Ax \cdot Ay$.

!!! tip "Theorem: Isometry Conditions"
    The following conditions on $\varphi: \R^n \to \R^n$ are equivalent.

    - a. $\varphi$ is an isometry that fixes the origin $\varphi(0) = 0$.
    - b. $\varphi(v) \cdot \varphi(w) = v \cdot w$ for all $v, w$.
    - c. $\varphi$ is an orthogonal linear operator.

We know that $c \implies a$.

!!! question "Lemma"
    Let $x, y \in \R^n$. If $x \cdot x = x \cdot y = y \cdot y$, then $x = y$.

!!! quote "Proof"
    Suppose $x \cdot x = x \cdot y = y \cdot y$. Then,

    $$
    (x - y) \cdot (x - y) = x \cdot x + y \cdot y - 2 x \cdot y = 0 \implies x = y
    $$

Now, we prove that $b \implies c$.

!!! quote "Proof"
    Let $\varphi$ be a map that preserves dot-products. Then, it will be orthogonal provided that it is a linear operator. So we need to show that $\varphi(cx) = c \varphi(x)$ and $\varphi(x + y) = \varphi(x) + \varphi(y)$.

    Suppose $w = u + v$. We want to show that $\varphi(w) = \varphi(u) + \varphi(v)$. To show this, it suffices to show that $\varphi(w) \cdot \varphi(w) = \varphi(w) \cdot (\varphi(u) + \varphi(v)) = (\varphi(u) + \varphi(v)) \cdot (\varphi(u) + \varphi(v))$.

    Then, it suffices to show that:

    $$
    \varphi(w) \cdot \varphi(w) = \varphi(w) \cdot \varphi(u) + \varphi(w) \cdot \varphi(v) = \varphi(u) \cdot \varphi(u) + \varphi(v) \cdot \varphi(v) + 2 \varphi(u) \cdot \varphi(v)
    $$

    Since $\varphi$ preserves dot-products, we just need to show that:

    $$
    w \cdot w = w \cdot u + w \cdot v = u \cdot u + v \cdot v + 2 u \cdot v
    $$

    Since $w = (u + v)$, we have that $w \cdot w = w \cdot (u + v) = (u + v) \cdot (u + v)$. Therefore, $\varphi(w) = \varphi(u) + \varphi(v)$.

    The proof for $\varphi(cv) = c \varphi(v)$ sets $u = cv$ and shows that $\varphi(u) = c \varphi(v)$ and is analogous.

Next, we show that $a \implies b$.

!!! quote "Proof"
    Let $\varphi$ be an isometry that fixes the origin. Then,

    $$
    (\varphi(u) - \varphi(v)) \cdot (\varphi(u) - \varphi(v)) = (u - v) \cdot (u - v)
    $$

    Substitute $v = 0$. Since $\varphi(0) = 0$, it follows that $\varphi(u) \cdot \varphi(u) = u \cdot u$. Similarly, $\varphi(v) \cdot \varphi(v) = v \cdot v$. Expanding, we get:

    $$
    \varphi(u) \cdot \varphi(u) + \varphi(v) \cdot \varphi(v) - 2 \varphi(v) \cdot \varphi(u) = u \cdot u + v \cdot v - 2 u \cdot v
    $$

    Canceling, we get:

    $$
    \varphi(v) \cdot \varphi(u) = u \cdot v
    $$

!!! warning "Corollary: Isometry Composition"
    Every isometry $f$ of $\R^n$ is the composition of an orthogonal linear operator and a translation. If $f$ is an isometry and $f(0) = a$, then $f = t_a \varphi$ where $t_a$ is a translation and $\varphi$ is an orthogonal linear operator. This expression for $f$ is unique.

!!! quote "Proof"
    Let $f$ be an isometry and $a = f(0)$. Let $\varphi = t_{- a} f$. Then, $t_a \varphi = f$. Since $\varphi$ is the composition of isometries $t_{- a}$ and $f$, it's an isometry. $\varphi$ also fixes the origin, $\varphi(0) = t_{-a} f(0) = t_{-a} a = 0$. Since $\varphi$ is an isometry which fixes the origin, it is an orthogonal linear operator. The expression $f = t_a \varphi$ is unique - since $\varphi(0) = 0$, we have $a = f(0) \implies \varphi = t_{- a} f$.


Can we compose isometries together? We know that the composition of orthogonal operators is an orthogonal operator.

Clearly, $t_a t_b = t_{a + b}$. We also have that $\varphi t_a = t_{\varphi(a)} \varphi$.

$$
\varphi t_a(x) = \varphi(a + x) = \varphi(a) + \varphi(x) = t_{\varphi(a)} \varphi(x)
$$

!!! warning "Corollary: Isometry Group"
    The set of all isometries of $\R^n$ forms a group $M_n$ with composition of functions as its law of composition.

!!! quote "Proof"
    The composition of isometries is an isometry. The inverse of an isometry is an isometry too since orthogonal operators and translations are invertible so if $f = t_a \varphi$, then

    $$
    f^{-1} = \varphi^{-1} t_a^{-1} = \varphi^{-1} t_{- a}
    $$

    This is a composition of isometries so $f^{-1}$ is an isometry.

    The composition of isometries:

    $$
    t_a \varphi t_b \phi (x) = t_a \varphi(b + \phi(x)) = a + \varphi(b) + \varphi \phi(x) = t_{a + \varphi(b)} \varphi \phi(x)
    $$

$O_n$ is the group of $n \times n$ orthogonal matrices (product of orthogonal matrices is orthogonal and the transpose (inverse) is orthogonal). $O_n$ is a subgroup of $\text{GL}_n$.

!!! success "Proposition: Homomorphism"
    There is a map $\pi: M_n \to O_n$ defined by dropping the translation part of an isometry. Specifically, if $f = t_a \varphi$, then $\pi(f) = \varphi$. This map $\pi$ is a surjective homomorphism where $\text{Ker}(\pi) = T = \{t_v\}$, the set of translations which is a normal subgroup of $M_n$.

!!! quote "Proof"
    It's clear that $\pi$ is surjective. We need to show that $\pi(fg) = \pi(f) \pi(g)$. Suppose $f = t_a \varphi, g = t_b \phi$. Then,

    $$
    \pi(f) \pi(g) = \varphi \phi
    $$

    $$
    \pi(fg) = \pi(t_a \varphi t_b \phi) = \pi(t_{a + \varphi(b)} \varphi \phi) = \varphi \phi
    $$

    Therefore, $\pi(fg) = \pi(f) \pi(g)$ so $\pi$ is a homomorphism.

Let $P$ be an $n$-dimensional space. The formula $t_a \varphi$ depends on the choice of coordinates. How does the formula change when coordinates are changed? We allow changes of coordinates via isometry.

Consider isometry $f, p \in P$ and $q = f(p)$. When we introduce coordinates $P$ is identified with $\R^n$ and $p, q$ have coordinates as $x = (x_1, \dots, x_n), y = (y_1, \dots, y_n)$. Then, $q = f(p)$ translates to $y = m(x) = t_a \varphi(x)$.

Let $\eta$ be the isometry performing a change of coordinates. Specifically, $\eta$ maps new coordinates back to the old coordinates. Then, the new coordinate vectors for $p, q$ are $x', y'$. Then, $m'$ for $f$ is $m'(x') = y'$. Substitute $\eta(x') = x, \eta(y') = y$ into the equation $m(x) = y$ obtaining $m \eta(x') = \eta(y') \implies \eta^{-1} m \eta(x') = y'$. So the new formula is the conjugate:

$$
m' = \eta^{-1} m \eta
$$

!!! warning "Corollary"
    The homomorphism $\pi: M_n \to O_n$ doesn't change when the origin is shifted by translation.

If $\eta = t_v$, then $m' = t_{- v} m t_v$. Since the translations are in the kernel of $\pi$ and since $\pi$ is a homomorphism, $\pi(m') = \pi(m)$.

Finally, we consider orientation. The determinant of orthogonal operator $\varphi$ on $\R^n$ is $\pm 1$. The operator is orientation-preserving if $\det(\varphi) = 1$ and orientation-reversing if $\det(\varphi) = -1$. Similarly, an isometry $f = t_a \varphi$ is called orientation-preserving or reverseing if $\varphi$ is orientation preserving or reversing.

The map $\sigma: M_n \to \{\pm 1\}$ that sends orientation-preserving isometries to $1$ and orientation-reserving isometries to $-1$ is a group homomorphism.

## Plane Isometries



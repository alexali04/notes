# Groups

## Definitions, Examples

!!! info "Definition: Law of Composition"
    A law of composition is a binary function:

    $$
    S \times S \to S
    $$

    This law is *associative* if $(ab)c = a(bc)$. The law is *commutative* if $ab = ba$. Associativity is more fundamental than commutativity because it relates to function composition.

!!! info "Definition: Group"
    A group is a set $G$ with a binary operation on $G$ with the following properties.

    - The operation is associative, $(ab)c = a(bc)$ for all $a, b, c \in G$.
    - $G$ has an identity element $1$ such that $1a = a1 = a$ for all $a \in G$.
    - For each $a$ in $G$, there exists an inverse element $b$ such that $ab = 1$.

Associativity, identity, and invertibility - that's all a group is.

An *abelian group* is one whose operation is also commutative.

!!! example "Example: Groups"

    - $\mathbb{R} / \{0\}$ forms an abelian group under multiplication. Multiplication is associative, invertible (under exclusion of $0$) and the identity is $1$.
    - $\mathbb{R}$ forms an abelian group under addition. Addition is associative, invertible (via subtraction), and the identity is $0$.
    - The set of invertible $n \times n$ matrices forms a group under matrix multiplication. It's associative, invertible and the identity matrix is the identity. This is called the *general linear group*.

The order of a group $G$ is the number of elements it contains denoted by $|G|$. If $|G|$ is finite, then $G$ is a *finite group*. Otherwise, $G$ is an infinite group.

!!! tip "Theorem: Cancellation Law"
    Let $a, b, c$ be elements of a group $G$. If $ab = ac$ or $ba = ca$, then $b = c$. This is a direct consequence of the inverse.

Groups can also be obtained by excluding elements that are not invertible.

- $\text{GL}_n(\mathcal{F}) = \{A \in \mathcal{F}^{n \times n} | \det(A) \neq 0\}$. This is the $n \times n$ general linear group - the group of all invertible $n \times n$ matrices. We can write $\text{GL}_n(\mathbb{R})$ or $\text{GL}_n(\mathbb{C})$ to indicate if we are working with real or complex matrices.
- Let $M$ be the set of maps from a set $T$ to itself. A map $f: T \to T$ has an inverse iff it is bijective - in other words, $f$ is a *permutation* of $T$. These permutations form a group where the binary op. is function composition. The group of permutations of index set $\{1, 2, \dots, n\}$ is called the *symmetric group* written like $S_n$. $|S_n| = n!$.

!!! quote "Important: "
    The elements of a permutation group are the permutations, not the set of indices.

## Permutation Groups

### Cyclic Notation

To write down a permutation, we typically use *cycle notation*. Consider the output of some permutation $p$ to be

$$
p = \begin{bmatrix}
1 & 2 & 3 & 4 & 5 \\
3 & 5 & 4 & 1 & 2
\end{bmatrix}
$$

$p$ maps each element in the upper row to the matching element in the bottom row. Writing the output of each permutation makes it a nightmare to track composition of permutations (which is what we really care about).

Instead, we use cycle notation. Pick some index, say $3$. $p(3) = 4$. $p(4) = 1$. $p(1) = 3$. So we have a cycle $(3, 4, 1)$. Since $p(2) = 5$ and $p(5) = 2$, we can write:

$$
p = (3 \ 4 \ 1) (2 \ 5)
$$

Basically, an index within a cycle gets mapped to the next element.

Consider $q = (1 \ 4 \ 5 \ 2)$. We want to compute $q \circ p$. In function composition, the inner function is applied first. So consider an index $1$. By $p$, $1$ gets mapped to $3$ and $q$ leaves $3$ alone. $p(3) = 4$ and $q(4) = 5$. $p(5) = 2$ and $q(2) = 1$. So we have the chain:

$$
q \circ p = (1 \ 3 \ 5)
$$

where the omitted $2$ and $4$ means that those indices are left alone (which is easily verifiable).

Consider $S_2 = \{a, b\}$. All we can do is either apply the identity $i$ or transpose $\tau$. Since there are only two permutations, our group has order two.

Consider $S_3$. This is the smallest group whose binary operation isn't commutative. Pick two permutations - the cyclic permutation $x = (1, 2, 3)$ and the transposition $(1, 2)$. We have $x^3 = 1$ and $y^2 = 1$ (following the cycle).

It's also easily verifiable that $yx = x^2y$. $x^3 = 1 \implies x \circ x^2 = 1 \implies x^2 = x^{-1}$. Let's multiply both sides by $y$. We get $x^2 y = x^{-1} y$.

$$
\begin{aligned}
x^{-1} &= (3 \ 2 \ 1) \\
y &= (1 \ 2) \\
x^{-1} y &= (2 \ 3)
\end{aligned}
$$

$$
\begin{aligned}
y &= (1 \ 2) \\
x &= (1 \ 2 \ 3) \\
yx &= (2 \ 3)
\end{aligned}
$$

So $x^2 y = yx$.

Thus our group is:

$$
S_3 = \{1, x, x^2, y, xy, x^2 y\}
$$

Any product of elements $x, y$ can be shown to be equal to an element of $S_3$.

$$
x^{-1} y^3 x^2 y = x^2 y^3 y x = x^2 y^4 x = x^3 = 1
$$

These rules are called the *defining relations* for the group.

## Subgroups

The general linear group and symmetric groups are important because many other groups are included in them as subgroups.

!!! info "Definition: Subgroup"
    A subset $H$ of group $G$ is called a *subgroup* if

    - *Closure*. If $a, b \in H$, then $ab \in H$.
    - *Identity*. $1 \in H$.
    - *Inverses*. $a \in H \implies a^{-1} \in H$.

The first condition states that the law of composition on $G$ induces a law of composition on $H$. The other conditions state that $H$ is a group w.r.t. the induced law.

!!! example "Example: Subgroups"
    - The group of $n \times n$ real matrices with determinant $1$ is a subgroup of the general linear group $\text{GL}_n(\mathbb{R})$. This is called the *special linear group*, $\text{SL}_n(\mathbb{R})$.
    - Complex numbers of absolute value $1$ are the set of points on the unit circle in the complex plane. It's a subgroup of the multiplicative group $\mathbb{C}^{\times}$ called the *circle group*.

Each group $G$ has two obvious subgroups - the group $G$ itself and the *trivial* subgroup containing just the identity element. A subgroup is called a *proper subgroup* if its neither of these two.


!!! tip "Theorem: Subgroups of Additive Groups of Integers"
    Let $S$ be a subgroup of the additive group $\mathbb{Z}^{+}$. Either $\mathbb{Z}$ is the trivial subgroup $\{0\}$ of it has the form $\mathbb{Z}a$ where $a$ is the smallest positive integer in $S$. Here,

    $$
    \mathbb{Z}a = \{n \in \mathbb{Z} \mid n = ka, k \in \mathbb{Z}\}
    $$


!!! quote "Proof"
    Let $S$ be a subgroup of $\mathbb{Z}^{+}$. Then, $0 \in S$. If $S = \{0\}$, then its the trivial subgroup. Othherwise, there exists at least two more integers, namely $n$ and $-n$. WLOG, suppose $n > 0$. We now show that $S = \mathbb{Z}a$ where $a$ is the smallest positive integer in $S$. The way to show two sets are equivalent is to show that they are subsets of one another.

    First, we show that $\mathbb{Z}a \subseteq S$, namely that $ka \in S$ for every integer $k$. If $k > 0$, then $ka = (a + \dots + a)$ which is in $S$ under closure. If $k = 0$, then $ka = 0 \in S$. If $k < 0$, then $-ka \in S$ so by the inverse property of $S, ka \in S$. Therefore, $ka \in S$.

    Next, we show that $S \subseteq \mathbb{Z}a$, i.e. every element $n \in S$ is an integer multiple of $a$, the smallest positive integer in $S$. Consider an arbitrary element $n \in S$. By the division theorem, we have $n = qa + r$ where $0 \leq r < a$. Naturally, $qa \in \mathbb{Z}a$ since $a \mid qa$. Since $\mathbb{Z}a \subseteq S$, it follows that $qa \in S$ as well. Since $n, qa \in S$, it follows that $n - qa = r$ is also in $S$ as $S$ is closed under addition and has an inverse. Therefore, $r \in S$. Since $a$ is the smallest positive integer in $S$ and $0 \leq r < a$, $r = 0$ and $n = qa \implies n \in \mathbb{Z}a$.

    Therefore, $S = \mathbb{Z}a$.

This theorem is quite strong - every possible subgroup of the additive group of integers is just a group where the elements are all integer multiples of some integer $a$.

I review this only briefly since I dislike the book-keeping involved in the GCD algorithm.


### Cyclic Subgroups

We consider an important abstract example of a subgroup, the *cyclic subgroup* generated by an arbitrary element $x$ of a group $G$ (using multiplicative notion).

!!! info "Definition: Cyclic Subgroup"
    The *cyclic subgroup* $H$ generated by $x$ is:

    $$
    H = \{\dots, x^{-2}, x^{-1}, 1, x, x^2, \dots \}
    $$

    This is the smallest subgroup of $G$ containing $x$ and is often written $\langle x \rangle$.

The notation $x^n$ represents an element of the group obtained under the particular law. For example, if $G$ is the multiplicative group $\mathbb{R}^{\times}$ and $x = -1$, then $\langle -1 \rangle = \{-1, 1\}$. Either $x^n$ represents different elements or they don't. Consider the cases.

!!! success "Proposition: Cyclic Subgroups"
    Let $\langle x \rangle$ be the cyclic subgroup of a group $G$ generated by $x \in G$ and $S = \{k \in \mathbb{Z} \mid x^k = 1\}$.

    Then,

    - $S$ is a subgroup of $\mathbb{Z}^{+}$.
    - The powers $x^r = x^s$ with $r \geq s$ are equal iff $x^{r - s} = 1$, i.e. if $r - s \in S$.
    - Suppose $S$ is not the trivial subgroup. Then, $S = \mathbb{Z}n$ for some positive integer $n$. Then, $1, x, x^2, \dots, x^{n - 1}$ are the distinct elements of subgroup $\langle x \rangle$ and the order of $\langle x \rangle$ is $n$.

Basically, if $c$ is the smallest positive integer such that $x^c = 1$, then past $c$, the group elements begin to recycle.

Then, the group $\langle x \rangle = \{1, x, \dots, x^{n - 1}\}$ is called the cyclic group of order $n$.

Within $S_3$, $x$ has order $3$ and $y$ has order $2$. If $x^n \neq 1$ for all $n > 0$, then $x$ has infinite order and the group is infinite cyclic.

We can also speak about the subgroup $G$ generated from a subset $U$. This is the smallest subgroup of $G$ that contains $U$ and it consists of all elements of $G$ that can be expressed as a product of a "string" of elements in $U$ and relevant inverses. A subset $U$ of $G$ is said to *generate* $G$ if every element of $G$ is such a product. For example, in $S_3$, the set $U = \{x, y\}$ generates $S_3$. Elementary matrices generated $\text{GL}_n$.

In those particular examples, inverses weren't needed but that's not always the case. Negative powers are generally needed to fill out the group. 














---
numbering: false
---

# Exercises

I wrote out the solutions to several problems on paper and have had Opus 5.5 transcribe them.

[TOC]

# Artin, Chapter 2 — Exercises

## Section 1: Laws of Composition

### 1.1

WTS $ab = a$ is associative.

Let $a, b, c \in S$. Then

$$
\begin{aligned}
(ab)c &= ac = a \\
a(bc) &= ab = a \\
\Rightarrow \quad (ab)c &= a(bc)
\end{aligned}
$$

Sup. $1 \in S$. Then $1a = a$ but $1a = 1 \Rightarrow a = 1$. Therefore $S = \{1\}$.

### 1.2.a

Sup. $la = 1$, $ar = 1$. WTS $l = r$, $a$ is invertible, and $r = a^{-1}$.

$$
\begin{aligned}
1 \cdot 1 &= 1 \\
(ar) \cdot (ar) &= 1 \\
a(ra)r &= 1 \Rightarrow ra = 1 = la \\
&\Rightarrow r = l, \quad r = a^{-1}
\end{aligned}
$$

### 1.2.b

If $a^{-1}$ exists, it is unique.

Sup. $a^{-1}a = 1$, $b^{-1}a = 1$. Then

$$
\begin{aligned}
a^{-1}a &= b^{-1}a \\
(a^{-1}a)a^{-1} &= (b^{-1}a)a^{-1} \\
a^{-1}(aa^{-1}) &= b^{-1}(aa^{-1}) \\
\Rightarrow \quad a^{-1} &= b^{-1}
\end{aligned}
$$

### 1.2.3

Inverses multiply in opposite order.

Sup. $a, b$ invertible. WTS that $(ab)^{-1} = b^{-1}a^{-1}$.

$$
\begin{aligned}
(ab)(ab)^{-1} &= 1 \\
(ab)(b^{-1}a^{-1}) &= \\
a(bb^{-1})a^{-1} &= \\
aa^{-1} &= 1 \\
\Rightarrow \quad (ab)^{-1} &= b^{-1}a^{-1}
\end{aligned}
$$

### 1.2.4

By def'n, an inv. of $a$ is some elem $b$ s.t. $ab = ba = 1$. See 1.3 for example.

### 1.3

Consider $s(n): \N \to \N$ where $s(n) = n + 1$. WTS $s(n)$ has no right inverse but inf. many left inverses.

Let $f: \N \to \N$ be our candidate inverse. $s(n)$ has no right inverse. We require that $s \circ f(n) = n$. But there is no natural number $f(1)$ such that $s \circ f(1) = 1$ since $1$ is the smallest element in $\N$. Therefore, $s$ has no right inverse.

However, $s$ has infinitely many left inverses. We require that $f \circ s(n) = n$. So $f(2) = 1, f(3) = 2, \dots$. However, $f(1)$ is free to vary. Therefore, there are an infinite number of left inverses of $s$.

---

## Section 2: Groups and Subgroups

### 2.2

Let $S = (S, \cdot)$ where $\cdot$ is associative, $1 \in S$. WTS $U \subseteq S$ s.t. $U = \{a \mid a^{-1} \in U\}$ is a group.

Associativity carries over. $1 \in U$ since $1^{-1} = 1$. NTS that $ab \in U$ is invertible. Then,

$$
(ab)b^{-1}a^{-1} = a(bb^{-1})a^{-1} = aa^{-1} = 1 \implies ab \text{ is invertible}
$$

Since $U$ has an associative, closed law of comp. and $1 \in U$, $U$ forms a group.

### 2.3

**(a)**

$$
\begin{aligned}
xyz^{-1}w &= 1 \\
xy &= w^{-1}z \\
y &= x^{-1}w^{-1}z
\end{aligned}
$$

**(b)** Sup. $xyz = 1$. Then $yz = x^{-1}$. Then,

$\Rightarrow (yz)x = x^{-1}x = 1$

$\Rightarrow zx = y^{-1}$

$\not\Rightarrow yxz = 1$ since $xz \neq zx$ (necessarily).

### 2.4

**(a)** $GL_n(\mathbb{R})$ is a group and a subset of $GL_n(\mathbb{C})$ so yes.

**(b)** Yes, $\{\pm1\}$ is a subgroup of $\R^{\times}$.

**(c)** No, not invertible.

**(d)** No, not invertible.

**(e)** No since $I \notin H$.

### 2.5

Sup. $H \subseteq G$, $1 \in H$. Let $h \in H, G$.

Then $1 \cdot h = h \in G \Rightarrow 1 \in G$.

$h^{-1}h = 1$. $h^{-1} \in H \subseteq G \Rightarrow h^{-1} \in G$.

### 2.6

$G^\circ = \{G,\ a * b = ba\}$. WTS $G^\circ$ is a group.

**Associative:**

$$
\begin{aligned}
a * (b * c) &= a * (cb) = cba \\
(a * b) * c &= (ba) * c = cba
\end{aligned}
$$

**Identity:** $1$ carries over. $a * 1 = 1a = a$.

**Inverse:** $a * a^{-1} = a^{-1}a = 1$.

---

## Section 4: Cyclic Groups

### 4.1

Sup $a, b \in G$, $a^7 = 1$ and $a^3 b = b a^3$. WTS that $ab = ba$.

$$
ab = ab \cdot 1 = ab \cdot a^7 = a (ba^7) = a (ba^3) a^4 = a (a^3 b) a^4 = a^4 b a^4 = a^7 ba = ba
$$

### 4.2

Sup. $z \in \C$ s.t. $z^n = 1$.

a) Show that $z^n$ form a cyclic subgroup of $\C^{\times}$.

$\langle z \rangle = \{0, z, \dots, z^{n - 1}\}$. By definition, $\langle z \rangle$ is cyclic. Complex multiplication is associative and invertible since $z^k z^{-k} = z^0 = 1$. It's also closed since $z^a z^b = z^{a + b \mod n}$. Therefore, $\langle z \rangle$ forms a cyclic subgroup.

b) Find the product of the roots of unity.

$$
\prod_{i = 0}^n z^i = z^{\sum_{i = 1}^n} = z^{n(n + 1)/2}
$$

Generally, $z = e^{2 \pi i / n}$ where $i$ is the imaginary unit, not an index. Then, $z^{n(n + 1)/2} = e^{\pi i (n + 1)} = (-1)^{n + 1}$.


### 4.3

Let $a, b \in G$. WTS that $|ab| = |ba|$. Suppose $|ab| = k$, i.e. $k$ is the smallest integer s.t. $(ab)^k = 1$. Then,

$$
\begin{aligned}
b(ab)^k &= b \\
(ba)^kb &= b \\
(ba)^k &= 1
\end{aligned}
$$

Let $k' = |ba|$. Then, $k' \leq k$. By symmetry, we can show that $k \leq k'$ (repeat the above trick in the opposite direction). Therefore, $k' = k$ and $|ab| = |ba|$.

### 4.4

Describe all groups $G$ that contain no proper subgroup.

A proper subgroup is a subgroup which is neither the whole group nor the trivial group (just the identity). This is all cyclic groups which have prime orders.

### 4.5

Show that every subgroup of a cyclic group is cyclic.

Suppose $S$ is a subgroup of cyclic group $C$. Let $d$ be the smallest integer such that $x^d \in S$. We want to show that for all $x^m \in S, m = zd$ where $z \in \Z$.

Let $x^m \in S, m = qd + r$. WTS $r = 0$. Then, $r = m - qd, x^r = x^m x^{-qd}$. $x^r \in S$ since $x^m, x^{-qd} \in S$. However, $x^r < x^d \implies r= 0 \implies m = qd$. Therefore, $S$ is cyclic.

### 4.6

Let $G$ be a cyclic group of order $6$. How many of its elements generate $G$? What about order $5, 8$?

Clearly, $x$ generates $G$. So does $x^5$ (work out the math mod $6$). Clearly, any divisors of $|G|$ other than $1$ don't generate $G$ as they cycle through $G$ once reaching $|G|$. But neither does $x^4$ since the cycle goes $x^4, x^2, x^6, x^4$. Only elements with exponents which are relatively prime to $|G|$ generate $G$. So if $|G| = 6$, then, $\{x, x^5\}$. If $|G| = 5$, then $\{x, x^2, x^3, x^4\}$ generate $G$. If $|G| = 8$, then $\{x, x^3, x^5, x^7\}$ generate $G$.

-- Skipping 4.7 since dumb ---

### 4.8

--- Skipping a ---

b) Show that elementary matrices of the first type generate $\text{SL}_n(\R)$. Do the $2 \times 2$ case first.

We'll show that you can convert arbitrary elements of $\text{SL}_n(\R)$ into $I$ using only left-multiplication by first-type elementary matrices. These matrices correspond to row addition / subtraction which does not affect determinants. Consider the $2 \times 2$ case first. Then, we have $x \in \text{SL}_n(\R)$ where:

$$
x = \begin{bmatrix}
a & b \\
c & d
\end{bmatrix}
$$

where $ad - bc = 1$. Suppose $c \neq 0$. Then, left-multiply by:

$$
\begin{bmatrix}
1 & (1 - a)/c \\
0 & 1
\end{bmatrix}
\begin{bmatrix}
a & b \\
c & d
\end{bmatrix} =
\begin{bmatrix}
1 & b + d(1 - a)/c \\
c & d
\end{bmatrix}
$$

$$
\begin{bmatrix}
1 & 0 \\
-c & 1
\end{bmatrix}
\begin{bmatrix}
1 & b + d(1 - a)/c \\
c & d
\end{bmatrix} =
\begin{bmatrix}
1 & b + d(1 - a)/c \\
0 & d -c(b + d(1 - a)/c)
\end{bmatrix}
$$

Observe that the bottom-right element reduces to $ad - bc = 1$. So we have:

$$
\begin{bmatrix}
1 & b + d(1 - a)/c \\
0 & 1
\end{bmatrix}
$$

We can easily clear the top-right element since elementary matrices of the first type do row substitution. Since we can convert arbitrary $2 \times 2$ matrices with determinant $1$ into $I_2$ with just first-type elementary matrices, we can generate those matrices by inverting the first-type elementary matrices (which themselves are first-type elementary matrices).

Next, we generalize by induction. Suppose it's true for $n - 1$. We've shown it true for the base case $n = 2$. Consider $n \times n$ matrix $A$.

Since $\det(A) = 1$, the first column must have some non-zero entry. Suppose there exists some non-zero $a$ in the first column. Via row-substitution, we can introduce a second element $ta$ into a different row. Using the same trick as in the $2 \times 2$ case, we can convert the top-left element of $A$ and clear out the column. Then, the matrix looks like

$$
\begin{bmatrix}
1 & \text{ junk } \\
0 & B
\end{bmatrix}
$$

where $B$ is the submatrix. Since we've only done row substitutions, we haven't changed the determinant of $B$. Via cofactor expansion where $a_{11} = 1$, we know that $\det(B) = 1$. By the induction assumption, we can reduce $B$ in the same way. Therefore, $A$ can be generated by first-type elementary matrices and by induction first-type elementary matrices generate $\text{SL}_n(\R)$ for all $n$.

## Section 5: Homomorphisms

## Section 6: Isomorphisms

## Section 7: Equivalence Relations

## Section 8: Cosets


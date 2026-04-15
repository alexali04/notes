# Background

## Topology

### Metric Space

!!! info "Definition: Metric space"

    A **metric space** is a pair $(M, d)$ consisting of a set of points $M$ and a metric $d: M \times M \to \mathbb{R}_{\geq 0}$. $d$ is symmetric, positive-definite, and satisfies the triangle-inequality.

Examples:
1. The real line $\mathbb{R}$ is a metric space under $d(x, y) = |x - y|$.
2. $\mathbb{R}^2$ is a metric space where $d((x_1, y_1), (x_2, y_2)) = \sqrt{(x_1 - y_1)^2 + (x_2 - y_2)^2}$.

This metric allows for very natural definitions of convergence and continuity.

!!! info "Definition: Convergence"

    Let $(x_n)_{n \geq 1}$ be a sequence of points in a metric space $(M, d)$. We say that $x_n$ **converges** to $x$ if for all $\epsilon > 0$, there is an integer $N_{\epsilon}$ such that for each $n \geq N_{\epsilon}$,

    $$
    d(x_n, x) < \epsilon
    $$


## Probability and Measure Theory

### Measures

Consider a non-empty set $\Omega$.

!!! info "Definition: $\sigma$-algebra"

    A collection $\mathcal{S}$ of subsets of $\Omega$ for which:

    1. $\Omega \in \mathcal{S}$.
    2. $A \in \mathcal{S} \implies A^C \in \mathcal{S}$.
    3. $S_1, S_2, \dots \in \mathcal{S} \implies S_1 \cup S_2 \cup \dots \in \mathcal{S}$.

    The pair $(\Omega, \mathcal{S})$ is called a *measurable space*.


!!! info "Definition: Measure"

    Let $S$ be a $\sigma$-algebra on $\Omega$. A map $\mu: S \to [0, \infty]$ is called a measure if:

    1. $\mu(\emptyset) = 0$.
    2. $S_1, S_2, \dots,$ are pairwise-disjoint implies that $\mu(S_1 \cup S_1 \cup \dots) = \sum_{i} \mu(S_i)$.

The $\sigma$-algebra selects which events $S \subset \Omega$ we can measure. For the trivial $\sigma$-algebra, $\{\emptyset, \Omega\}$, all we know is that $\mu(\emptyset) = 0, \mu(\Omega) = 1$.




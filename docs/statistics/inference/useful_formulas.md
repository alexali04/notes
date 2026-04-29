# Useful Formulas

## Variance

- $\text{Var}(aX + b) = a^2 \text{Var}(X)$.
- $\text{Var}(X) = \mathbb{E}[X^2] - \mathbb{E}[X]^2$.

## Inequalities

- Chebyshev's Inequality: Let $X$ be a random variable and $g(x)$ be a non-negative function. Then, for any $r > 0$,

$$
P(g(X) \geq r) \leq \frac{\mathbb{E}[g(X)]}{r}
$$

## Convergence

- Convergence: A sequence $(a_n)$ *converges* to a real number $a4 if for every $\epsilon > 0$, there exists an $N_{\epsilon} \in \mathbb{N}$ such that for all $n \geq N_{\epsilon}$

  $$
  |a_n - a| < \epsilon
  $$

In other words, fix a radius $\epsilon$. Then, for any radius, there's a certain index $n$ past which all points $a_n$ exist in the $\epsilon$-ball around $a$.


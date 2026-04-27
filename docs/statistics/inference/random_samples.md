# Random Samples

## Basic Concepts

!!! info "Definition: I.I.D. random Variables"

    A *random sample* of size $n$ from a population with distribution $f(x)$ is a collection of mutually independent random variables $X_1, \dots, X_n$ where each RV has marginal distribution $f(x)$. Alternatively, $X_1, \dots, X_n$ are called *independently and identically distributed random variables with probability distribution $p(x)$*.

By independence, we have:

$$
f(x_1, \dots, x_n) = \prod_{i = 1}^n f(x_i)
$$

If the population distribution is from a parametric family given by $f(x \mid \theta)$,

$$
f(x_1, \dots, x_n \mid \theta) = \prod_{i = 1}^n f(x_i \mid \theta)
$$

## Sums over Random Samples

!!! info "Definition: Statistic"

    Let $X_1, \dots, X_n$ be a random sample (drawn with replacement) of size $n$ from a population. Let $T(x_1, \dots, x_n)$ be a functionn whose domain includes the sample space of $(X_1, \dots, X_n)$. The random variable (possibly a vector) $Y = T(X_1, \dots, X_n)$ is called a *statistic*. The distribution of $Y$ is called the *sampling distribution* of $Y$.

The only restriction on a statistic is that it cannot be a function of a parameter.

Examples: Max value in sample, min value in sample, average sample value, sample variance.

!!! example "Example: Sample Mean"

    $$
    \hat{\mu} = \frac{1}{n} \sum_{i = 1}^n X_i
    $$

!!! example "Example: Sample Variance"

    $$
    \hat{\sigma}^2 = \frac{1}{n - 1} \sum_{i = 1}^n (X_i - \mu)^2
    $$

    The sample standard deviation is then $\hat{\sigma}$.

!!! tip "Theorem: MSE, Sample Variance"

    a. $\hat{\mu} = \argmin_a \sum_{i = 1}^n (x_i - a)^2$.

    The proof is simple. Taking partials w.r.t. $a$ to get:

    $$
    0 = \sum_{i = 1}^n (x_i - a)
    $$
    $$
    n a = \sum_{i = 1}^n x_i \implies a = \frac{1}{n} \sum_{i = 1}^n x_i
    $$

    b. $(n - 1) \hat{\sigma}^2 = \sum_{i = 1}^n (x_i - \hat{\mu})^2 = \sum_{i = 1}^n x_i^2 - n \hat{\mu}^2$.

    Proof:

    Let $S = \sum_{i = 1}^n x_i$. Then, $\hat{\mu} = \frac{1}{n} S$.

    $$
    \sum_{i = 1}^n (x_i - \hat{\mu})^2 = \sum_{i = 1}^n x_i^2 + \hat{\mu}^2 - 2 \hat{\mu} x_i
    $$

    $$
    = n \hat{\mu}^2 + \sum_{i = 1}^n x_i^2 - 2 \hat{\mu} \sum_{i = 1}^n x_i
    $$

    $$
    = n \hat{\mu}^2 + \sum_{i = 1}^n x_i^2 - 2 n \hat{\mu}^2
    $$

    $$
    = \sum_{i = 1}^n x_i^2 - n \hat{\mu}^2
    $$

!!! question "Lemma: Linearity"
    Let $X_1, \dots, X_n$ be a random sample from a population. Let $g(x)$ be a function such that $\mathbb{E}[g(X)], \text{Var}[g(X)]$ exist.

    Then,

    $$
    \mathbb{E}[\sum_{i = 1}^n g(X_i)] = n \mathbb{E}[g(X_1)]
    $$

    $$
    \text{Var}[\sum_{i = 1}^n g(X_i)] = n \text{Var}(g(X_1))
    $$

    The first statement is true for any identically distributed collection of random variables by the linearity of expectation (it does not require independence). The second statement requires both identical distributions and independence.

    Linearity of expectation follows from the linearity of a sum. We will prove the second statement now.

    $$
    \text{Var} \left ( \sum_{i = 1}^n g(X_i) \right ) = \mathbb{E} \left [ \sum_{i = 1}^n g(X_i) - \mathbb{E}[\sum_{i = 1}^n g(X_i)]\right ]^2
    $$

    $$
    = \mathbb{E} \left [  \sum_{i = 1}^n \left ( g(X_i) - \mathbb{E}[g(X_i)] \right ) \right ]^2
    $$

    We've used linearity of expectation to take the sum over $n$ expectations of $g(X_i)$.

    The outer-most expectation has a "hidden" index $j$ running over all samples. So there are $n^2$ terms total with $n$ corresponding to $\mathbb{E}[g(X_i) - \mathbb{E}[g(X_i)]]^2 = \text{Var}(g(X_1))$. These are like the diagonals of our covariance matrix.

    The other $n(n - 1)$ terms are covariances and factorize like

    $$
    \mathbb{E}[(g(X_i) - \mathbb{E}[g(X_i)]) (g(X_j) - \mathbb{E}[g(X_j)])] = \text{Cov}(g(X_i), g(X_j))
    $$

    However, since the different samples are independent, this covariance is equal to $0$. So we wind up with

    $$
    \text{Var} \left [\sum_{i = 1}^n g(X_i) \right ] = n \text{Var}(g(X_1))
    $$

!!! tip "Theorem: Sampling Distribution"
    Let $X_1, \dots, X_n$ be a random sample from a population with mean $\mu$ and variance $\sigma^2 < \infty$. Then,

    1. $\mathbb{E}[\hat{\mu}] = \mu$. The proof is simple:

    $$
    \mathbb{E}[\hat{\mu}] = \frac{1}{n} \mathbb{E}[\sum_{i = 1}^n X_i] = \mu
    $$

    2. $\text{Var}(\hat{\mu}) = \frac{\sigma^2}{n}$.

    $$
    \text{Var}(\hat{\mu}) = \frac{1}{n^2} \text{Var}(\sum_{i = 1}^n X_i) = \frac{\sigma^2}{n}
    $$

    3. $\mathbb{E}[\hat{\sigma}^2] = \sigma^2$.

    $$
    \mathbb{E}[\hat{\sigma}^2] = \mathbb{E}[\frac{1}{n - 1} \sum_{i = 1}^n (X_i - \hat{\mu})^2]
    $$
    $$
    = \frac{1}{n - 1} \mathbb{E}[\sum_{i = 1}^n (X_i - \hat{\mu})^2]
    $$

    By our previous theorem, we get:
    $$
    = \frac{1}{n - 1} \mathbb{E}[\sum_{i = 1}^n X_i^2 - n \hat{\mu}^2]
    $$
    $$
    = \frac{n}{n - 1} \mathbb{E}[X_i^2] - \mathbb{E}\hat{\mu}^2
    $$
    $$
    = \frac{n}{n - 1} (\mu^2 + \sigma^2 - (\mu^2 + \frac{\sigma^2}{n}))
    $$
    $$
    = \frac{n}{n - 1} (\sigma^2 - \frac{\sigma^2}{n})
    $$
    $$
    = \frac{n}{n - 1} \frac{(n - 1) \sigma^2}{n} = \sigma^2
    $$

The use of $n - 1$ in the definition of $\hat{\sigma}^2$ may seem unintuitive, but we have shown why we use it - it is unbiased (in that in expectation, the sample parameter converges to the population parameter). This particular correction is called the *Bessel correction*.

## Order Statistics

!!! info "Definition: Order Statistics"
    The order statistics of a random sample $X_1, \dots, X_n$ are the sample values placed in ascending order, $X_{(1)}, \dots, X_{(n)}$ where if $i < j$, $X_{(i)} < X_{(j)}$.





















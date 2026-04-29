# Random Samples

Notes on Ch. 5 of Statistical Inference by Casella and Berger.

## Definition

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

## Sample Statistics

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

    a. $\hat{\mu} = \text{argmin}_a \sum_{i = 1}^n (x_i - a)^2$.

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

## Convergence

What happens as sample size approaches infinity? We want to observe the behavior of $\hat{\mu}_n$ as $n \to \infty$.

### Convergence In Probability

!!! info "Definition: Convergence in Probability"
    A sequence of random variables $X_1, X_2, \dots$ *converges in probability* to a random variables $X$ if for every $\epsilon > 0$,

    $$
    \lim_{n \to \infty} P(|X_n - X| \geq \epsilon) = 0
    $$

We are frequently concerned with scenarios where the limiting random variable is a constant.

!!! tip "Theorem: Weak Law of Large Numbers"
    Let $X_1, X_2, \dots$ be i.i.d. random variables where $\mathbb{E}[X_i] = \mu$, $\text{Var}(X_i) < \infty$. Define $\hat{\mu}_n = \frac{1}{n} \sum_{i = 1}^n X_i$. Then for every $\epsilon > 0$,

    $$
    \lim_{n \to \infty} P(|\hat{\mu}_n - \mu| > \epsilon) = 0
    $$

!!! quote "Proof: Weak LLN"

    Chebychev's inequality: For every $\epsilon > 0$,

    $$
    P(|\hat{\mu}_n - \mu| \geq \epsilon) = P((\hat{\mu}_n - \mu)^2 \geq \epsilon^2)
    $$

    $$
    \leq \frac{\mathbb{E}[(\hat{\mu}_n - \mu)^2]}{\epsilon^2}
    $$

    $$
    = \frac{\text{Var}(\hat{\mu}_n)}{\epsilon^2}
    $$

    $$
    = \frac{\sigma^2}{n \epsilon^2}
    $$

    Then, as $n \to \infty$, $P(|\hat{\mu}_n - \mu| \geq \epsilon) \to 0$.

The Weak LLN states that as sample size approaches infinity, the sample mean converges in probability to the true mean.

**Consistency** is a property of estimators where as $n \to \infty$, the sequence of estimators converges in probability to the true parameter value.

!!! example "Example: Consistency of $S^2_n$"
    Suppose we have a sequence $X_1, X_2, \dots$ of i.i.d. random variables with mean $\mu$ and finite variance $\sigma^2$. Given that:

    $$
    S^2_n = \frac{1}{n - 1} \sum_{i = 1}^n (X_i - \bar{\mu}_n)^2
    $$

    Can we prove a WLLN for $S_n^2$?

    By Chebyshev, we have:

    $$
    P(|S^2_n - \sigma^2| \geq \epsilon) \leq \frac{\mathbb{E}[S^2_n - \sigma^2]^2}{\epsilon}
    $$

    $$
    = \frac{\text{Var}(S^2_n)}{\epsilon}
    $$

    In other words, a sufficient condition for $S_n^2$ to converge in probability to $\sigma^2$ is for $\text{Var}(S^2_n) \to 0$ as $n \to \infty$.


!!! tip "Theorem: Function Convergence"
    Suppose $X_1, X_2, \dots$ converge in probability to $X$ and $h$ is a continuous function. Then, $h(X_1), h(X_2), \dots$ converges in probability to $h(X)$.


### Almost Sure Convergence

!!! info "Definition: Almost Sure Convergence"
    A sequence of random variables $X_1, X_2, \dots$ **converges almost surely** to a random variable $X$ if for every $\epsilon > 0$,

    $$
    P(\lim_{n \to \infty} |X_n - X| < \epsilon) = 1
    $$

This type of convergence is stronger than convergence is probability (similar to pointwise convergence of a sequence).

A rando variable is a real-valued function on a sample $S$ where $X_n(s)$ and $X(s)$ are functions defined over $S$. $X_n$ converges almost surely to $X$ if the functions $X_n(s)$ converges to $X(s)$ for all $s \in S$ except for $s \in N$ where $N \subset S$ and $P(N) = 0$.

!!! example "Example: A.S. Convergence"
    Let $S = [0, 1]$ with a uniform distribution. Define $X_n(s) = s + s^n$ and $X(s) = s$. For all $s \in [0, 1), s^n \to 0$ as $n \to \infty$ and $X_n(s) \to s = X(s)$. For the point $1$, $X_n(1) = 2$ for all $n$ so $X_n(1)$ doesn't converge to $1$. However, $P[0, 1) = 1$ so $X_n$ converges to $X$ almost surely.

!!! example "Example: Convergence in Probability, not almost surely"
    Again, let $S = [0, 1]$ with a uniform distribution. Define

    $$
    X_1(s) = s + I_{[0, 1]}(s)
    $$

    $$
    X_2(s) = s + I_{[0, 1 / 2]}(s), X_3(s) = s + I_{[1/2, 1]}(s)
    $$

    $$
    X_4(s) = s + I_{[0, 1 / 3]}(s), X_5(s) = s + I_{[1/3, 2/3]}(s), X_6(s) = s + I_{[2/3, 1]}(s)
    $$

    Let $X(s) = s$. The sequence $(X_n)$ iterates over the $[0, 1]$ interval several times. Each time, it's value is either $s$ or $1 + s$ assuming s happens to fall in a vanishingly small interval.

    Convergence in probability looks at the limit of the probability. Specifically, $\lim_{n \to \infty} P(|X_n - X| \geq \epsilon)$. We can characterize $P(|X_n - X| \geq \epsilon)$ by observing that for each "pass" of the $[0, 1]$ interval that only $\frac{1}{n}$ interval will produce an estimate equal to $1 + s$. However, the number of intervals continues to grow so in the limit, this probability goes to $0$. Hence, we have convergence in probability.

    However, we do not have a.s. convergence as the sequence doesn't even converge - there is no radius $\epsilon$ and point $N$ after which all points indexed by $n > N$ live entirely inside the $\epsilon$-ball. There will always be some point $s'$ such that $X_n(s') = 1 + s'$ (due to $s'$ always existing in of our intervals). 






!!! info "Definition: Convergence in Distribution"
    A sequence of random variables $X_1, X_2, \dots$ *converges in distribution* to $X$ if

    $$
    \lim_{n \to \infty} F_{X_n}(s) = F_X(s)
    $$

    where $F_X(x)$ is continuous.

























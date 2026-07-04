# 01 - Itô Integral

Consider a gambling sequence - at each step, toss a fair coin. For $i = 1, 2, \dots$, let $\Delta W_i$ be the outcome of the $i$'th toss where

$$
\Delta W_i \sim_{\text{i.i.d.}} P(\Delta W_i = \pm 1) = \frac{1}{2}
$$

Before each coin toss, place a stake $X_{i - 1}$. If $\Delta W_i = 1$, you win $X_{i - 1}$ and if $\Delta W_i = -1$, you lose $X_{i - 1}$.

The gambler's wealth after $n$ steps is

$$
Y_n = \sum_{i = 1}^n X_{i - 1} \Delta W_i
$$

This is basically the Itô Integral in the discrete form. The goal is to define stochastic integrals in continuous time:

$$
Y_n = \sum_{i = 1}^n X_{i - 1} \Delta W_i \rightsquigarrow Y_t = \int_{0}^t X_s dW_s
$$

We identify the assumption **non-anticipation**. $X_{i - 1}$ cannot rely on future outcomes $\Delta W_{j > i}$.

## Random Walk

In the discrete setting, the process $W$ is called a random walk.

!!! info "Definition: Symmetric Simple Random Walk"

    We define the **symmetric simple walk** $\{W_n\}_{n = 0, 1, 2, \dots}$ as

    $$
    W_n = \sum_{i = 1}^n \Delta W_i, n = 1, 2, \dots; W_0 = 0
    $$

Here, $\Delta W_i$ carries the same meaning as defined in the previous section (hence why the walk is symmetric). We can immediately identify that

- $\mathbb{E}[W_n] = 0$ (by linearity of expectation).

- The variance of $\Delta W_i$ is $1$ (this is Rademacher, not Bernoulli) and by additivity of variance under independence, $\text{Var}(W_i) = n \text{Var}(\Delta W_i) = n$.

- Since $W_n$ is a sum of i.i.d. random variables, $W_n \sim \mathcal{N}(0, n)$ by CLT.

With these observations, we can construct a continuous analogue.

## Brownian Motion

This is a continuous time stochastic process taking continuous values, a limit of the random walk.

!!! info "Definition: Brownian Motion"

    The **standard Brownian motionn (Wiener process)** is a continuous-time real-valued stochastic process $\{W_t\}_{t \geq 0}$ with the following properties:

    - $W_0 = 0$.

    - $\{W_t\}$ has continuous sample path with probability one - the trajectories are almost always continuous.

    - $\{W_t\}$ has stationary, normally distributed increments. For $0 \leq s < t$,

    $$
    W_t - W_s \sim \mathcal{N}(0, t - s)
    $$

    - $\{W_t\}$ has independent increments. Increments on non-overlapping time intervals are statistically independent.

From this definition, we can show (informally) that Brownian motion is nowhere differentiable.

$$
\frac{\Delta W_t}{\Delta t} = \frac{W_{t + \Delta t} - W_t}{\Delta t} \sim \frac{1}{\Delta t} \mathcal{N}(0, \Delta t) = \mathcal{N}(0, \frac{1}{\Delta t})
$$

In the limit as $\Delta t \to 0$, the variance explodes. We say that in an $L^2$ sense, the derivative of Brownian motion does not exist. This non-differentiability requires a new calculus including a new chain rule, a new product rule, etc.

## Itô Integral

!!! info "Definition: Itô Integral"

    For $i = 0, 1, \dots, n$, let $t_i = i \Delta t = \frac{i t}{n}$.

    $$
    \int_{0}^t X_s dW_s := \lim_{n \to \infty} \sum_{i = 1}^n X_{t_{i - 1}} (W_{t_i} - W_{t_{i - 1}}) = \lim_{n \to \infty} \sum_{i = 1}^n X_{i - 1} \Delta W_i
    $$

    We divide the time interval $[0, t]$ into $n$ sub-intervals each with length $\Delta t$. Looking at the summand on the middle term, $X$ is evaluated at the left endpoint of the current interval $X_{t_{i - 1}}$ and is multiplied against the increment of the Brownian motion in that period. This is like approximating an integral using the **left** Riemann sum.

Here, the limit (and stochastic convergence) are in reference to $L^2$ convergence.

!!! info "Definition: Mean Square Convergence"

    A sequence $(\xi_n)$ of RVs is said to convergence to an rv $\xi$ in **mean square** if for all $N$, $\mathbb{E}[\xi_n]^2 < \infty, \mathbb{E}[\xi]^2 < \infty$ and

    $$
    \lim_{n \to \infty} \mathbb{E}[(\xi_n - \xi)^2] = 0
    $$

## Integrals

!!! example "Example: Constant Function"

    Let

    $$
    Y_t = \int_{0}^t f(s) dW_s = \lim_{n \to \infty} \sum_{i = 1}^n f_{i - 1} \Delta W_i
    $$

    where $f(s)$ only depends on time. Specifically, suppose $f(s) = c$ is a constant function. Then, we get:

    $$
    Y_t = \lim_{n \to \infty} \sum_{i = 1}^n c \Delta W_i
    $$

    $$
    = \lim_{n \to \infty} \sum_{i = 1}^n c (W_{t_{i}} - W_{t_{i - 1}})
    $$

    This is a telescoping sum and we end up with

    $$
    = \lim_{n \to \infty} c (W_{t_n} - W_0)
    $$

    $$
    = \lim_{n \to \infty} c W_{t_n} = c W_t
    $$


Generally, if $f$ is not constant, $Y_t$ will not have a closed-form formula. Still, $Y_t$ is a
Gaussian RV with $\mathbb{E}[Y_t] = 0$ (by linearity of expectation=) with variance:

$$
\text{Var}(Y_t) = \lim_{n \to \infty} \sum_{i = 1}^{n} f_{i - 1}^2 \text{Var}(\Delta W_i)
$$

$$
= \lim_{n \to \infty} \sum_{i = 1}^{n} f_{i - 1}^2 \Delta t = \int_{0}^t f^2(s) ds
$$

The variance of $\Delta W_i$ is $\Delta t$ by the stationary increment property.

## Summary

$$
\int_0^t c dW_s = cW_t
$$

$$
\int_0^t \exp(\theta_s) dW_s \sim \mathcal{N}(0, \int_{0}^t \exp(2 \theta_s) ds) = \mathcal{N}(0, \frac{\exp(2^{\theta}_t) - 1}{2 \theta})
$$
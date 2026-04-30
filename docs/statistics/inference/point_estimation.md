# Point Estimation

## Estimators

!!! info "Definition: Point Estimator"
    A *point estimator* is any function $W(X_1, \dots, X_n)$ of a sample: any statistic is a point estimator.

An *estimator* is a function of the sample. An *estimate* is a realized value of an estimator obtained once the sample is actually taken. Estimator is $W(X_1, \dots, X_n)$ while estimate is $w(x_1, \dots, x_n)$.

As an example, the sample mean is an estimator of the population mean.

### Method of Moments

Let $X_1, \dots, X_n$ be a sample from a population with distribution $f(x \mid \theta_1, \dots, \theta_k)$. *Method of Moment* estimators are found from equating the first $k$ sample moments against the corresponding $k$ population moments and solving the system of equations. Define

$$
m_1 = \frac{1}{n} \sum_{i = 1}^n X_i^1, \mu_1 = \mathbb{E}[X^1]
$$
$$
m_k = \frac{1}{n} \sum_{i = 1}^n X_i^k, \mu_k = \mathbb{E}[X^k]
$$

!!! example "Example: Normal MoM"
    Suppose $X_1, \dots, X_N \sim \mathcal{N}(\theta, \sigma^2)$. We have $m_1 = \hat{\mu}, m_2 = \frac{1}{n} \sum X_i^2, \mu_1 = \theta, \mu_2 = \theta^2 + \sigma^2$.

    We want to solve:
    $$
    $\hat{\mu} = \theta, \frac{1}{n} \sum X_i^2 = \theta^2 + \sigma^2
    $$

    We get:
    $$
    \hat{\theta} = \hat{\mu}, \hat{\sigma}^2 = \frac{1}{n} \sum X_i^2 - \hat{\mu}^2 = \frac{1}{n} \sum (X_i - \hat{\mu})^2
    $$

### Maximum Likelihood Estimation

Recall that if $X_1, \dots, X_n$ are i.i.d. sampled from a population with distribution $f(x \mid \theta_1, \dots, \theta_k)$, the likelihood function is defined as:

$$
L(\theta \mid x) = L(\theta_1, \dots, \theta_k \mid x_1, \dots, x_n) = \prod_{i = 1}^n f(x_i \mid \theta_1, \dots, \theta_k)
$$

!!! info "Definition: MLE"
    For each sample point $\mathbf{x}$, let $\hat{\theta}(\mathbf{x})$ be a parameter value at which $L(\theta \mid \mathbf{x})$ obtains its maximum w.r.t. $\theta$ with $\mathbf{x}$ held fixed. A *maximum likelihood estimator* (MLE) of $\theta$ based on this sample is $\hat{\theta}(\mathbf{X})$.

This is the parameter point for which the observed sample is most likely. Statistical drawbacks include that a) finding the global maximum is hard and b) the estimate may be numerically sensitive to small changes in data.

## Bayes Estimator

Classically, the parameter $\theta$ is thought to be a unknown but fixed quantity. A random sample $X_1, \dots, X_n$ is drawn from a population parameterized by $\theta$ and based on the sample, information about $\theta$ is inferred.

In the Bayesian approach, $\theta$ itself is a random variable. We place a *prior distribution* representing our beliefs about likely values of $\theta$ before seeing any data. Then, upon observation of a sample, we update our beliefs to obtain a *posterior distribution*. This process is called **Bayesian Inference** and is done via Bayes Rule.

!!! tip "Theorem: Bayes"
    Let $\pi(\theta)$ be a prior distribution and the sampling distribution be given by $f(x \mid \theta)$. Then, the posterior distribution is given be

    $$
    \pi(\theta \mid x) = \frac{f(x \mid \theta) \pi(\theta)}{m(x)}
    $$

    $$
    m(x) = \int f(x \mid \theta) \pi(\theta) d\theta
    $$

The posterior distribution tells us about the distribution of $\theta$ conditional on observed data.

## Expectation Maximization

## Estimator Evaluation

!!! info "Definition: MSE"
    The *mean squared error* (MSE) of an estimator $W$ of some parameter $\theta$ is defined as:

    $$
    MSE(W) = \mathbb{E}_{\theta}[(W - \theta)^2]
    $$

    This measures average squared difference between $W$ and the parameter $\theta$. MSE is analytically tractable and admits the bias-variance decomposition.

    $$
    \mathbb{E}_{\theta}[(W - \theta)^2] = \text{Var}_{\theta}(W) + \mathbb{E}_{\theta}[W - \theta]^2 = \text{Var}_{\theta}(W) + \text{Bias}_{\theta}(W)^2
    $$

!!! info "Definition: Bias"
    The bias of a point estimator $W$ of some parameter $\theta$ is the difference in the expected value of $W$ and $\theta$:

    $$
    \text{Bias}_{\theta}(W) = \mathbb[E]_{\theta}(W) - \theta
    $$

Therefore, an unbiased estimator has an MSE equal to its variance.








# Deep Generative Models

[TOC]

## EBM


The following is taken from How to Train Your Energy-Based Models by Song & Kingma[^song2021].

Probabilistic models require a *tractable likelihood*. This allows for straightfoward comparison between models and optimization via MLE. Even if the likelihood isn't completely tractable, we can often optimize a *variational lower-bound* on the likelihood.

Models with tractable likelihoods are constrained in that they are defined as a sampling procedure. Auto-regressive models factorize the joint distribution as a product of conditional distributions. Flow-based models model the data distribution as a sequence of invertible transformations from some base distribution.

**Energy-based models** only specify the unnormalized negative log-probability called the *energy function*. The energy function need not integrate to $1$ and can be parameterized with any non-linear regression function. While they are more flexible, absent an exact likelihood / sampling procedure, training is difficult.

This paper presents three methods for training EBMs - MCMC sampling, Score Matching, and Noise Contrastive Estimation.

!!! info "Definition: Energy Based Models"
    EBMs specify a energy function $E_{\theta}(x)$. The probability density of some sample $x$ is given by:

    $$
    p_{\theta}(x) = \frac{\exp(-E_{\theta}(x))}{Z_{\theta}}
    $$

    $$
    Z_{\theta} = \int \exp(- E_{\theta}(x)) dx
    $$

    The partition function is constant w.r.t. $x$ but is a function of $\theta$.

### EBM Motivation

We take a brief detour for motivation and show we can derive EBMs from the principle of *maximum entropy*. Consider the following variational problem over the space of distributions $\Delta$.

$$
\max_{P \in \Delta} H(P) = \int P(x) \log \frac{1}{P(x)} dx, \ \E_{P(x)}[f(x)] = \mu
$$

where $f$ is some vector of statistics. Why maximum entropy? Suppose you know some data statistics (mean, variance). The maximum entropy principle states to pick the distribution with the highest entropy while still matching those statistics - any lower-entropy distribution is making assumptions about where the distribution is concentrated without evidence.

We can solve MaxEnt via calculus of variations, associating with the functional:

$$
\mathcal{L}(P, \alpha, \eta) = \int P(x) \log \frac{1}{P(x)} dx - \alpha \left(
\int P(x) dx - 1 \right) - \left ( \eta^T \E_{P(x)}[f(x)] - \mu \right )
$$

with Lagrange multipliers $\alpha, \eta$. The entropy attains its maximum when:

$$
\frac{\delta \mathcal{L}}{\delta P} P = \log P(x) + 1 - \alpha - eta^T f(x) = 0
$$

Solving for $P(x)$, we get:

$$
\log P(x) = \eta^T f(x) + \alpha - 1 \implies P(x) \propto \exp(\eta^T f(x))
$$

To show this is a maximum, you can take the second variation. This is the form of the exponential family and why EBMs take a similar form.

EBMs have advantages. They can be easily combined:

$$
P_1(x) \propto \exp(f_{\theta_1}(x)), P_2(x) \propto \exp(f_{\theta_2}(x))
$$

Then, $P(x) \propto P_1(x) P_2(x) \propto \exp(f_{\theta_1}(x) + f_{\theta_2}(x))$.

It is also easy to analyze relationships between different coordinates. Suppose $x, y$ represent different data types. Then, $P(x, y) \propto \exp(\psi(y)^T \varphi(y))$.

However, they have several disadvantages. They're hard to sample from (MCMC), hard to evaluate (due to intractability of $Z_{\theta}$) and hard to learn due to $Z_{\theta}$.

### Training - MCMC

We return to the paper and present how train your EBM. Specifically, we can do maximum likelihood training with MCMC sampling, Score Matching, and Noise Contrastive Estimation. We begin with MCMC.

MLE proceeds like $\E_{x \sim p_{\text{data}}(x)[ \log p_{\theta}(x)]}$. Maximizing likelihood is equivalent to minimizing KL-divergence between $p_{\text{data}}(x)$ and $p_{\theta}(x)$:

$$
- \E_{x \sim p_{\text{data}}(x)}[ \log p_{\theta}(x)] = D_{\text{KL}}(p_{\text{data}}(x) \mid \mid p_{\theta}(x)) - \E_{x \sim p_{\text{data}}(x)}[\log p_{\text{data}}(x)]
$$

The last term is constant w.r.t. $\theta$ so optimizing likelihood is minimizing the KL-divergence between the model's distribution and the data distribution.

EBMs cannot compute likelihoods since they don't have access to $Z_{\theta}$. However, with MCMC procedures, they can estimate the gradient of the log-likelihood and perform gradient ascent to do likelihood maximization. Intuitively, we want the network to assign low-energy to observed samples and high-energy everywhere else.

In particular,

$$
\nabla_{\theta} \log p_{\theta}(x) = \nabla_{\theta} (- E_{\theta}(x) - \log Z_{\theta})
$$

$$
= - \nabla_{\theta} E_{\theta}(x) - \E_{x \sim p_{\theta}(x)}[- \nabla_{\theta} E_{\theta}(x)]
$$

The first term on the RHS is $- \nabla_{\theta} E_{\theta}[x_{\text{data}}]$ in other words, seeking to decrease energy at the real data.

The second term is $\nabla_{\theta} E_{\theta}[x_{\text{model}}]$, seeking to increase energy for the model samples. Raising energy just for model samples is enough because that's the area the model currently assigns low energy (when it should assign high energy).

Eventually, once the model samples are similar to the real data, the two gradients cancel out.

The first term can be evaluated via auto-differentiation. Recall that for an exponential family, $\frac{d A(\eta)}{d \eta} = \E_{\eta}[T(x)]$. In this case, the integrand is $\exp(\eta^T T(x))$ and its derivative w.r.t. $\eta$ is $T(x) \exp(\dots)$. In EBMs, the integrand is $\exp(-E_{\theta}(x))$ and the derivative doesn't have a closed form so it's just $- \nabla_{\theta} E_{\theta}(x) \exp(\dots)$. Therefore,

$$
\nabla_{\theta} \log Z_{\theta} = \E_{x \sim p_{\theta}(x)}[- \nabla_{\theta} E_{\theta}(x)]
$$

Using MCMC procedures we can sample $\tilde{x} \sim p_{\theta}(x)$. Then, we can compute our estimate of the gradient of the log-partition function as $\nabla_{\theta} \log Z_{\theta}(x) \approx - \sum_{i = 1}^k \nabla_{\theta} E_{\theta}(\tilde{x})$ and do gradient ascent.

!!! quote "Important: Maximum Likelihood vs Marginal Likelihood"
    The term $Z(\theta)$ is the partition function integrating over data points $x$. Although it is a normalizing constant, it is distinct from the *marginal likelihood* which integrates over parameters $\theta$.

We naturally have access to the first term using auto-diff. Since the second term is just the gradient of the EBM w.r.t. $\theta$ where $x$ is sampled from the model's learned distribution of data, as long as we can draw random samples, we can perform gradient ascent on the log-likelihood w.r.t. $\theta$.


!!! abstract "Algorithm: MCMC for MLE"
    We want to optimize

    $$
    \nabla_{\theta} \log p_{\theta}(x) = - \nabla_{\theta} E_{\theta}(x) + \E_{x \sim p_{\theta}(x)}[\nabla_{\theta} E_{\theta}(x)]
    $$

    Start with $\theta_t$.

    1. Draw real data $x_1, \dots, x_n \sim p_{\text{data}}(x)$.
    2. Draw $m$ samples from the model using Langevin MCMC. Specifically, sample noise $\tilde{x}^0$ and repeat:

        $$
        \tilde{x}^{k + 1} \leftarrow \tilde{x}^k - \frac{\epsilon^2}{2} \nabla_x E_{\theta_t}(\tilde{x}^k) + \epsilon z, \ z \sim \mathcal{N}(0, I)
        $$

    3. Compute gradient estimate

        $$
        \hat{\nabla}_{\theta_t} = - \frac{1}{n} \sum_{i = 1}^n \nabla_{\theta_t} E_{\theta_t}(x_i) + \frac{1}{m} \sum_{j = 1}^m \nabla_{\theta_t} E_{\theta_t}(\tilde{x}_j)
        $$

    4. Update

    $$
    \theta_{t + 1} \leftarrow \theta_t + \eta \hat{\nabla}_{\theta_t}
    $$

In short, we use real data to compute the gradient of the negative energy (assign lower energy to real samples). We then generate samples from the network (doing gradient descent on the learned energy landscape) to estimate the gradient of the partition function. Then, we can add the two to get a gradient estimate of the log-likelihood.

Note that this is merely for density estimation, i.e. learning $p(x)$ to get a generative model. For supervised learning, energy takes the input and label and defines $E_{\theta}(x, y)$. The normalizing constant sums over labels $y$. In a discrete classification scenario, thisis just a standard classification model. In a continuous or structured $y$, the normalizing constant becomes intractable again.

### Score Matching

If two continuously differentiable real-valued functions $f(x)$ and $g(x)$ have equal first derivatives everywhere, then $f(x) = g(x) + C$. When $f(x)$ and $g(x)$ are log density functions with equal first derivatives, then they have equivalent normalizing constants and $f(x) = g(x)$. Therefore, one can learn an EBM by matching the first derivative of its log-PDF with the first derivative of the log-PDF of the data distribution. This is called **score matching**[^hyvarinen2005].

Recall:

$$
\nabla_x \log p_{\theta}(x) = - \nabla_x E_{\theta}(x) - \nabla_{x} \log Z_{\theta} = - \nabla_x E_{\theta}(x)
$$

since the partition function is constant w.r.t $x$.
!!! info "Definition: Score Matching (Fisher)"
    Let $p_{\text{data}}$ be the data distribution. The basic Score Matching objective minimizes the *Fisher Divergence*:

    $$
    D_F(p_{\text{data}}(x) \mid \mid p_{\theta}(x)) = \E_{p_{\text{data}}(x)} \left [
    \frac{1}{2} || \nabla_x \log p_{\text{data}}(x) - \nabla_x \log p_{\theta}(x)||^2
    \right ]
    $$

This is impractical since we typically don't have access to $\nabla_x \log p_{\text{data}}(x)$. Under regularity conditions, the Fisher divergence can be re-written using integration by parts:

$$
D_F(p_{\text{data}}(x) \mid \mid p_{\theta}(x)) =  \E_{p_{\text{data}}(x)} \left [
\frac{1}{2} \sum_{i = 1}^d \left ( \frac{\partial E_{\theta}(x)}{\partial x_i} \right )^2 + \frac{\partial^2 E_{\theta}(x)}{(\partial x_i)^2}
\right ]
$$

$$
= \E_{p_{\text{data}}(x)} [\text{Tr}(\nabla^2_x E_{\theta}(x)) + \frac{1}{2} || \nabla_x E_{\theta}(x) ||^2]
$$

where $d$ is the dimensionality of $x$ and $\nabla^2_x E_{\theta}(x)$ is the Hessian of the energy w.r.t. $x$. Naturally, for high-dimensionality, the Hessian is very expensive to compute.

#### Denoising Score Matching

The score matching objective requires regularity conditions for $\log p_{\text{data}}(x)$ (continuously differentiable, finite everywhere). However, a distribution of images is discrete and bounded - $\log p_{\text{data}}$ is discontinuous and negative infinity outside the range.

Thus, we can add a bit of noise to each data point, $\tilde{x} = x + \epsilon$. As long as $p(\epsilon)$ is smooth, the noisy data distribution, $q(\tilde{x}) = \int q(\tilde{x} \mid x) p_{\text{data}}(x) dx$ is smooth and the Fisher divergence $D_F(q(\tilde{x}) \mid \mid p_{\theta}(\tilde{x}))$ is a proper objective.

Vincent[^vincent2011] showed that:

$$
D_F(q(\tilde{x}) \mid \mid p_{\theta}(\tilde{x})) = \E_{q(\tilde{x})} \left [
\frac{1}{2} || \nabla_x \log q(\tilde{x}) - \nabla_x \log p_{\theta}(\tilde{x}) ||_2^2
\right ]
$$

$$
= \E_{q(x, \tilde{x})} \left [
\frac{1}{2} || \nabla_x \log q(\tilde{x} \mid x) - \nabla_x \log p_{\theta}(\tilde{x}) ||_2^2
\right ]
$$

This completely avoids the unknown term and second-order derivatives. Formulas can be traced back to Tweedie's formula and SURE (Stein's Unbiased Risk Estimation).

When $p_{\text{data}}$ is already well-behaved and satisfies the regularity conditions given by Score Matching, $D_F(q(\tilde{x}) \mid \mid p_{\theta}(\tilde{x})) \neq D_F(p_{\text{data}}(x) \mid \mid p_{\theta}(x))$. The optimal EBM matches the noisy distribution and not the data distribution.


### NCSN

The following is taken from "Generative Modeling by Estimating Gradients of the Data Distribution" by Song & Ermon[^song2019].

Score-matching is not scalable due to the computation of $\text{Tr}(\nabla_x s_{\theta}(x))$. Denoising score-matching cirucmvents the trace computation *but* the optimal score network only learns the score of the data distribution at very low noise levels. Sliced score-matching is more expensive than regular score-matching.

Generally, score-based generative modeliing faces two major obstacles.

1. The manifold hypothesis suggests that the data distribution is clustered on a low-dimensional manifold embedded in a higher-dimensional ambient space. First, the score is a gradient taken in the *ambient space* meaning it is undefined when confining $x$ to the low-dimensional space. Second, the score-matching objective only provides a *consistent* estimator when the support of the data distribution is the ambient space.

2. In regions of low data density, score matching is too low sample to estimate the score accurately. This means that Langevin dynamics (which we use to sample from the model, like in the EBM section) may not be able to traverse low-density regions to go from one mode to another.

![](../../images/low_sample_score.png){ .center width="400" }

**Noise Conditional Score Networks** find that perturbing the data with random Gaussian noise makes the data distribution easier to model. It means the perturbed data distribution isn't confined to the low-dimensional manifold making score-estimation well-defined. Gaussian noise also fills the low-density regions. By using multiple levels of noise, NCSN achieves a sequence of noise-perturbed distributions which converge to the true data distribution.

!!! info "Definition: Noise Conditional Score Networks"
    Consider a sequence of noise levels $\sigma_1, \dots, \sigma_L$ where $\sigma_j / \sigma_{j + 1} > 1$. So $\sigma_1$ corresponds to a high-noise level and $\sigma_L$ to a low-noise level.

    Let $q_{\sigma}(\tilde{x}) = \int p_{\text{data}}(x) \ \mathcal{N}(\tilde{x} \mid x, \sigma^2 I) \ dx$ be the perturbed data distribution. We want to train a conditional score network to jointly estimate the scores of all perturbed data distributions,

    $$
    s_{\theta}(x, \sigma) \approx \nabla_x \log q_{\sigma}(x)
    $$

    The noise distribution is $q_{\sigma}(\tilde{x} \mid x) = \mathcal{N}(\tilde{x} \mid x, \sigma^2 I)$. Therefore, $\nabla_{\tilde{x}} \log q_{\sigma}(\tilde{x} \mid x) = - \frac{\tilde{x} - x}{\sigma^2}$. For a given $\sigma$, the objective (taken from DSM) is:

    $$
    l(\theta, \sigma) = \frac{1}{2} \E_{p_{\text{data}}} \E_{\tilde{x} \sim \mathcal{N}(x, \sigma^2 I)} \left [
    \left | \left | s_{\theta}(\tilde{x}, \sigma) + \frac{\tilde{x} - x}{\sigma^2} \right | \right |_2^2
    \right ]
    $$

    We combine this for all $\sigma$ to get:

    $$
    L(\theta, \{\sigma_i\}_{i = 1}^L) = \frac{1}{L} \sum_{i = 1}^L \lambda(\sigma_i) l(\theta, \sigma_i)
    $$

    where $\lambda(\sigma_i)$ is a coefficient function dependeing on $\sigma_i$.

In the loss derived in DSM, the network was trained such that the *score of the network* matched the score of the single noise-perturbed distribution. Generally, EBMs produce a scalar $E_{\theta}(x)$ and the score is derived from a backwards pass. NCSNs directly output a $d$-dimensional vector and are parameterized to directly predict the score of the noise-perturbed distribution.

![alt text](../../images/annealed_langevin.png){ .center width="400" }

The idea of progressively de-noising will be revisited soon. These models are known as **diffusion models**.


## VAE

### AutoEncoder

Reference: Auto-Encoding Variational Bayes by Kingma & Welling[^kingma2013].

!!! info "Definition: Auto-Encoder"
    An **autoencoder** is a model that takes some vector $x$, compresses it into a lower-dimensional vector $z$ and decompresses $z$ back to $x$. Here,

    $$
    z = h_{\phi}(x), x' = f_{\theta}(z)
    $$

    Here, $h_{\phi}$ is an encoder and $f_{\theta}$ is a decoder. Typically, both functions are neural networks.

The parameters $\{\theta, \phi\}$ are learned jointly, typically via something like MSE:

$$
L_{\text{AE}}(\theta, \phi) = \frac{1}{n} \sum_{i = 1}^n (x_i - f_{\theta}(h_{\phi}(x_i)))^2
$$

### Variational Bayes

**Variational Auto-Encoders** are like probabilistic versions of autoencoders. The following derivation is taken from From Autoencoder to Beta-VAE by Lilian Weng (Lil'Log)[^weng2018].

A VAE can be viewed as a directed PGM $z \to x$. Instead of taking some input $x$ into a fixed vector $z$, we map it to a posterior distribution $p_{\theta}(z \mid x)$. This requires a prior $p(z)$ and a likelihood $p_{\theta}(x \mid z)$. The likelihood function is a conditional distribution parameterized by $\theta$ called the **decoder**.

Suppose we know the real $\theta^*$ for this distribution. To sample some $x_i$, we:

1. Sample $z_i \sim p(z)$.

2. Sample $x_i \sim p_{\theta^*}(x \mid z = z_i)$.

The optimal parameter $\theta^*$ is the one that maximizes the probability of real data samples:

$$
\theta^* = \argmax_{\theta} \prod_{i = 1}^n p_{\theta}(x_i)
$$

$$
= \argmax_{\theta} \sum_{i = 1}^n \log p_{\theta}(x_i)
$$

$$
= \argmax_{\theta} \sum_{i = 1}^n \log \int p_{\theta}(x_i \mid z) p(z) dz
$$

This integral is analytically intractable but crucially, hard to estimate. We want to estimate $\int p_{\theta}(x_i \mid z) p(z) dz$. Ideally, we could just sample $z \sim p(z)$ and then compute the density $p(x_i \mid z = z)$ and multiply the densities together. Then, we should just average those to estimate $p_{\theta}(x_i)$.

The problem is that $p_{\theta}(x_i \mid z = z), z \sim p(z)$ is nearly always $0$. Randomly sampled latents from the prior basically have zero chance of producing the observed data. Generally, the $z$'s that are likely to produce the observed $x$ occupy a tiny fraction of the prior's probability so the estimate has very high variance. As a consequence, rejection-sampling also won't work since our rejection rate will be too high.

We need to do importance sampling. Ideally, we want some tractable proposal distribution $q(z)$ which puts a lot of probability on the $z$'s that could generate $x_i$'s.

$$
p_{\theta}(x_i) = \E_{z \sim q(z)} \left [ p_{\theta}(x_i \mid z) \cdot \frac{p(z)}{q(z)} \right ]
$$

The best proposal is the posterior $p_{\theta}(z \mid x_i)$ as it ensures that the weights are just the likelihoods themselves $p_{\theta}(x_i)$. However,

$$
p_{\theta}(z \mid x) = \frac{p_{\theta}(x \mid z) p(z)}{p_{\theta}(x)}
$$

so this quantity assumes we already have access to the likelihood $p_{\theta}(x)$. Instead, we can train an encoder network $q_{\phi}(z \mid x)$ meant to approximate the posterior distribution. This can stabilize our likelihood estimate.

We can use KL-Divergence to do this (specifically, the reverse KL):

$$
\min_{\phi} D_{\text{KL}}(q_{\phi}(z \mid x) \mid \mid p_{\theta}(z \mid x))
$$

We need to use the reverse KL as we do not have the ability to sample from $p_{\theta}(z \mid x)$ and the forward KL is an expectation over the true posterior. The goal here is to isolate all of the terms we cannot compute on one side. This involves $p_{\theta}(x)$ and $p_{\theta}(z \mid x)$.

$$
\begin{aligned}
&= \int q_{\phi}(z \mid x) \log \frac{q_{\phi}(z \mid x)}{p_{\theta}(z \mid x)} dz \\
&= \int q_{\phi}(z \mid x) \log \frac{q_{\phi}(z \mid x) p_{\theta}(x)}{p_{\theta}(z, x)} dz \\
&= \int q_{\phi}(z \mid x) \left (\log p_{\theta}(x) + \log \frac{q_{\phi}(z \mid x)}{p_{\theta}(z, x)} \right ) dz \\
&= \log p_{\theta}(x) + \int q_{\phi}(z \mid x) \log \frac{q_{\phi}(z \mid x)}{p_{\theta}(z, x)} dz \\
&= \log p_{\theta}(x) + \int q_{\phi}(z \mid x) \log \frac{q_{\phi}(z \mid x)}{p_{\theta}(x \mid z) p(z)} \\
&= \log p_{\theta}(x) + \E_{q_{\phi}(z \mid x)} \left [
    \log \frac{q_{\phi}(z \mid x)}{p(z)} - \log p_{\theta}(x \mid z)
\right ] \\
&= \log p_{\theta}(x) + D_{\text{KL}}(q_{\phi}(z \mid x) \mid \mid p(z)) - \E_{q_{\phi}(z \mid x)}[\log p_{\theta}(x \mid z)]
\end{aligned}
$$

Rearranging, we have:

$$
\log p_{\theta}(x) - D_{\text{KL}}(q_{\phi}(z \mid x) \mid \mid p_{\theta}(z \mid x)) = \E_{q_{\phi}(z \mid x)}[\log p_{\theta}(x \mid z)] - D_{\text{KL}}(q_{\phi}(z \mid x) \mid \mid p(z))
$$

When learning the true distribution, we want to maximize the log-likelihood while minimizing the difference between the approximated and true posterior. Thus, our loss is:

$$
\begin{aligned}
L_{\text{VAE}}(\theta, \phi) &= - \log p_{\theta}(x) + D_{\text{KL}}(q_{\phi}(z \mid x) \mid \mid p_{\theta}(z \mid x)) \\
&= - \E_{q_{\phi}(z \mid x)}[\log p_{\theta}(x \mid z)] + D_{\text{KL}}(q_{\phi}(z \mid x) \mid \mid p(z))
\end{aligned}
$$

This loss function is known as the **ELBO** or the *evidence lower bound*. It's a lower-bound - since KL-Divergence is always non-negative:

$$
- L_{\text{VAE}}(\theta, \phi) = \log p_{\theta}(x) - D_{\text{KL}}(q_{\phi}(z \mid x) \mid \mid p_{\theta}(z \mid x)) \leq \log p_{\theta}(x)
$$

By minimizing the loss, we are maximizing a lower bound on the log-likelihood.

### Reparameterization

The ELBO involves expectations which involve sampling $z \sim q_{\phi}(z \mid x)$. In this form, we cannot backpropagate to compute gradients. We use the reparameterization trick. Suppose $z \sim q_{\phi}(z \mid x_i) = \mathcal{N}(z; \mu_i, \sigma^2_i I)$. We can set $z = \mu + \sigma \odot \mathcal{N}(0, I)$.

We directly set the encoder to output two $d$-dimensional vectors, corresponding to the mean $\mu_{\phi}$ and the diagonal covariance $\log \sigma_{\phi}$.

### Summary

In short, in order to do MLE, we needed to estimate the likelihood $p_{\theta}(x)$ which would've required marginalizing over all latents $z$. This integral is analytically intractable and hard to estimate via sampling - $z$'s sampled from the prior are very unlikely to produce the observed $x$ so our likelihood estimate of $p_{\theta}(x)$ is very high variance. We need to do importance sampling and choose an appropriate proposal distribution. Ideally, we would like to sample from the posterior but that requires knowing the likelihood $p_{\theta}(x)$ in the first place.

Instead, we can optimize the reverse KL-divergence between a learned posterior and the actual posterior. After isolating inaccessible terms, we end up with a regularized reconstruction objective which jointly trains both the encoder and decoder at the same time (minimizing an upper bound (NELBO) on the NLL). The result is a generative model which is able to produce realistic samples starting with latents sampled from the prior.



## GAN

## Normalizing Flows


## Appendix

### Sliced Score Matching

Instead of minimizing Fisher divergence, **Sliced Score Matching** minimizes the sliced Fisher divergence.

!!! info "Definition: Sliced Score Matching"
    Randomly sample a projection $v$. Take the inner-product between $v$ and the two scores and compare the scalars. This forms an objective called **Sliced Fisher Divergence**:

    $$
    D_{SF}(p_{\text{data}}(x) \mid \mid p_{\theta}(x)) =
    \E_{p_{\text{data}}} \E_{p(v)} \left [
        \frac{1}{2} v^T(\nabla_x \log p_{\text{data}}(x) - \nabla_x \log p_{\theta}(x))
    \right ]
    $$

    $$
    =  \E_{p_{\text{data}}} \E_{p(v)} \left [
        \frac{1}{2} \left (v^T \nabla_x \log p_{\text{data}}(x) - v^T \nabla_x \log p_{\theta}(x) \right )
    \right ]
    $$

    Again, we don't have access to the gradients of the data distribution. So the implicit form is:

    $$
    = \E_{p_{\text{data}}} \E_{p(v)} \left [
        \frac{1}{2} \sum_{i = 1}^d \left ( \frac{\partial E_{\theta}(x)}{\partial x_i}  v_i \right )^2 + \sum_{i = 1}^d \sum_{j = 1}^d \frac{\partial^2 E_{\theta}(x)}{\partial x_i \partial x_j} v_i v_j
        \right ] + C
    $$

The second term involves second-derivatives of the $E_{\theta}(x)$ but that can be computed efficiently in $O(d)$. This is because:

$$
\sum_{i = 1}^d \sum_{j = 1}^d \frac{\partial^2 E_{\theta}(x)}{\partial x_i \partial x_j} v_i v_j = \sum_{i = 1}^d \frac{\partial}{\partial x_i} \left ( \sum_{j = 1}^d \frac{\partial E_{\theta}(x)}{\partial x_j} v_j \right) v_i
$$

The term in the parantheses does not depend on $i$ so we only need to compute it once with a $O(d)$ computation and another $O(d)$ computation for the outer sum. For many $p(v)$, the SSM objective can be evaluated in closed form. When $p(v) = \mathcal{N}(0, I)$, we have:

$$
\E_{p_{\text{data}}} \E_{p(v)} \left [
    \frac{1}{2} \sum_{i = 1}^d \left ( \frac{\partial E_{\theta}(x)}{\partial x_i}  v_i \right )^2 = \E_{p_{\text{data}}} \left [
        \frac{1}{2} \sum_{i = 1}^d \left ( \frac{\partial E_{\theta}(x)}{\partial x_i} \right )^2
        \right
    ]
\right ]
$$

Therefore,

$$
D_{SF}(p_{\text{data}}(x) \mid \mid p_{\theta}(x)) = \E_{p_{\text{data}}} \E_{v \sim \mathcal{N}(0, 1)} \left [
    \frac{1}{2} \sum_{i = 1}^d \left ( \frac{\partial E_{\theta}(x)}{\partial x_i} \right )^2 + \sum_{i = 1}^d \sum_{j = 1}^d \frac{\partial^2 E_{\theta}(x)}{\partial x_i \partial x_j} v_i v_j
    \right
]
$$

with a constant $C$ omitted. The left-term is the squared norm of the gradient of the energy w.r.t. $x$.

### ELBO - Jensen



### Citations

[^song2021]: @misc{song2021trainenergybasedmodels,
      title={How to Train Your Energy-Based Models},
      author={Yang Song and Diederik P. Kingma},
      year={2021},
      eprint={2101.03288},
      archivePrefix={arXiv},
      url={https://arxiv.org/abs/2101.03288},
    }

[^hyvarinen2005]: @article{hyvarinen2005estimation,
      title={Estimation of Non-Normalized Statistical Models by Score Matching},
      author={Aapo Hyvärinen},
      journal={Journal of Machine Learning Research},
      volume={6},
      pages={695--709},
      year={2005},
      url={https://jmlr.org/papers/v6/hyvarinen05a.html},
    }

[^vincent2011]: @article{vincent2011connection,
      title={A Connection Between Score Matching and Denoising Autoencoders},
      author={Pascal Vincent},
      journal={Neural Computation},
      volume={23},
      number={7},
      pages={1661--1674},
      year={2011},
      doi={10.1162/NECO_a_00142},
    }

[^song2019]: @inproceedings{song2019generative,
      title={Generative Modeling by Estimating Gradients of the Data Distribution},
      author={Yang Song and Stefano Ermon},
      booktitle={Advances in Neural Information Processing Systems},
      volume={32},
      year={2019},
      eprint={1907.05600},
      archivePrefix={arXiv},
      url={https://arxiv.org/abs/1907.05600},
    }

[^kingma2013]: @misc{kingma2013autoencodingvariationalbayes,
      title={Auto-Encoding Variational Bayes},
      author={Diederik P. Kingma and Max Welling},
      year={2013},
      eprint={1312.6114},
      archivePrefix={arXiv},
      url={https://arxiv.org/abs/1312.6114},
    }

[^weng2018]: @article{weng2018VAE,
      title={From Autoencoder to Beta-VAE},
      author={Lilian Weng},
      journal={lilianweng.github.io},
      year={2018},
      url={https://lilianweng.github.io/posts/2018-08-12-vae/},
    }

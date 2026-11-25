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
    The term $Z(\theta)$ is the partition function integrating over data points $x$. Although it is a normalizing constant, it is distinct from the *marginal likelihood* which integrates over parameters $\theta$. Gradient ascent on $\log Z(\theta)$ is thus doing *maximum likelihood estimation* as opposed to *marginal likelihood optimization*.

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








## VAE

## GAN

## Normalizing Flows


## Appendix

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

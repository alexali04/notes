# Fisher Information Matrix

The **Fisher Information Matrix (FIM)** plays an important role in statistics and optimization. In the post, we will review the FIM and it's role in statistics, it's role in designing pre-conditioners for natural gradient optimization methods and how it interacts with singular models. 

## Overview

We motivate the FIM by considering the following problem. Suppose we have some observed sample $X_1, X_2, \dots \sim_{\text{i.i.d.}} p(x; \theta)$ where $\theta \in \Theta \subseteq \mathbb{R}$. Consider an unbiased estimator $\hat{\theta}$ and suppose we plot the likelihood function over many different possible $\theta$ candidates. 

Consider two scenarios. In one scenario, the likelihood function is sharply peaked while in the other, the likelihood function is flat. Which shape tells you more information about the true parameter?

It seems like the sharply peaked likelihood function intuitively would make it easier to distinguish the true parameter $\theta_0$ from the rest. How can we quantify this and moreover, how good can we get at distinguishing $\theta_0$?

First, let's introduce the **score function**:

$$
s(\theta) = \nabla_{\theta} \log p(\mathbf{x} ; \theta)
$$

This is the derivative of the log-likelihood function. Consider a finite-difference approximation. Suppose in both scenarios, our distribution is peaked around $\theta'$ and we take some step $d\theta$ to the right. In the highly peaked scenario, we would observe a large decrease in likelihood while in the flatter scenario, we would observe a much more mild decrease. 

So the score would be larger in a more sharply peaked scenario. The **Fisher Information** is then the expected variance of the score over the dataset. 

$$
\mathcal{I}(\theta) = \mathbb{E}_{X}[s(\theta)^2] = \int s(\theta)^2 p(x \mid \theta) dx
$$

We can measure the Fisher information of each parameter. Imagine many log-likelihood curves laid atop one another. At a particular parameter, we can look at the variance of the log-likelihood gradients over all of these curves. The FIM is mathematically, a weighted sum-of-squares of gradients so a larger FIM would mean that a particular parameter is distinguishable from its neighbors. 

In the multivariate scenario, the log-likelihood gradient is no longer a singular number but rather a gradient. To square the gradient, we can take it's outer-product. This gives us the **Fisher Information Matrix**.

$$
\mathcal{I}(\mathbf{\theta}) = \mathbb{E}[s(\mathbf{\theta}) s(\theta)^T]
$$

This plays a role in the Cramer-Rao Lower Bound which lower-bounds the asymptotic variance of any unbiased estimator by the inverted Fisher information matrix (matrix inequality). That particular bound is not the focus of this post though. 

## Hessian Matrix

You might suspect that the **FIM** could be intuitively related to the Hessian at this point. The Hessian is a matrix of $2$nd derivatives while the FIM is the outer-product of gradients. Additionally, the utility of the FIM is essentially to analyze the curvature of the log-likelihood at a specific point which is precisely what the Hessian does! It turns, out they are related. 

Consider the Hessian of the log-likelihood. We have:

$$
[H(\theta)]_{ij} = \frac{\partial}{\partial \theta_i \theta_j} \mathbb{E}_X[\log p(X \mid \theta)]
$$

The FIM (written as $F$) here is:

$$
[F(\theta)]_{ij} = \mathbb{E}_{X} \left [ \frac{\partial}{\partial \theta_i} \log p(X \mid \theta) \cdot \frac{\partial}{\partial \theta_j} \log p(X \mid \theta) \right ]
$$

$$
= \mathbb{E}_{X} [\nabla_{\theta_i} \ \log p(x \mid \theta) \cdot \nabla_{\theta_j} \ \log p(x \mid \theta)]
$$

**We will show that**:

$$
F(\theta) = - \mathbb{E}_{X}[H(\theta)]
$$


Let's establish some basic tools. 

$$
\int_{X} p(x \mid \theta) dx = 1
$$

Any normalizable probability distribution must integrate to $1$. It follows that

$$
\frac{\partial}{\partial \theta_i} \int_{X} p(x \mid \theta) dx = \int_{X} \frac{\partial}{\partial \theta_i} p(x \mid \theta) dx = 0
$$ 

$$
\int_{X} \frac{\partial}{\partial \theta_i \partial \theta_j} p(x \mid \theta) dx = 0
$$

We can also compute the $2$nd derivative of the log-likelihood. 

$$
\frac{\partial}{\partial \theta_i \theta_j} \log p(x \mid \theta) = \frac{\partial}{\partial \theta_i} \cdot \frac{\frac{\partial}{\partial \theta_j} p(x \mid \theta)}{p(x \mid \theta)}
$$

$$
= \frac{[\frac{\partial}{\partial \theta_i} \frac{\partial}{\partial \theta_j} p(x \mid \theta)] p(x \mid \theta)  - \frac{\partial}{\partial \theta_j} p(x \mid \theta) \cdot \frac{\partial}{\partial \theta_i} p(x \mid \theta)}{p(x \mid \theta)^2}
$$

$$
= \frac{\frac{\partial}{\partial \theta_i \theta_j}p(x \mid \theta)}{p(x \mid \theta)} -  \frac{\frac{\partial}{\partial \theta_j} p(x \mid \theta)}{p(x \mid \theta)} \cdot \frac{\frac{\partial}{\partial \theta_i} p(x \mid \theta)}{p(x \mid \theta)}
$$

Now that we have our basic tools, let's compute the expected Hessian. By the linearity of expectation,

$$
\mathbb{E}_{X}[H(\theta)]_{ij} = \mathbb{E}_{X} [\frac{\partial}{\partial \theta_i \theta_j} \log p(x \mid \theta)] = \mathbb{E}_{X} \left [ \frac{\frac{\partial}{\partial \theta_i \theta_j}p(x \mid \theta)}{p(x \mid \theta)} -  \frac{\frac{\partial}{\partial \theta_j} p(x \mid \theta)}{p(x \mid \theta)} \cdot \frac{\frac{\partial}{\partial \theta_i} p(x \mid \theta)}{p(x \mid \theta)} \right ]
$$

$$
= \mathbb{E}_{X} \left [ \frac{\frac{\partial}{\partial \theta_i \theta_j}p(x \mid \theta)}{p(x \mid \theta)} \right ] - \mathbb{E}_{X} \left [\frac{\frac{\partial}{\partial \theta_j} p(x \mid \theta)}{p(x \mid \theta)} \cdot \frac{\frac{\partial}{\partial \theta_i} p(x \mid \theta)}{p(x \mid \theta)} \right ]
$$

The first term evaluates to $0$ as established beforehand.

$$
\mathbb{E}_{X} \left [ \frac{\frac{\partial}{\partial \theta_i \theta_j}p(x \mid \theta)}{p(x \mid \theta)} \right ] = \int \frac{\frac{\partial}{\partial \theta_i \theta_j}p(x \mid \theta)}{p(x \mid \theta)} p(x \mid \theta) dx
$$

$$
= \int \frac{\partial}{\partial \theta_i \theta_j}p(x \mid \theta) dx = 0
$$

Thus, we have:

$$
\mathbb{E}_{X}[H(\theta)]_{ij} = - \mathbb{E}_{X} \left [\frac{\frac{\partial}{\partial \theta_j} p(x \mid \theta)}{p(x \mid \theta)} \cdot \frac{\frac{\partial}{\partial \theta_i} p(x \mid \theta)}{p(x \mid \theta)} \right ] = - \mathbb{E}_{X} [\nabla_{\theta_i} \ \log p(x \mid \theta) \cdot \nabla_{\theta_j} \ \log p(x \mid \theta)]
$$

$$
= - F(\theta)
$$

Hence,

$$
F(\theta) = - \mathbb{E}_X[H(\theta)]
$$

This equality only works because we're integrating over $X$ using the density $p(x \mid \theta)$. In other words, the FIM coincides with the negative expected Hessian when both expectations are being taken over $p(x \mid \theta)$. Typically, the expected Hessian of the loss is taken over *data* while we compute the FIM of our *model* which are normally different. 

We should also draw a subtle distinction. The FIM measures sensitivity of the model's output distribution, $p(y \mid x_n, \theta)$ w.r.t. the model parameters. The *empirical Fisher* instead uses labels $y_n$ from the dataset. There has been research showing that the empirical Fisher does not make for a particularly good pre-conditioner. See [1](https://www.inference.vc/on-empirical-fisher-information/), [2](https://arxiv.org/abs/1905.12558) for more information.

https://www.inference.vc/on-empirical-fisher-information/

https://arxiv.org/abs/1905.12558






# Deep Learning Alchemy

Notes on Deep Learning Alchemy (CS 312). Fair amount of stuff is skipped.

A fair amount of this course is about experimentation. Sadly, my GPUs are currently busy. So I will figure somewhere else to put the assignments. For now (admittedly against the spirit of the course), we will just take notes on the content.

## LLM 101

### Setting

LLMs model joint distribution over sequences of tokens auto-regressively using the chain law of probability.

$$
p_{\theta}(x_{2:T} \mid x_1) = \prod_{t = 1}^{T - 1} p_{\theta}(x_{t + 1} \mid x_{\leq t})
$$

$$
= p_{\theta}(x_2 \mid x_1) p_{\theta}(x_3 \mid x_2, x_1) \dots p_{\theta}(x_{T} \mid x_1 \dots x_{T - 1})
$$

Note that during training, transformers recieve the true prefix - this is called **teacher forcing**. Like many other ML settings, we train using maximum likelihood estimation (MLE) done by minimizing negative log-likelihood of cross-entropy. We also **normalize per sequence length**.

$$
L(\theta) = - \frac{1}{T - 1} \E_{x \sim p_{\text{data}}} \left [ \log p_{\theta}(x) \right ] = - \frac{1}{T - 1} \E_{x \sim p_{\text{data}}} \left [ \sum_{i = 1}^{T - 1} \log p_{\theta}(x_{t + 1} \mid x_{\leq t}) \right ]
$$

In other words, the model $\theta$ is punished for assigning low probabilities to observed tokens.

Naturally, this expectation is intractable so we need to average over available examples. A more intuitive measure of this negative likelihood is called *perplexity*.

!!! quote "Important: Perplexity"
    Perplexity is defined as $\exp(L)$ and is equivalent to the uncertainty you'd experience when rolling a die. A perplexity of $20$ means you're choosing a token from a uniform distribution over $20$ choices (rolling a $20$ sided die). See [this blog post](https://mbernste.github.io/posts/perplexity/) for more.

Evaluating LLMs is tricky. There have been times where the sample qualities achieve lower perplexity (as evaluated by a larger model which we take to provide the ground-truth) but also lower sample diversity. For example, a model which simply repeats many common tokens (BOS, EOS, "the") may achieve good perplexity according to a weak evaluator like GPT2.

### Optimization

To optimize this loss function with respect to the parameters $\theta$, we use gradient descent (where the gradient is computed over a batch of sequences). There are many resources about backpropagation available but the idea is to simply use the chain rule from calculus.

An *epoch* is a single pass over the training dataset. In training my language diffusion models, we used 33 epochs over LM1B, a dataset of about 1 billion tokens.

A crucial hyperparameter in the optimizer is the *learning rate*. Essentially, gradient descent computes:

$$
\theta^{(i + 1)} = \theta_i - \eta \nabla L_{\theta_i}
$$

where $\eta$ is the learning-rate - essentially, how large of a step do we take in the gradient direction. If $\eta$ is too small, we will never reach a good loss value. If $\eta$ is too big, we may "overshoot" the minima we're aiming for.

*Warmup* starts with small updates and increases scale early in training. *Decay* decreases it later.

![](../images/warmup_decay.png)

More advanced optimization methods (SGD with Momentum, AdamW) seek to stabilize gradient-based training (i.e. keeping running direction from past gradients or normalizing moment-estimates for the gradients).

*Weight decay* shrinks selected parameters towards $0$. In AdamW, it is *decoupled* from gradient's moving averages.

*Gradient Clipping* tries to avoid taking huge steps even when a single batch can yield huge gradients.

### Diagnostics

Gradient norms, parameter / activation magnitudes (RMS). The time when the metric is measured also matters - pre-clipping gradients, post-update parameters, etc.

### Architecture

QK-normalization applies RMSNorm to each attention head's query / key vector before computing the dot-product.

SwiGLU computes:

$$
\text{SwiGLU}(x) = (Wx+b)*\text{Swish}(Vx+c)
$$

$$
\text{Swish}(Vx+c) = (Vx + c) \sigma(\beta (Vx + c))
$$

where $\sigma(z) = \frac{1}{1 + e^{-z}}$.

## Basics

Deep learning looks more like biology than computer science - tight experimental looops, learning from and designing experiments matter a lot.

Good skills include optimization, being efficient, and knowing what to measure / debug.

Hyperparameters are like nuisance parameters or things we pick by hand - when an experiment fails, all we can infer is that *at least one* setting is bad.

Failures to tune hyperparameters:
- DP-SGD does work with appropriate 

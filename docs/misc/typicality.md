# Understanding Typicality

## Before Blog

I have previously come across typicality in a couple of contexts

- In using MCMC estimators in high dimensions, an integral tends to concentrate its $\text{volume} * \text{density}$ on a thin surface called the *typical set* where the Markov Chain should ideally spend most of its time. High dimensional Gaussians are frequently analogized to soap bubbles (I think of them like pound cakes). The density is concentrated around the distribution's mode but there is also very little *volume* around the mode. The typical set is thus like a film around the mode where both the probability density and the volume are non-negligible (hence where most of the integral is).

- The AEP (Asymptotic Equipartition Property) in information theory states that there is a set of sequences called the *typical set* where the probability of this set as the length of the sequence grows approaches $1$ *and* the distribution over this set is roughly uniform. Additionally, I recall that the single most likely sequence is frequently *not* in this set.

For the first point, much of my intuition comes from this [paper](https://arxiv.org/abs/1701.02434) and talk by Michael Betancourt.

## Blog

Maximum likelihood training is simple and intuitive. However, for generative modeling, higher likelihood frequently does not correlate to visual fidelity and can produce very unintuitive results. This post excludes overfitting as a possible explainer as that is not unique to likelihood based models.

### Coins

Consider the binomial distribution $B(n, p)$ where $n = 16, p = \frac{3}{4}$ modeling a sequence of unfair coin flips. On average, we would expect to see about $12$ heads and $4$ tails with some room for error. Here, we are treating sequences as unordered sets.

Let $Y$ be the sequence $(x_1, \dots, x_{16})$. What is $\text{argmax}_Y \ P(Y)$, the *single* most likely sequence?

The single most likely sequence is all heads. The probability of this sequence is $\frac{3}{4}^{16} = 0.01$. While this sequence is the single most likely sequence, we would be shocked if we actually ended up counting $16$ heads as that would mean not a single coin landed on tails.

On the contrary, let $X$ be the number of heads observed. Then, the most likely number of heads to observe is $12$. The specific probability of observing $12$ heads is $C(16, 4) * (\frac{3}{4})^{12} (\frac{1}{4})^4$. While each individual sequence containing $12$ heads is not as likely as the sequence with $16$ heads, there are $C(16, 4)$ ways to *get* $12$ heads while there is only *one* way to get $16$ heads.

### Gaussians

![Gaussian Densities Resemble Pound Cakes](../images/lemon_pound_cake.png)
*Gaussian Densities can be analogized to soap bubbles... or pound cakes!*

As was stated earlier, high-dimensional Gaussians concentrate their probability density around the mode. However, computing an integral involves multiplying this density against $dx$, a little piece of volume. In high-dimensional spaces, there is more volume *further away* from any given point. There is simply more space for the distribution to exist over further away from the mode (at the peak of the pound cake / surface of the soap bubble). This is the continuous version of the coin example - $16$ heads is the single most likely sequence but there are more *ways* to get $12$ heads. Similarly, if you had a hundred-dimensional Gaussian centered around $\vec{0}$, you would still be extremely surprised to observe $\vec{0}$ as a sample.

This is stated formally in many textbooks as the Gaussian annulus theorem.

### Typicality

Entropy can be written as

$$
H(X) = \mathbb{E}_{X \sim p} \left [ \log \frac{1}{p(X)} \right ]
$$

Suppose $X_1, \dots, X_n$ are i.i.d. $\sim p$. If $H(X) < \infty$, then by LLN

$$
\frac{1}{n} \log \frac{1}{p(X_1, \dots, X_n)} = \frac{1}{n} \sum_{i = 1}^n \log \frac{1}{p(X_i)} \to_{n \to \infty} \mathbb{E}[\log \frac{1}{p(X)}] = H(X)
$$

Then, for $\epsilon > 0$, define the *typical set*

$$
\mathcal{T}_{n}^{\epsilon} = \{x^n \in \mathcal{X}^n: p(x^n) \in [2^{-n(H(X) + \epsilon)}, 2^{-n(H(X) - \epsilon)}] \}
$$

In other words, each sequence in the typical set carries roughly as much information as expected (within $\epsilon$ of the distribution's entropy). To see this, simply reverse:

$$
\frac{1}{n} \log \frac{1}{p(\mathbf{x})} \approx H(X)
$$

$$
\frac{1}{p(\mathbf{x})} \approx 2^{n H(X)}
$$

$$
p(\mathbf{x}) \approx 2^{- n H(X)}
$$

The negative log likelihood of each of these sequences is close to the distribution's entropy. As the dimensionality increases, the probability that each random sample drawn from the distribution is part of a given typical set $\mathcal{T}_{\epsilon}$ approaches $1$. Random samples will nearly always be 'typical' and the typical set covers most of the distribution's support.

Additionally, like mentioned earlier (and illustrated with the coin example), the mode frequently is not part of the typical set. Individual samples with exceptional likelihoods are in fact atypical and we shouldn't expect to observe them during sampling.

### Paradoxes

#### Language

In autoregressive models + beam search, we sometimes may want to find the single most likely sentence ('MAP decoding') or something akin to that. However, those familiar with language models know that in setting temperature to $0$, we get degenerate or repetitive sentences. This repetitivity is atypical but has high likelihoods precisely because it is more predictable.

#### OOD detection

OOD detection asks if an input plausibly could have been drawn from some distribution. Typically, we assume that OOD inputs have low-likelihoods and in-distribution inputs have high-likelihoods (we are likely to sample them). However, the mode of a distribution has a very high likelihood but as we established, we are extremely *unlikely* to sample the mode as it is not part of the typical set.

## Conclusion

It may be preferable to learn fidelity using 'intuitive' likelihood or to learn some kind of perceptual metric.

After reading this blog, I feel that I have a much better handle on typicality and its relationship with likelihoods. I believe the first intuition which is that in high-dimensional spaces, volume grows the further we move from a given spot, explains this phenomenon of Gaussian "soap bubbles". The trap of examining atypically likely samples (like the mode) seems to be the clearest connection between typicality and machine learning.









### Citations
- @misc{dieleman2020typicality,
  author = {Dieleman, Sander},
  title = {Musings on typicality},
  url = {https://benanne.github.io/2020/09/01/typicality.html},
  year = {2020}
}
- @misc{betancourt2018conceptualintroductionhamiltonianmonte,
      title={A Conceptual Introduction to Hamiltonian Monte Carlo},
      author={Michael Betancourt},
      year={2018},
      eprint={1701.02434},
      archivePrefix={arXiv},
      primaryClass={stat.ME},
      url={https://arxiv.org/abs/1701.02434},
}
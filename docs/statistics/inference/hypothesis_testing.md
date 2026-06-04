# Hypothesis Testing

## Introduction

A *hypothesis* is a statement about a population parameter.

!!! info "Definition: Complementary Hypotheses"
    The two complementary hypotheses in hypothesis testing are called the *null hypothesis* and the *alternative hypothesis* written as $H_0$, $H_1$.

If $\theta$ is a population parameter, then $H_0 = \{\theta \in \Theta_0\}$ and $H_1 = \{\theta \in \Theta_0^C\}$.

!!! example "Example: Drugs"
    If $\theta$ denotes the average change in a patient's blood pressure after taking a drug, an experimenter would likely by interested in testing $H_0: \theta = 0$ vs $H_1: \theta \neq 0$.

    The null states that on average, the drug doesn't affect blood pressure whereas the alternative states that there is some effect. The common situation is that $H_0$ states that the treatment has no effect, hence why it is called the "null" hypothesis.

!!! info "Definition: Hypothesis Test"
    A hypothesis test is a rule that specifies for which sample values the decision is made to accept $H_0$ as true vs where $H_0$ is rejected and $H_1$ is accepted as true.

We can sidestep the philosophical discussion of accepting $H_1$ as opposed to "rejecting the null".

Typically, a *test statistic* $W(X_1, \dots, X_n) = W(\mathbf{X})$ is a function of the sample. A test might specify that $H_0$ is to be rejected if $W(\mathbf{X}) = \bar{X}$, the sample mean, is greater than $10$. Here, test statistic is the sample mean and the rejection region is $\{(x_1, \dots, x_n): \bar{x} \geq 19\}$.

## Methods of Finding Tests

### Likelihood Ratio

Recall that if $X_1, \dots, X_n$ is a random sample from a population with distribution $f(x \mid \theta)$, the likelihood function is:

$$
L(\theta \mid x_1, \dots, x_n) = L(\theta, \mathbf{x}) = f(\mathbf{x} \mid \theta) = \prod_{i = 1}^n f(x_i \mid \theta)
$$

!!! info "Definition: Likelihood Ratio Test Statistic"
    Let $\Theta$ denote the parameter space. Then, the *likelihood ratio test statistic* for testing $H_0: \theta \in \Theta_0$ versus $H_1: \theta \in \Theta_0^C$ is

    $$
    \lambda(\mathbf{x}) = \frac{\sup_{\Theta_0} L(\theta \mid \mathbf{x})}{\sup_{\Theta} L(\theta \mid \mathbf{x})}
    $$

    A *likelihood ratio test* is any test with a rejection region of the form $\{\mathbf{x} : \lambda(\mathbf{x}) \leq c} where $0 \leq c \leq 1$.

In the discrete case, the numerator is the maximum probability of the observed sample under the null hypothesis while the denominator is the maximum probability of the observed sample over all possible parameters.

This ratio is small when there are points in the alternative hypothesis space where the observed sample is much more likely. When this ratio is close to $1$, the null hypothesis space produces as good (or nearly as good) likelihoods for the observed sample.

This is essentially computing the ratio of maximum likelihoods.

### Bayesian Tests

We use the posterior distribution $\pi(\theta \mid \mathbf{x})$ to calculate the probabilities that $H_0, H_1$ are true. Recall $\pi(\theta \mid \mathbf{x})$ is a probability distribution over a random variable. The posterior probabilities, $P(\theta \in \Theta_0 \mid \mathbf{x}), P(\theta \in \Theta_0^C \mid \mathbf{x})$ can be computed.

A Bayesian hypothesis tester can choose to accept $H_0$ as true if $P(\theta \in \Theta_0 \mid \mathbf{X}) \geq P(\theta \in \Theta_0^C \mid \mathbf{X})$. If the tester wishes to guard against false rejections, the tester can reject $H_0$ only if $P(\theta \in \Theta_0^C \mid \mathbf{X})$ is greater than some large number. 







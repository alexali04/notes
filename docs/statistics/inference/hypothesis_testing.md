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









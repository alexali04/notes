# Introduction

What kind of models should we prefer? Do we prefer simplistic models as
is in line with Occam's Razor? Do we prefer exceedingly complex models?

We argue that we should prefer highly flexible models with inductive
biases which determine how we distribute our a priori support.

Note: Model and model class are used interchangeably below.

Probability Rules:

1.  Sum Rule:

    $$\begin{equation}
        p(A) = \int_B p(A \mid B) \ p(B) \ dB
    \end{equation}$$

    Again,

    $$\begin{equation}
        p(A, B) = \int_C p(A, B \mid C) \ p(C) \ dC
    \end{equation}$$

2.  Product Rule:

    $$\begin{equation}
        p(A, B) = p(A \mid B) p(B)
    \end{equation}$$

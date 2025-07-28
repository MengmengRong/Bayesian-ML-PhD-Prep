# Week 2: Bayesian Thinking

This document summarizes key concepts from Week 2 of the Bayesian Statistics course on Coursera (UCSC). It covers the basic building blocks of Bayesian inference.

---

## 🔑 Core Concepts

- Prior distribution
- Likelihood function
- Bayes’ Theorem in action
- Posterior distribution
- Beta and Bernoulli conjugate priors

---

## ✍️ Notes

> Posterior ∝ Likelihood × Prior  
> \[
P(\theta \mid x) \propto P(x \mid \theta) \cdot P(\theta)
\]

- Rules of Probability

If A and B are two events, the probability that A or B happens (this is an inclusive or, meaning that either A, or B, or both happen) is the probability of the union of the events:

$$ P(A \cup B) = P(A) + P(B) - P(A \cap B) $$

where \cup represents union (\or") and \cap represents intersection (\and"). If a set of events A_i for i = 1...,m are mutually exclusive (only one can happen), then

$$ P\left(\bigcup_{i=1}^{m} A_i\right) = \sum_{i=1}^{m} P(A_i) $$ 

- Probabilities can be re-expressed in terms of odds.
- The expected value of a random variable X is a weighted average of values X can take, with weights given by the probabilities of those values.

- Basic Concepts & Notation

  Random Variable (随机变量)

  X, Y, Z (大写字母): Denotes a random variable itself.

  x, y, z (小写字母): Denotes a specific realization or value of a random variable.

  Distributed As (服从...分布)

  X ~ Distribution(...): Indicates that random variable X follows a specific distribution.

  Example: X ~ Binomial(n, p) (X follows a Binomial distribution with parameters n and p).

- Probability Calculation Formulas
  
  Probability of Union of Events (并事件的概率)

  For any two events A and B (对于任意两个事件 A 和 B):
  P(A ∪ B) = P(A) + P(B) - P(A ∩ B)

  For a series of mutually exclusive events A₁, A₂, ..., Aₘ (对于一系列互斥事件 A₁, A₂, ..., Aₘ):
  P(⋃ᵢ<binary data, 1 bytes><binary data, 1 bytes>₁ᵐ Aᵢ) = ∑ᵢ<binary data, 1 bytes><binary data, 1 bytes>₁ᵐ P(Aᵢ)

- Definition of Conditional Probability (条件概率的定义)

  Definition (定义):
  P(B|A) = P(A ∩ B) / P(A) (for P(A) > 0)

  Multiplication Rule (乘法法则 - derived from definition):
  P(A ∩ B) = P(B|A)P(A)
  P(A ∩ B) = P(A|B)P(B)

- Independence of Events (事件独立性)

  Definition 1 (定义 1):
  P(A|B) = P(A)

  Definition 2 (Equivalent to Definition 1 - 定义 2，等价于定义 1):
  P(A ∩ B) = P(A)P(B)

- Properties of Expectation and Variance

  Expected Value (期望)
  Linearity (线性性质): For any constants a, b and random variables X, Y:
  E(aX + bY) = aE(X) + bE(Y)

  Variance (方差)

  Definition/Calculation Formula (定义/计算公式):
  Var(X) = E[(X - E[X])²] = E[X²] - (E[X])²

  Variance of Sum (和的方差):

  If X and Y are Independent (如果 X 和 Y 独立):
  Var(X + Y) = Var(X) + Var(Y)

  If X and Y are Not Independent (如果 X 和 Y 不独立):
  Var(X + Y) = Var(X) + Var(Y) + 2Cov(X,Y)

  Covariance (协方差)

  Definition (定义):
  Cov(X,Y) = E[(X - E[X])(Y - E[Y])]

  Calculation Formula (计算公式 - derived from definition):
  Cov(X,Y) = E[XY] - E[X]E[Y]

---

## 💡 Reflections

- How do different priors affect the posterior?
- What happens with more data?
- What applications might benefit from Bayesian thinking?

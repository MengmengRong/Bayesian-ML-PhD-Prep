# Week 2: Bayesian Thinking – Priors, Likelihood, Posterior

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
  
---

## 💡 Reflections

- How do different priors affect the posterior?
- What happens with more data?
- What applications might benefit from Bayesian thinking?

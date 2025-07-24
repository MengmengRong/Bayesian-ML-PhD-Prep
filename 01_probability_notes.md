# Week 1: Probability Basics

This document summarizes the key concepts and takeaways from the first week of probability review (based on Khan Academy and/or MIT OCW materials).

📘 Based on Khan Academy "Statistics and Probability" – Chapters 1–3  
🎯 Goal: Build foundational understanding of probability for Bayesian modeling

---

## 🔢 Topics Covered

- What is probability?
- Random events and outcomes
- Sample space, events, and probability rules
- Conditional probability
- Bayes' Theorem (brief intro)
- Expected value and variance

---

## 📖 Key Concepts

### ✅ What is Probability?

- Probability measures the likelihood of an event
- Values range from 0 (impossible) to 1 (certain)
- Example:  
  - P(rolling a 6 on a fair die) = 1/6

---

### ✅ Conditional Probability

- `P(A | B)` = Probability of A given that B has occurred
- Formula:  
  \[
  P(A|B) = \frac{P(A \cap B)}{P(B)}
  \]
- Example:  
  - P(drawing a red card | known it's a heart) = 1

---

### ✅ Independent Events

- Events A and B are independent if:  
  \[
  P(A \cap B) = P(A) \cdot P(B)
  \]
- Example:  
  - Tossing two coins

> Example: What is the probability of rolling an even number on a fair 6-sided die?

\[
P(\text{even}) = \frac{3}{6} = 0.5
\]

> Conditional Probability:

\[
P(A|B) = \frac{P(A \cap B)}{P(B)}
\]

---

### ✅ Expected Value (E[X])

- Weighted average of outcomes
- Example: Tossing a fair die:  
  \[
  E[X] = \frac{1+2+3+4+5+6}{6} = 3.5
  \]

---

### ✅ Variance and Standard Deviation

- Variance:  
  \[
  \text{Var}(X) = E[(X - \mu)^2]
  \]
- Standard deviation = √Variance

---

## 🧪 Practice Examples

```python
# Simulate coin tosses and calculate empirical probabilities
import numpy as np

n = 10000
flips = np.random.choice(['H', 'T'], size=n)
heads_prob = np.mean(flips == 'H')
print(f"Empirical P(H) ≈ {heads_prob}")



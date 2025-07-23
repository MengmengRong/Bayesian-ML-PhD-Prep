import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import beta

# Prior: Beta(2,2)
a_prior, b_prior = 2, 2

# Simulate coin flips: 10 heads, 5 tails
heads = 10
tails = 5

# Posterior: Beta(2+10, 2+5) = Beta(12,7)
a_post = a_prior + heads
b_post = b_prior + tails

x = np.linspace(0, 1, 100)
y = beta.pdf(x, a_post, b_post)

plt.plot(x, y)
plt.title(f"Posterior Beta({a_post},{b_post})")
plt.xlabel("Theta")
plt.ylabel("Density")
plt.grid()
plt.show()

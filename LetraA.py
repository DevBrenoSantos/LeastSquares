import numpy as np
import matplotlib.pyplot as plt

plt.style.use('seaborn-poster')

# Given values
X = np.array([-3, -1.5, 0.3, 1.7, 2.2])
Y = np.array([1, 2, 2.4, 2.9, 3.5])

# Assemble matrix A
A = np.vstack([X, np.ones(len(X))]).T

# Direct least square regression
alpha = np.dot((np.dot(np.linalg.inv(np.dot(A.T, A)), A.T)), Y[:, np.newaxis])
print(alpha)
0

print(f"Fitted Line: y = {alpha[0][0]} * x + {alpha[1][0]}")
# Plot the results
plt.figure(figsize=(10, 8))
plt.plot(X, Y, 'b.')
plt.plot(X, alpha[0] * X + alpha[1], 'r')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()
import numpy as np
import matplotlib.pyplot as plt
from numerical_derivative import numerical_derivative

def f(x):
    return x**2

x0 = 3
grad = numerical_derivative(f, x0)

x = np.linspace(0, 6, 100)
y = f(x)
tangent = grad * (x - x0) + f(x0)

plt.plot(x, y, label='f(x) = x^2')
plt.plot(x, tangent, '--', label='Tangent at x=3')
plt.scatter([x0], [f(x0)], color='red')
plt.title("Numerical Derivative Visualization")
plt.legend()
plt.grid()
plt.show()

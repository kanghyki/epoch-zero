import numpy as np
import matplotlib.pyplot as plt

def f_min(x, y):
    return x**2 + y**2  # local/global minimum at (0, 0)

def f_saddle(x, y):
    return x**2 - y**2  # saddle point at (0, 0)

x = np.linspace(-2, 2, 100)
y = np.linspace(-2, 2, 100)
X, Y = np.meshgrid(x, y)
Z_min = f_min(X, Y)
Z_saddle = f_saddle(X, Y)

fig = plt.figure(figsize=(14, 6))

# Local Minimum
ax1 = fig.add_subplot(121, projection='3d')
ax1.plot_surface(X, Y, Z_min, cmap='viridis', alpha=0.8)
ax1.set_title('Local Minimum: $f(x, y) = x^2 + y^2$')
ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.set_zlabel('f(x, y)')

# Saddle Point
ax2 = fig.add_subplot(122, projection='3d')
ax2.plot_surface(X, Y, Z_saddle, cmap='plasma', alpha=0.8)
ax2.set_title('Saddle Point: $f(x, y) = x^2 - y^2$')
ax2.set_xlabel('x')
ax2.set_ylabel('y')
ax2.set_zlabel('f(x, y)')

plt.tight_layout()
plt.show()

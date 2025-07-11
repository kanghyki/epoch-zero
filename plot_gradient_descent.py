import matplotlib.pyplot as plt
from gradient_descent import *

def plot_path_3d(f, path, title='3D Gradient Descent Path'):
    x_vals, y_vals = path[:, 0], path[:, 1]
    z_vals = np.array([f(np.array([x, y])) for x, y in zip(x_vals, y_vals)])

    fig = plt.figure(figsize=(10, 7))
    ax = fig.add_subplot(111, projection='3d')

    x = np.linspace(-5, 5, 100)
    y = np.linspace(-5, 5, 100)
    X, Y = np.meshgrid(x, y)
    Z = np.array([[f(np.array([xi, yi])) for xi, yi in zip(x_row, y_row)] for x_row, y_row in zip(X, Y)])

    ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.6)
    ax.plot(x_vals, y_vals, z_vals, 'ro-', label='GD Path')
    ax.scatter(x_vals[0], y_vals[0], z_vals[0], color='green', s=100, label='Start')
    ax.scatter(x_vals[-1], y_vals[-1], z_vals[-1], color='blue', s=100, label='End')

    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('f(x, y)')
    ax.set_title(title)
    ax.legend()
    plt.show()

def plot_path_2d(f, path, title='Gradient Descent Path'):
    x_vals = np.linspace(-5, 5, 100)
    y_vals = np.linspace(-5, 5, 100)
    X, Y = np.meshgrid(x_vals, y_vals)
    Z = f(np.array([X, Y]))

    px, py = path[:, 0], path[:, 1]

    plt.figure(figsize=(8, 6))
    plt.contour(X, Y, Z, levels=30, cmap='gray')
    plt.plot(px, py, 'ro-')
    plt.quiver(px[:-1], py[:-1], px[1:] - px[:-1], py[1:] - py[:-1],
               angles='xy', scale_units='xy', scale=1, color='blue', width=0.004)
    plt.title(title)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.axis('equal')
    plt.grid(True)
    plt.show()


def f1(x):  # 기본 함수
    return x[0]**2 + x[1]**2

def f2(x):  # 경사 비대칭 함수
    return x[0]**2 + 2 * x[1]**2

def f3(x):  # 비선형 함수
    return np.sin(x[0]) + np.cos(x[1])

start = np.array([3.0, 4.0])
path = gradient_descent(f1, start)
plot_path_3d(f1, path)
plot_path_2d(f1, path)

path = gradient_descent(f2, start)
plot_path_3d(f2, path)
plot_path_2d(f2, path)

start = np.array([1.5, 1.5])
path = gradient_descent(f3, start, lr = 1, steps = 10)
plot_path_3d(f3, path)
plot_path_2d(f3, path)

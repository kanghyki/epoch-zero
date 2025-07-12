from numerical_gradient import *

def gradient_descent(f, init_x, lr=0.1, steps=100):
    x = init_x.copy()
    history = [x.copy()] # for visualization

    for _ in range(steps):
        grad = numerical_gradient(f, x)
        x -= lr * grad
        history.append(x.copy())

    return np.array(history)

import numpy as np

def mse(y_true, y_pred):
    return np.mean((y_true - y_pred) ** 2)

def mse_grad(y_true, y_pred):
    return 2 * (y_pred - y_true) / y_true.shape[0]

def binary_cross_entropy(y_true, y_pred, eps=1e-10):
    y_pred = np.clip(y_pred, eps, 1 - eps)
    return -np.mean(y_true * np.log(y_pred) + (1 - y_true) * np.log(1 - y_pred))

def binary_cross_entropy_grad(y_true, y_pred, eps=1e-10):
    y_pred = np.clip(y_pred, eps, 1 - eps)
    return (y_pred - y_true) / (y_pred * (1 - y_pred) * y_true.shape[0])

def huber(y_true, y_pred, delta=1.0):
    error = y_pred - y_true
    is_small = np.abs(error) <= delta
    squared = 0.5 * (error ** 2)
    linear = delta * (np.abs(error) - 0.5 * delta)
    return np.mean(np.where(is_small, squared, linear))

def huber_grad(y_true, y_pred, delta=1.0):
    error = y_pred - y_true
    is_small = np.abs(error) <= delta
    grad = np.where(is_small, error, delta * np.sign(error))
    return grad / y_true.shape[0]

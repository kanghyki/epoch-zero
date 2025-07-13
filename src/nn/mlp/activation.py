import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))
def sigmoid_grad(x):
    s = sigmoid(x)
    return s * (1 - s)

def tanh(x):
    return np.tanh(x)
def tanh_grad(x):
    return 1 - np.tanh(x) ** 2

def relu(x):
    return np.maximum(0, x)
def relu_grad(x):
    return (x > 0).astype(float)

def leaky_relu(x, alpha=0.01):
    return np.where(x > 0, x, alpha * x)
def leaky_relu_grad(x, alpha=0.01):
    return np.where(x > 0, 1, alpha)

def elu(x, alpha=1.0):
    return np.where(x >= 0, x, alpha * (np.exp(x) - 1))
def elu_grad(x, alpha=1.0):
    return np.where(x >= 0, 1, alpha * np.exp(x))

def gelu(x):
    return 0.5 * x * (1 + np.tanh(np.sqrt(2/np.pi)*(x + 0.044715 * x**3)))
def gelu_grad(x):  # 근사치
    return 0.5 * (1 + np.tanh(np.sqrt(2/np.pi)*(x + 0.044715 * x**3))) + \
           (0.5 * x * (1 - np.tanh(np.sqrt(2/np.pi)*(x + 0.044715 * x**3))**2)
            * (np.sqrt(2/np.pi)*(1 + 3*0.044715*x**2)))

import numpy as np

class MLP:
    def __init__(self, layers, activation, activation_grad):
        self.layers = layers
        self.activation = activation
        self.activation_grad = activation_grad
        self.weights = []
        self.biases = []

        for i in range(len(layers) - 1):
            w = np.random.randn(layers[i], layers[i + 1])
            b = np.zeros((1, layers[i + 1]))
            self.weights.append(w)
            self.biases.append(b)

    def forward(self, X):
        self.zs = []
        self.activations = [X]
        a = X
        for i in range(len(self.weights) - 1):  # 은닉층
            z = a @ self.weights[i] + self.biases[i]
            a = self.activation(z)
            self.zs.append(z)
            self.activations.append(a)
        # 출력층 (sigmoid 고정)
        z = a @ self.weights[-1] + self.biases[-1]
        a = 1 / (1 + np.exp(-z))  # sigmoid
        self.zs.append(z)
        self.activations.append(a)
        return a

    def backward(self, y_true):
        m = y_true.shape[0]
        self.dw = [None] * len(self.weights)
        self.db = [None] * len(self.biases)

        # 출력층
        dz = (self.activations[-1] - y_true) * self.activations[-1] * (1 - self.activations[-1])
        for i in reversed(range(len(self.weights))):
            a_prev = self.activations[i]
            self.dw[i] = a_prev.T @ dz / m
            self.db[i] = np.sum(dz, axis=0, keepdims=True) / m
            if i > 0:
                dz = dz @ self.weights[i].T * self.activation_grad(self.zs[i - 1])

    def update(self, lr):
        for i in range(len(self.weights)):
            self.weights[i] -= lr * self.dw[i]
            self.biases[i] -= lr * self.db[i]

    def train(self, X, y, epochs=10000, lr=0.1):
        history = []
        for _ in range(epochs):
            y_pred = self.forward(X)
            loss = np.mean((y - y_pred) ** 2)
            history.append(loss)
            self.backward(y)
            self.update(lr)
        return history

    def predict(self, X):
        return (self.forward(X) > 0.5).astype(int)

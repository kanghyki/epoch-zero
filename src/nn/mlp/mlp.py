import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_grad(x):
    s = sigmoid(x)
    return s * (1 - s)

class MLP:
    def __init__(self, layer_sizes):  # 예: [2(입력), 4, 4, 1(출력)]
        self.layer_sizes = layer_sizes
        self.weights = []
        self.biases = []

        # 가중치와 편향 초기화
        for i in range(len(layer_sizes) - 1):
            w = np.random.randn(layer_sizes[i], layer_sizes[i + 1])
            b = np.zeros((1, layer_sizes[i + 1]))
            self.weights.append(w)
            self.biases.append(b)

    def forward(self, X):
        self.activations = [X]
        self.zs = []

        a = X
        for w, b in zip(self.weights, self.biases):
            z = a @ w + b
            a = sigmoid(z)
            self.zs.append(z)
            self.activations.append(a)

        return a  # 최종 출력

    def backward(self, y_true):
        m = y_true.shape[0]
        self.dw = [None] * len(self.weights)
        self.db = [None] * len(self.biases)

        # 출력층 오차
        dz = (self.activations[-1] - y_true) * sigmoid_grad(self.zs[-1])
        for i in reversed(range(len(self.weights))):
            a_prev = self.activations[i]
            self.dw[i] = a_prev.T @ dz / m
            self.db[i] = np.sum(dz, axis=0, keepdims=True) / m

            if i != 0:  # 입력층 이전은 없음
                dz = dz @ self.weights[i].T * sigmoid_grad(self.zs[i - 1])

    def update(self, lr):
        for i in range(len(self.weights)):
            self.weights[i] -= lr * self.dw[i]
            self.biases[i] -= lr * self.db[i]

    def train(self, X, y, epochs, lr):
        history = []
        for _ in range(epochs):
            y_pred = self.forward(X)
            loss = np.mean((y - y_pred) ** 2)
            history.append(loss)
            self.backward(y)
            self.update(lr)
        return history
    
    def predict(self, X):
        output = self.forward(X)
        return (output > 0.5).astype(int)

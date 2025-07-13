import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_grad(x):
    s = sigmoid(x)
    return s * (1 - s)

class MLP:
    def __init__(self, input_size=2, hidden_size=2, output_size=1):
        self.w1 = np.random.randn(input_size, hidden_size)
        self.b1 = np.zeros((1, hidden_size))
        self.w2 = np.random.randn(hidden_size, output_size)
        self.b2 = np.zeros((1, output_size))

    def forward(self, X):
        self.X = X  # 입력 저장
        self.z1 = X @ self.w1 + self.b1
        self.a1 = sigmoid(self.z1)
        self.z2 = self.a1 @ self.w2 + self.b2
        self.a2 = sigmoid(self.z2)
        return self.a2

    def backward(self, y_true):
        # 출력층 오차
        dz2 = (self.a2 - y_true) * sigmoid_grad(self.z2)
        self.dw2 = self.a1.T @ dz2
        self.db2 = np.sum(dz2, axis=0, keepdims=True)

        # 은닉층 오차
        dz1 = dz2 @ self.w2.T * sigmoid_grad(self.z1)
        self.dw1 = self.X.T @ dz1
        self.db1 = np.sum(dz1, axis=0, keepdims=True)

    def update(self, lr):
        self.w2 -= lr * self.dw2
        self.b2 -= lr * self.db2
        self.w1 -= lr * self.dw1
        self.b1 -= lr * self.db1

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
        return self.forward(X).round()
